import streamlit as st

st.set_page_config(page_title="Aprende Python", page_icon="🐍")
st.title("🐍 Aprende Python: while, for, if")
st.markdown("""
## 🧠 Introducción

Esta página te enseñará cómo funcionan las estructuras básicas de control en Python: `while`, `for`, e `if`.

---

### 🔁 Bucle While
El bucle `while` ejecuta un bloque de código **mientras** una condición sea verdadera.

```python
i = 0
while i < 5:
    print(i)
    i += 1
🔂 Bucle For
Se usa para recorrer elementos de una secuencia como listas, rangos, strings, etc.

for i in range(5):
    print(i)
🔀 Condicional If
Se usa para ejecutar código dependiendo del resultado de una condición.

x = 10
if x > 5:
    print("x es mayor que 5")
""")

st.header("📝 Quiz: Evalúa lo que aprendiste")

questions = [
{"question": "¿Qué hace un bucle while?", "options": ["Repite mientras la condición es verdadera", "Solo una vez", "Compara valores"], "answer": 0},
{"question": "¿Qué palabra se usa para condicionales?", "options": ["if", "loop", "while"], "answer": 0},
{"question": "¿Qué hace el bucle for?", "options": ["Repite sobre una secuencia", "Solo repite una vez", "Compara dos valores"], "answer": 0},
{"question": "¿Qué hace este código?\n\nx = 5\nif x > 3:\n print('Mayor')", "options": ["Imprime 'Mayor'", "Error", "Nada"], "answer": 0},
{"question": "¿Cuál es el resultado?\n\nfor i in range(3):\n print(i)", "options": ["0 1 2", "1 2 3", "3 2 1"], "answer": 0},
{"question": "¿Qué operador compara igualdad?", "options": ["==", "=", "!="], "answer": 0},
{"question": "¿Qué ocurre si while nunca se vuelve falso?", "options": ["Bucle infinito", "Error", "Nada"], "answer": 0},
{"question": "¿Qué hace 'if x == y'?", "options": ["Compara si x es igual a y", "Asigna y a x", "Termina el código"], "answer": 0},
{"question": "¿Qué palabra detiene un bucle?", "options": ["break", "stop", "exit"], "answer": 0},
{"question": "¿Qué hace este código?\n\ni = 0\nwhile i < 3:\n print(i)\n i += 1", "options": ["Imprime 0 1 2", "Imprime 1 2 3", "Nada"], "answer": 0}
]

user_answers = []

for i, q in enumerate(questions):
st.subheader(f"Pregunta {i+1}")
st.write(q["question"])
selected = st.radio("Selecciona una opción:", q["options"], key=f"q{i}")
user_answers.append(q["options"].index(selected))

if st.button("📊 Calcular puntaje"):
score = 0
for i, q in enumerate(questions):
if user_answers[i] == q["answer"]:
score += 1
st.success(f"Tu puntaje es: {score}/10")
if score == 10:
st.balloons()
st.markdown("🎉 ¡Felicidades! ¡Obtuviste el puntaje perfecto!")
