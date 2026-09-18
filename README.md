# HT5 — Sistemas multiagentes para Parachute S.A.

Implementación de tres estilos de orquestación para FAQs, evaluación climática
y calendarización de saltos.

## Estado de integración

| Componente | Estado | Ubicación |
|---|---|---|
| Arquitectura centralizada | Completa | `centralized/` |
| Arquitectura jerárquica | Completa; ya usa Open-Meteo real | `hierarchical/` |
| Arquitectura descentralizada | Pendiente de Integrante 3 | `decentralized/` |
| Cliente Open-Meteo compartido | Completo | `shared/open_meteo_client.py` |
| Evaluación de umbrales | Completa | `shared/weather_evaluator.py` |
| FAQs del Lab 4 y reservas persistentes | Pendientes de Integrante 3 | — |
| PDF con ambas respuestas | Pendiente de Integrante 3 | — |

La arquitectura centralizada contiene FAQs y reservas provisionales para poder
ejecutar el flujo completo. Están aisladas de la integración climática y se
pueden reemplazar sin modificar Open-Meteo ni sus reglas.

## Diseño compartido

```text
Arquitectura centralizada ─┐
Arquitectura jerárquica  ──┼─> weather_service ─> Open-Meteo
Arquitectura descentralizada┘          │
                                      └─> weather_evaluator
```

El cliente consulta las coordenadas **14.013722, -90.771611**, valida que la
fecha no haya pasado ni exceda 16 días, solicita las cinco variables y las
adapta a `WeatherReading`. El evaluador puro devuelve `ideal`, `marginal` o
`prohibido` con motivos y restricciones.

## Instalación rápida

```bash
python -m venv .venv
```

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Configura `OPENAI_API_KEY` en `.env` y ejecuta:

```bash
python -m centralized.main
python -m hierarchical.main
```

Pruebas:

```bash
python -m pytest -q
```

Consulta `docs/EJECUCION_INTEGRANTE1.md` y
`docs/EJECUCION_INTEGRANTE2.md`. Los diagramas están en `diagrams/`.

## Autores

- Juan Jose Rivas Alvarez — carnet universitario 24856 — arquitectura
  centralizada e integración Open-Meteo.
