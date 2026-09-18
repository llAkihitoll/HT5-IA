"""Agente de Clima — Integrante 2 (arquitectura jerárquica).

Obtiene datos climáticos (por ahora vía el stub provisional
`weather_provider_stub`, hasta que exista la integración real con
Open-Meteo del Integrante 1) y los evalúa con el módulo compartido
`shared.weather_evaluator`. No decide reservas ni responde FAQs.
"""

from agents import Agent, function_tool

from hierarchical.weather_provider_stub import get_weather_reading
from shared.weather_evaluator import evaluate_weather


@function_tool
def consultar_clima_salto(fecha_iso: str) -> str:
    """Consulta el clima en el sitio de aterrizaje para `fecha_iso`
    (formato YYYY-MM-DD) y determina si las condiciones permiten realizar
    el salto (ideal, marginal o prohibido), con motivos y restricciones."""

    reading, error = get_weather_reading(fecha_iso)
    if error:
        return error

    assessment = evaluate_weather(reading)

    lines = [f"Estado del clima para {fecha_iso}: {assessment.status.upper()}."]
    if assessment.reasons:
        lines.append("Motivos: " + "; ".join(assessment.reasons))
    if assessment.restrictions:
        lines.append("Restricciones: " + "; ".join(assessment.restrictions))
    return "\n".join(lines)


weather_agent = Agent(
    name="Agente Clima",
    handoff_description=(
        "Consulta las condiciones climáticas del sitio de aterrizaje para una "
        "fecha y determina si el salto es ideal, marginal o está prohibido."
    ),
    instructions=(
        "Eres el agente climático de Parachute S.A. Usa consultar_clima_salto "
        "con la fecha solicitada por el usuario (formato YYYY-MM-DD) y reporta "
        "el estado, los motivos y las restricciones tal como te los devuelve "
        "la herramienta, sin inventar información adicional."
    ),
    tools=[consultar_clima_salto],
)
