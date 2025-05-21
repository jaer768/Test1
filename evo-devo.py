import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(page_title="Evo-Devo", layout="wide", page_icon="🧬")

st.title("🧬 Evo-Devo: Biología Evolutiva del Desarrollo")
st.markdown("""
**Evo-Devo**, o Biología Evolutiva del Desarrollo, es un campo que estudia cómo los cambios en el desarrollo de los organismos contribuyen a la evolución de nuevas formas y estructuras. Combina conocimientos de genética, embriología, paleontología y biología molecular para entender cómo la evolución moldea el desarrollo.

### 🧠 ¿Por qué es importante?
- Ayuda a explicar cómo surgen nuevas características morfológicas.
- Relaciona genes del desarrollo con la evolución de las especies.
- Revela similitudes ocultas entre organismos diferentes.

### 📚 Referencias científicas
1. Carroll, S.B. (2005). *Endless Forms Most Beautiful*. W.W. Norton & Company.
2. Gilbert, S.F. (2014). *Developmental Biology* (10th ed.). Sinauer Associates.
3. Hall, B.K. (1992). *Evolutionary Developmental Biology*. Springer.
""")

# Función para insertar video YouTube con embed HTML (solo video introducción)
def embed_youtube(video_id, height=315):
    html_code = f"""
    <iframe width="100%" height="{height}" src="https://www.youtube.com/embed/{video_id}" 
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """
    components.html(html_code, height=height + 20)

st.header("🎬 Recurso Multimedia")

st.subheader("📘 ¿Qué es la biología evolutiva del desarrollo?")
embed_youtube("5MfSYnItYvg")  # Video "What is Evo-Devo?"

# Cuestionario
st.header("📝 Cuestionario Evo-Devo")

questions = [
    {
        "question": "¿Qué son los genes Hox?",
        "options": [
            "Genes que regulan el metabolismo celular",
            "Genes involucrados en la formación de órganos sexuales",
            "Genes que determinan la identidad de los segmentos corporales",
            "Genes responsables del sistema inmunológico"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué disciplina integra Evo-Devo?",
        "options": [
            "Embriología y genética",
            "Geología y astronomía",
            "Física cuántica",
            "Química orgánica"
        ],
        "answer": 0
    },
    {
        "question": "¿Cuál es un concepto clave en Evo-Devo?",
        "options": [
            "La ley de Hardy-Weinberg",
            "La selección artificial",
            "La modularidad del desarrollo",
            "La mecánica cuántica"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué papel juegan los genes reguladores?",
        "options": [
            "Controlan la expresión de otros genes durante el desarrollo",
            "Producen energía celular",
            "Intervienen en la digestión",
            "No tienen ninguna función conocida"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué animal ha sido un modelo común en estudios Evo-Devo?",
        "options": [
            "Perro",
            "Ser humano",
            "Mosca de la fruta (Drosophila)",
            "Elefante"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué sugiere la conservación de genes del desarrollo entre especies?",
        "options": [
            "Las especies no están relacionadas",
            "La evolución no ocurre",
            "Hay un ancestro común",
            "Los genes del desarrollo no son importantes"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué indica un cambio en la expresión espacial de un gen Hox?",
        "options": [
            "Cambio en el color de ojos",
            "Alteración en la forma corporal",
            "Incremento de velocidad metabólica",
            "Mejora de la audición"
        ],
        "answer": 1
    },
    {
        "question": "¿Cuál es un descubrimiento importante de Evo-Devo?",
        "options": [
            "Los agujeros negros",
            "La tectónica de placas",
            "Los genes homeóticos",
            "La fotosíntesis"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué término describe la aparición repetida de estructuras similares?",
        "options": [
            "Convergencia evolutiva",
            "Deriva genética",
            "Pérdida adaptativa",
            "Especiación alopátrica"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué muestra la heterocronía en Evo-Devo?",
        "options": [
            "Cambios en el tiempo del desarrollo",
            "Cambios en la temperatura",
            "Cambios hormonales en adultos",
            "Cambios en el ciclo del agua"
        ],
        "answer": 0
    }
]

user_answers = []
score = 0

with st.form("quiz_form"):
    for idx, q in enumerate(questions):
        st.subheader(f"Pregunta {idx + 1}: {q['question']}")
        user_answers.append(st.radio("Selecciona una respuesta:", q["options"], key=idx))
    submitted = st.form_submit_button("Enviar respuestas")

    if submitted:
        for i, q in enumerate(questions):
            if q["options"].index(user_answers[i]) == q["answer"]:
                score += 1

        st.success(f"Tu puntaje es {score}/10")

        if score == 10:
            st.balloons()
            st.markdown("🎉 ¡Excelente! ¡Has obtenido el puntaje perfecto! 🎉")
