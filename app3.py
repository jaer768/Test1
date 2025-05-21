import streamlit as st

st.set_page_config(page_title="Aprende Python", page_icon="🐍")
st.title("🐍 Aprende Python: while, for, if")

st.markdown
## Introducción a Python

Aquí aprenderás cómo funcionan las estructuras de control básicas en Python: `while`, `for` e `if`.

---

### Bucle While
Ejecuta un bloque de código mientras una condición sea verdadera.

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
{"question": "¿Qué palabra clave se usa para condicionales?", 
 "options": ["if", "for", "while"], "answer": 0},

{"question": "¿Para qué sirve un bucle for?", 
 "options": ["Iterar sobre secuencias", "Comparar valores", "Detener el programa"], "answer": 0},

{"question": "¿Qué imprime este código?\n\nx=3\nif x > 5:\n  print('Mayor')\nelse:\n  print('Menor')", 
 "options": ["Mayor", "Menor", "Error"], "answer": 1},

{"question": "¿Cuál es la salida de:\n\nfor i in range(3):\n  print(i)", 
 "options": ["0 1 2", "1 2 3", "3 2 1"], "answer": 0},

{"question": "¿Qué operador compara igualdad?", 
 "options": ["==", "=", "!="], "answer": 0},

{"question": "¿Qué sucede si la condición de un while nunca es falsa?", 
 "options": ["Bucle infinito", "Error", "Se ejecuta una vez"], "answer": 0},

{"question": "¿Qué significa 'if x == y'?", 
 "options": ["Compara si x es igual a y", "Asigna y a x", "Es un error"], "answer": 0},

{"question": "¿Qué palabra se usa para salir de un bucle?", 
 "options": ["break", "stop", "exit"], "answer": 0},

{"question": "¿Qué imprime este código?\n\ni=0\nwhile i<3:\n  print(i)\n  i +=1", 
 "options": ["0 1 2", "1 2 3", "Nada"], "answer": 0}
