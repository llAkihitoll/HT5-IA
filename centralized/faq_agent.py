"""Especialista provisional de FAQs; se reemplazará por la base del Lab 4."""

from agents import Agent, function_tool

_FAQS = {
    "tandem": (
        "Un salto tándem se realiza sujeto a un instructor certificado y no "
        "requiere experiencia previa."
    ),
    "edad": "La edad mínima es 18 años y se requiere identificación vigente.",
    "llevar": (
        "Debes llevar ropa cómoda, zapatos cerrados y llegar una hora antes."
    ),
    "cancelar": "Puedes cancelar o reprogramar hasta 24 horas antes sin costo.",
}


@function_tool
def buscar_faq(pregunta: str) -> str:
    """Busca una respuesta en la base provisional de preguntas frecuentes."""

    normalized = pregunta.casefold()
    for keyword, answer in _FAQS.items():
        if keyword in normalized:
            return answer
    return "No encontré esa información en la base provisional de FAQs."


faq_agent = Agent(
    name="Agente de FAQs",
    instructions=(
        "Responde únicamente con información obtenida mediante buscar_faq. "
        "No gestiones clima ni reservas."
    ),
    tools=[buscar_faq],
)
