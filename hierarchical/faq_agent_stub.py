"""Agente de FAQs — placeholder provisional del Integrante 2.

La búsqueda real de FAQs, adaptada del Lab 4, es responsabilidad del
Integrante 3 (ver sección 5 del enunciado de la HT5). Este archivo NO debe
tomarse como la entrega final de esa parte: es solo lo mínimo necesario
para poder demostrar que el Supervisor General sabe delegar hacia un
agente de FAQs dentro de la arquitectura jerárquica.

Cuando el Integrante 3 tenga lista su implementación, `supervisor.py` debe
importar su agente en lugar de `faq_agent` de este archivo.
"""

from agents import Agent, function_tool

_FAQ_KB = [
    (
        "¿Qué es un salto en tándem?",
        "Es un salto donde vas sujeto a un instructor certificado; no requiere experiencia previa.",
    ),
    (
        "¿Cuál es la edad mínima para saltar?",
        "18 años, presentando identificación vigente el día del salto.",
    ),
    (
        "¿Qué debo llevar el día del salto?",
        "Ropa cómoda, zapatos cerrados, y llegar con 1 hora de anticipación para el brief de seguridad.",
    ),
    (
        "¿Puedo cancelar o reprogramar mi cita?",
        "Sí, hasta 24 horas antes sin costo adicional.",
    ),
]


@function_tool
def buscar_faq(pregunta: str) -> str:
    """Busca una respuesta en la base de conocimiento de preguntas frecuentes
    de Parachute S.A. (placeholder: base de conocimiento mínima de ejemplo)."""

    palabras = [w for w in pregunta.lower().split() if len(w) > 3]
    for question, answer in _FAQ_KB:
        if any(word in question.lower() for word in palabras):
            return answer
    return (
        "No encontré una respuesta exacta en las FAQs disponibles. "
        "(Base de conocimiento placeholder del Integrante 2; la búsqueda real "
        "de FAQs del Lab 4 la implementa el Integrante 3.)"
    )


faq_agent = Agent(
    name="Agente FAQs",
    handoff_description=(
        "Responde preguntas frecuentes de Parachute S.A. usando la base de "
        "conocimiento (requisitos, políticas, información general)."
    ),
    instructions=(
        "Eres el agente de preguntas frecuentes de Parachute S.A. Usa "
        "buscar_faq para responder las preguntas del usuario."
    ),
    tools=[buscar_faq],
)
