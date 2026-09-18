# Diagrama — Arquitectura jerárquica (Integrante 2)

Este diagrama corresponde exactamente al código en `hierarchical/` y
`shared/`. Las líneas continuas son relaciones de delegación implementadas
con `Agent.as_tool()` del SDK de OpenAI Agents. Las líneas punteadas
marcan los componentes **placeholder/provisionales** que deben
reemplazarse por las entregas reales de Integrante 1 (Open-Meteo) e
Integrante 3 (FAQs del Lab 4, almacenamiento de citas).

```mermaid
graph TD
    U["Usuario"] -->|"solicitud en lenguaje natural"| S["Supervisor General<br/>(hierarchical/supervisor.py)"]

    S -->|"as_tool: responder_faq"| F["Agente FAQs<br/>(hierarchical/faq_agent_stub.py)"]
    S -->|"as_tool: gestionar_operaciones"| OM["Submanager Operaciones<br/>(hierarchical/operations_manager.py)"]

    OM -->|"as_tool: consultar_clima"| WA["Agente Clima<br/>(hierarchical/weather_agent.py)"]
    OM -->|"as_tool: gestionar_reserva"| BA["Agente Reservas<br/>(hierarchical/booking_agent_stub.py)"]

    WA -->|"llamada de función pura<br/>(no es un agente ni un tool call)"| EV["Evaluador Climático<br/>(shared/weather_evaluator.py)<br/>ideal / marginal / prohibido<br/>+ motivos + restricciones"]
    WA -.->|"obtiene WeatherReading<br/>PLACEHOLDER"| WP["weather_provider_stub.py<br/>(simula Open-Meteo)"]

    F -.->|"PLACEHOLDER"| FKB[("Mini base de FAQs<br/>de ejemplo")]
    BA -.->|"PLACEHOLDER"| BKB[("Citas en memoria<br/>sin dedup")]

    classDef mine fill:#d4edda,stroke:#2e7d32,color:#1b1b1b;
    classDef stub fill:#fdf3d7,stroke:#a0522d,stroke-dasharray: 4 2,color:#1b1b1b;

    class S,OM,WA,EV mine;
    class F,BA,WP,FKB,BKB stub;
```

## Equivalente en texto (por si no se renderiza Mermaid)

```
                              Usuario
                                 │
                                 ▼
                       Supervisor General                         ← mi entrega
                        /                \
             as_tool: responder_faq   as_tool: gestionar_operaciones
                      /                        \
                     ▼                          ▼
              Agente FAQs              Submanager Operaciones      ← mi entrega
            (placeholder Lab4)          /                  \
                                as_tool: consultar_clima   as_tool: gestionar_reserva
                                       /                          \
                                      ▼                            ▼
                              Agente Clima                 Agente Reservas
                             (mi entrega)                  (placeholder)
                                   │
                      llamada de función pura
                                   │
                                   ▼
                     Evaluador Climático (shared/weather_evaluator.py)   ← mi entrega
                     ideal / marginal / prohibido + motivos + restricciones
                                   ▲
                                   │ obtiene WeatherReading
                                   │
                        weather_provider_stub.py (placeholder de Open-Meteo)
```

## Puntos clave que el diagrama hace evidentes

1. **Jerarquía de dos niveles real**: el Supervisor General nunca llama
   directamente a Clima o Reservas — siempre pasa por el Submanager de
   Operaciones. No hay una arquitectura centralizada disfrazada.
2. **Sin handoffs**: todas las flechas de delegación son `Agent.as_tool()`
   (el agente que delega mantiene el control de la conversación), no
   `handoff` (que transferiría el control). Esto distingue la arquitectura
   jerárquica de la descentralizada del Integrante 3.
3. **El Evaluador Climático es un módulo compartido, no un agente**: no
   aparece como nodo con `as_tool()` porque no es un agente — es una
   función pura (`evaluate_weather`) que el Agente Clima invoca
   directamente. Esto es lo que permite reutilizarlo sin cambios en las
   arquitecturas centralizada y descentralizada.
4. **Componentes provisionales claramente marcados** (punteados): el
   proveedor climático, el agente de FAQs y el agente de reservas son
   placeholders mínimos que existen solo para poder demostrar el flujo
   completo mientras Integrante 1 e Integrante 3 no entregan sus partes.
