import streamlit as st

st.set_page_config(page_title="Aprende Python", page_icon="🐍")

st.title("🐍 Aprende Python: while, for, if")
st.markdown("""
Bienvenido a esta mini web para aprender sobre las estructuras de control en Python.

### 🔁 Bucle While
El bucle `while` ejecuta un bloque de código **mientras** una condición sea verdadera.

```python
i = 0
while i < 5:
    print(i)
    i += 1
for i in range(5):
    print(i)
x = 10
if x > 5:
    print("x es mayor que 5")
st.header("🧠 Quiz: ¿Cuánto sabes de Python?")
questions = [
{
"question": "¿Qué hace un bucle while?",
"options": [
"Repite código mientras una condición sea verdadera",
"Repite código una vez",
"Compara dos valores"
],
"answer": 0
},
{
"question": "¿Cuál es la sintaxis correcta de un for?",
"options": [
"for x en 5:",
"for x from range(5):",
"for x in range(5):"
],
"answer": 2
},
{
"question": "¿Qué palabra clave se usa para condicionales?",
"options": [
"for",
"if",
"while"
],
"answer": 1
},
{
"question": "¿Qué imprime este código?\n\nx = 3\nif x > 5:\n print('Mayor')\nelse:\n print('Menor')",
"options": [
"Mayor",
"Menor",
"Error"
],
"answer": 1
},
{
"question": "¿Cuál es la salida de este código?\n\nfor i in range(2):\n print(i)",
"options": [
"2 1",
"0 1",
"1 2"
],
"answer": 1
},
{
"question": "¿Qué hace el operador ==?",
"options": [
"Asigna valor",
"Compara igualdad",
"Finaliza bucles"
],
"answer": 1
},
{
"question": "¿Qué hace este código?\n\ni = 0\nwhile i < 3:\n i += 1\nprint(i)",
"options": [
"3",
"0 1 2",
"1 2 3"
],
"answer": 0
},
{
"question": "¿Cuál es un error común en while?",
"options": [
"No incrementar la variable de control",
"Usar break",
"Usar range"
],
"answer": 0
},
{
"question": "¿Qué significa 'if x == y'?",
"options": [
"x es igual a y",
"asigna y a x",
"x es diferente de y"
],
"answer": 0
},
{
"question": "¿Cuál es la salida?\n\nfor x in 'hi':\n print(x)",
"options": [
"h\ni",
"hi",
"error"
],
"answer": 0
},
]

Mostrar preguntas

user_answers = []
for idx, q in enumerate(questions):
st.subheader(f"Pregunta {idx+1}: {q['question']}")
choice = st.radio(
label="Selecciona una respuesta:",
options=q["options"],
key=f"q_{idx}"
)
user_answers.append(q["options"].index(choice))

Botón para mostrar puntaje

if st.button("📊 Verificar puntaje"):
score = 0
for idx, q in enumerate(questions):
if user_answers[idx] == q["answer"]:
score += 1
st.success(f"Tu puntaje es: {score}/10")

if score == 10:
    st.balloons()
    st.markdown("🎉 ¡Puntaje perfecto! ¡Tardis Time!")
    st.image("tardis.gif", caption="Mini TARDIS viajando en el tiempo 🛸")

---

### 📦 requirements.txt

streamlit


---

### 📤 ¿Cómo subir a GitHub?

1. Crea un repositorio.
2. Agrega los archivos `app.py`, `requirements.txt`, y `tardis.gif`.
3. Haz commit y push.

---

### 🚀 Cómo correrlo en tu PC

```bash
streamlit run app.py
