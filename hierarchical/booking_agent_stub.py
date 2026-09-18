"""Agente de Reservas — placeholder provisional del Integrante 2.

El almacenamiento real de citas y la prevención de duplicados son
responsabilidad del Integrante 3 (ver sección 5 del enunciado de la HT5).
Este archivo NO debe tomarse como la entrega final de esa parte: es solo
lo mínimo necesario para poder demostrar que el Submanager de Operaciones
sabe delegar hacia un agente de reservas dentro de la arquitectura
jerárquica, después de haber consultado el clima.

Cuando el Integrante 3 tenga lista su implementación (con persistencia y
prevención de duplicados), `operations_manager.py` debe importar su
agente en lugar de `booking_agent` de este archivo.
"""

from agents import Agent, function_tool

_bookings: list[dict[str, str]] = []


@function_tool
def calendarizar_cita(fecha_iso: str, nombre_cliente: str) -> str:
    """Registra una cita de salto para `nombre_cliente` en `fecha_iso`
    (formato YYYY-MM-DD). Implementación placeholder en memoria, sin
    prevención de duplicados."""

    _bookings.append({"fecha": fecha_iso, "cliente": nombre_cliente})
    return f"Cita registrada (placeholder) para {nombre_cliente} el {fecha_iso}."


booking_agent = Agent(
    name="Agente Reservas",
    handoff_description="Calendariza citas de salto para clientes de Parachute S.A.",
    instructions=(
        "Eres el agente de reservas de Parachute S.A. Usa calendarizar_cita "
        "para registrar la cita solicitada. Confía en que quien te invoca ya "
        "verificó que el clima lo permite."
    ),
    tools=[calendarizar_cita],
)
