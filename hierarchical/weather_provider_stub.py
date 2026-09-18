"""Proveedor climático MOCK — placeholder provisional del Integrante 2.

Simula lo que la integración real con Open-Meteo (responsabilidad del
Integrante 1, ver sección 3 del enunciado de la HT5) va a entregar. NO
hace ninguna llamada HTTP ni conoce la API real. Existe únicamente para
poder demostrar el flujo completo:

    Supervisor -> Submanager -> Agente Clima -> Evaluador

mientras esa integración no exista en el repositorio.

Cuando el Integrante 1 tenga lista su integración real (con su propia
validación de fecha y obtención de las 5 variables desde Open-Meteo),
`weather_agent.py` debe importar esa función en lugar de
`get_weather_reading` de este archivo, y este archivo puede eliminarse.
"""

import hashlib
from datetime import date, datetime

from shared.weather_contracts import WeatherReading

LANDING_LATITUDE = 14.013722
LANDING_LONGITUDE = -90.771611
MAX_FORECAST_DAYS = 16


def _parse_date(fecha_iso: str) -> date | None:
    try:
        return datetime.strptime(fecha_iso, "%Y-%m-%d").date()
    except ValueError:
        return None


def get_weather_reading(fecha_iso: str) -> tuple[WeatherReading | None, str | None]:
    """Devuelve una lectura climática simulada para `fecha_iso` (YYYY-MM-DD).

    Respeta la limitación real de Open-Meteo (máximo 16 días de pronóstico)
    para que la demo sea representativa: si la fecha pedida excede ese
    horizonte, devuelve un mensaje de error en vez de datos inventados.

    Devuelve (reading, None) en caso de éxito o (None, mensaje_error) si la
    fecha es inválida o está fuera de rango.
    """

    requested = _parse_date(fecha_iso)
    if requested is None:
        return None, f"Fecha inválida: '{fecha_iso}'. Usa el formato YYYY-MM-DD."

    days_ahead = (requested - date.today()).days
    if days_ahead < 0:
        return None, f"La fecha {fecha_iso} ya pasó."
    if days_ahead > MAX_FORECAST_DAYS:
        return None, (
            f"No es posible consultar el pronóstico para {fecha_iso}: "
            f"Open-Meteo solo predice hasta {MAX_FORECAST_DAYS} días."
        )

    # Valores deterministas derivados de la fecha (mismo input -> mismo
    # output), útiles para demos y pruebas reproducibles. NO son datos
    # climáticos reales.
    seed = int(hashlib.sha256(fecha_iso.encode()).hexdigest(), 16)
    return (
        WeatherReading(
            wind_speed_10m=round((seed % 400) / 10, 1),
            wind_gust_10m=round((seed // 400 % 500) / 10, 1),
            precipitation=round((seed // 200_000 % 30) / 10, 1),
            cloud_cover=float(seed // 6_000_000 % 101),
            temperature_2m=round(15 + (seed // 600_000_000 % 150) / 10, 1),
        ),
        None,
    )
