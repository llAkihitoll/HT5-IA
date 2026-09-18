"""Manager único de la arquitectura centralizada."""

from agents import Agent

from centralized.booking_agent import booking_agent
from centralized.faq_agent import faq_agent
from centralized.weather_agent import weather_agent

manager = Agent(
    name="Manager Central",
    instructions=(
        "Eres el único punto de contacto de Parachute S.A. Conservas el control "
        "de la conversación y coordinas tres agentes como herramientas.\n"
        "- Usa responder_faq para preguntas informativas.\n"
        "- Usa consultar_clima para evaluar una fecha.\n"
        "- Usa registrar_reserva para guardar una cita.\n\n"
        "REGLA OBLIGATORIA: antes de cada reserva llama consultar_clima para la "
        "misma fecha, incluso si crees conocer el resultado. Si el resultado es "
        "PROHIBIDO o contiene un error, no llames registrar_reserva. Si es "
        "MARGINAL por viento, solo registra si el usuario confirma que es un "
        "tándem experimentado; en otro caso explica la restricción. Si es IDEAL, "
        "puedes registrar. Nunca inventes datos ni confirmes una cita sin recibir "
        "la confirmación de registrar_reserva."
    ),
    tools=[
        faq_agent.as_tool(
            tool_name="responder_faq",
            tool_description="Responde preguntas frecuentes de Parachute S.A.",
        ),
        weather_agent.as_tool(
            tool_name="consultar_clima",
            tool_description=(
                "Consulta Open-Meteo y evalúa la seguridad del salto para una fecha."
            ),
        ),
        booking_agent.as_tool(
            tool_name="registrar_reserva",
            tool_description=(
                "Registra una cita ya autorizada; nunca sustituye la revisión climática."
            ),
        ),
    ],
)
