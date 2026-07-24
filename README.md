# ComuHR AI

Asistente de inteligencia artificial con arquitectura RAG para consultar políticas
internas ficticias de **NovaTech Guatemala, S.A.**

> Todos los documentos y datos incluidos son ficticios y fueron creados únicamente
> para fines educativos. El proyecto no contiene información real de una empresa.

## Problema

Las políticas internas suelen estar distribuidas entre distintos documentos. Esto
provoca consultas repetitivas, tiempo perdido y respuestas inconsistentes.

## Solución

ComuHR AI permite hacer preguntas en lenguaje natural y genera respuestas basadas
exclusivamente en una base documental controlada. También muestra los documentos
y páginas recuperados para facilitar la trazabilidad.

## Funcionalidades del MVP

- Lectura de múltiples archivos PDF.
- División del texto en fragmentos.
- Embeddings con Gemini.
- Búsqueda semántica con FAISS.
- Respuestas generadas con Gemini.
- Referencia a documentos y páginas.
- Manejo explícito de preguntas sin respuesta documental.
- Interfaz conversacional con Streamlit.

## Arquitectura

```text
PDF → PyPDFLoader → fragmentación → embeddings → FAISS
                                             ↓
Pregunta → búsqueda semántica → contexto → Gemini → respuesta y fuentes
```

## Estructura

```text
comuhr-ai/
├── app.py
├── data/
│   ├── Politica_de_Confidencialidad.pdf
│   ├── Politica_de_Permisos_y_Ausencias.pdf
│   └── Politica_de_Vacaciones.pdf
├── docs/
│   ├── AI_PROJECT_CANVAS.md
│   └── PREGUNTAS_DE_PRUEBA.md
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.11 o 3.12.
- Una clave de la API de Gemini.
- Conexión a internet durante la indexación y generación de respuestas.

## Instalación en Windows

```powershell
git clone URL_DE_TU_REPOSITORIO
cd comuhr-ai

python -m venv .venv
.\.venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

copy .env.example .env
```

Abre `.env` y reemplaza `tu_clave_aqui` con tu clave.

## Ejecución

```powershell
streamlit run app.py
```

La terminal mostrará una dirección local, normalmente:

```text
http://localhost:8501
```

## Pruebas recomendadas

### Preguntas cuya respuesta está en los documentos

- ¿Cuántos días hábiles de vacaciones corresponden por cada año?
- ¿Con cuánto tiempo debo solicitar vacaciones?
- ¿Qué debo hacer antes de salir de vacaciones?
- ¿Con cuánto tiempo se solicita un permiso previsible?
- ¿Puedo colocar contratos reales en una herramienta pública de IA?
- ¿Qué debo hacer si envié información al destinatario equivocado?

### Preguntas fuera del alcance

- ¿La empresa ofrece seguro dental?
- ¿Cuál es el salario de un analista?
- ¿Cuántos días de teletrabajo hay por semana?

El comportamiento esperado es reconocer que esa información no aparece en las
políticas y recomendar la consulta al área responsable.

## Decisiones técnicas

- Se utiliza recuperación semántica para encontrar fragmentos relacionados con la
  pregunta aunque no usen exactamente las mismas palabras.
- La temperatura del modelo es baja para reducir variaciones.
- El prompt prohíbe completar vacíos con conocimiento general.
- Se muestran fuentes recuperadas para mejorar la transparencia.
- No se almacenan documentos reales ni datos personales.

## Limitaciones

- Una respuesta generada por IA todavía puede contener errores.
- FAISS se crea nuevamente al iniciar la aplicación.
- No hay autenticación ni perfiles de usuario.
- No se evalúa automáticamente la fidelidad de cada respuesta.
- El prototipo no debe usarse para decisiones laborales o legales reales.

## Próximas mejoras

- Persistir el índice vectorial.
- Permitir carga controlada de documentos.
- Añadir evaluación automática de respuestas.
- Incorporar filtros por tipo de política.
- Desplegar la aplicación en la nube.
- Registrar métricas sin almacenar información sensible.

## Autor

Proyecto desarrollado para el Challenge AluraAgente de ONE AI.
