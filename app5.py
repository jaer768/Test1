import streamlit as st
import random

st.set_page_config(page_title="Aprende Python - Condicionales y Bucles", page_icon="🐍", layout="wide")

# Título y descripción
st.title("🐍 Aprende Python: Condicionales y Bucles")
st.markdown("""
Bienvenido a esta mini lección interactiva. Hoy aprenderás sobre:

- `if`: Estructura condicional.
- `for`: Bucle determinado.
- `while`: Bucle indeterminado.

Vamos a repasar cada uno con una breve explicación y luego pondrás a prueba tu conocimiento con un quiz.
""")

# Sección educativa
with st.expander("📘 ¿Cómo funciona `if`?"):
    st.code("""
x = 10
if x > 5:
    print("x es mayor que 5")
""", language='python')
    st.write("`if` evalúa una condición: si se cumple, ejecuta el bloque de código.")

with st.expander("🔁 ¿Cómo funciona `for`?"):
    st.code("""
for i in range(5):
    print(i)
""", language='python')
    st.write("`for` se usa para iterar un número determinado de veces.")

with st.expander("🔁 ¿Cómo funciona `while`?"):
    st.code("""
x = 0
while x < 5:
    print(x)
    x += 1
""", language='python')
    st.write("`while` repite un bloque mientras la condición sea verdadera.")

# Quiz
st.subheader("🧠 Quiz: ¿Qué tanto aprendiste?")
st.markdown("Selecciona la alternativa correcta para cada pregunta:")

# Preguntas
preguntas = [
    {
        "pregunta": "¿Qué palabra se usa para ejecutar código si una condición es verdadera?",
        "opciones": ["if", "for", "while"],
        "respuesta": "if"
    },
    {
        "pregunta": "¿Qué bucle se usa cuando conocemos el número de iteraciones?",
        "opciones": ["while", "if", "for"],
        "respuesta": "for"
    },
    {
        "pregunta": "¿Qué estructura se ejecuta mientras una condición se mantenga verdadera?",
        "opciones": ["for", "if", "while"],
        "respuesta": "while"
    },
    {
        "pregunta": "¿Qué imprime este código? `for i in range(3): print(i)`",
        "opciones": ["0 1 2", "1 2 3", "3 2 1"],
        "respuesta": "0 1 2"
    },
    {
        "pregunta": "¿Qué operador representa 'igual a' en Python?",
        "opciones": ["=", "==", "!="],
        "respuesta": "=="
    },
    {
        "pregunta": "¿Qué sucede si la condición de un `while` nunca es falsa?",
        "opciones": ["Error de sintaxis", "Se ejecuta una vez", "Bucle infinito"],
        "respuesta": "Bucle infinito"
    },
    {
        "pregunta": "¿Cuál es la salida de este código?\n`x = 5\nif x == 5:\n    print('Sí')`",
        "opciones": ["No", "Sí", "Error"],
        "respuesta": "Sí"
    },
    {
        "pregunta": "¿Cuál es el rango de `range(3)`?",
        "opciones": ["0 1 2", "1 2 3", "0 1 2 3"],
        "respuesta": "0 1 2"
    },
    {
        "pregunta": "¿Qué hace este código? `for letra in 'abc': print(letra)`",
        "opciones": ["abc", "a b c", "c b a"],
        "respuesta": "a b c"
    },
    {
        "pregunta": "¿Cómo salimos de un bucle anticipadamente?",
        "opciones": ["continue", "break", "exit"],
        "respuesta": "break"
    },
]

# Respuestas del usuario
respuestas_usuario = []
puntos = 0

with st.form("quiz_form"):
    for i, q in enumerate(preguntas):
        seleccion = st.radio(f"{i+1}. {q['pregunta']}", q['opciones'], key=f"pregunta_{i}")
        respuestas_usuario.append(seleccion)
    submit = st.form_submit_button("Calcular Puntaje")

if submit:
    for i, q in enumerate(preguntas):
        if respuestas_usuario[i] == q['respuesta']:
            puntos += 1

    st.success(f"Obtuviste {puntos} de {len(preguntas)} puntos.")

    if puntos == len(preguntas):
        st.balloons()
        st.markdown("🎉 ¡Perfecto! Has respondido todas correctamente.")
    elif puntos >= 7:
        st.markdown("👍 ¡Buen trabajo! Puedes repasar para perfeccionar.")
    else:
        st.markdown("📘 Te recomendamos revisar las secciones anteriores.")
