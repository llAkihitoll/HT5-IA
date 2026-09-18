"""Especialista provisional de reservas para demostrar la coordinación."""

from agents import Agent, function_tool

_bookings: set[tuple[str, str]] = set()


def save_booking(fecha_iso: str, nombre_cliente: str) -> str:
    """Guarda en memoria y evita repetir la misma cita durante la ejecución."""

    key = (fecha_iso.strip(), nombre_cliente.strip().casefold())
    if key in _bookings:
        return f"La cita de {nombre_cliente} para {fecha_iso} ya existe."
    _bookings.add(key)
    return f"Cita registrada para {nombre_cliente} el {fecha_iso}."


@function_tool
def calendarizar_cita(fecha_iso: str, nombre_cliente: str) -> str:
    """Registra una cita que el manager ya autorizó después de revisar clima."""

    return save_booking(fecha_iso, nombre_cliente)


booking_agent = Agent(
    name="Agente de Reservas",
    instructions=(
        "Registra citas mediante calendarizar_cita. El manager central debe "
        "haber autorizado la operación después de consultar el clima."
    ),
    tools=[calendarizar_cita],
)
