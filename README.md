# 🧠 TALLER DE LENGUAJE Y AUTÓMATAS FINITOS DETERMINISTAS

## Descripción general

Este taller corresponde a la práctica sobre **lenguajes formales, tokens y autómatas finitos deterministas (AFD)**.  
En él se analizan conceptos fundamentales como el papel del alfabeto, la generación de patrones por autómatas celulares, la homeostasis en sistemas basados en lenguaje, la relación entre lenguaje máquina y ensamblador, y la detección de tokens en código C.  
Finalmente, se diseñan varios AFD sobre diferentes alfabetos y condiciones, incluyendo el que acepta cadenas donde cada grupo de ‘a’ sea seguido por al menos una ‘b’.

---

## Respuestas teóricas

### 1️⃣
El papel que cumple el alfabeto en un lenguaje formal es ser el conjunto de letras o símbolos con los que se forman las palabras o expresiones que pertenecen a ese lenguaje. En el leguaje autómata basicamente es un fitro que determina si la palabra pasa o no, ¿Como determina eso?, si la palabra pertecence al lenguaje. 

### 2️⃣  
Sí, un autómata celular puede crear patrones muy ordenados como caóticos. A veces forma figuras ordenadas y repetitivas, y otras veces genera cosas totalmente desordenadas o caóticas. Todo depende de las reglas que siga para cambiar cada parte del sistema. 

### 3️⃣  
Un sistema puede mantener su estado de homeostasis si logra adaptarse a los cambios. O sea, si nota que algo esta surgiendo mal o diferente a lo esperado, y ajusta su forma de actuar para seguir funcionando bien. 

---

### Punto 4️⃣  

El lenguaje de máquina es el lenguaje de programación de más bajo nivel, con instrucciones binarias por lo que las computadoras lo ejecutan al instante, sin embargo aunque es tan  eficiente es demasiado complicado para un ser humano. Por esto, el lenguaje ensamblador es vital, pues traduce el codigo hecho por un humano a código de máquina, lo que lo hace sumamente eficiente.

---

### Punto 5️⃣  

**Token:** Es la unidad mas pequeña con un significado dentro de un programa.  

**Tokens detectados:**  

```
int -> Tipo de dato, entero  
Suma -> Nombre de la variable  
= -> Operador de asignación  
a -> Variable  
+ -> Operador aritmético de suma  
b -> Variable  
* -> Operador aritmético de multiplicación  
2 -> Constante entero  
; -> Separador
```

---

## 🧩 Punto 6 al 9 — Autómatas Finitos Deterministas (AFD)

Los puntos del taller incluyen la construcción de varios autómatas deterministas (AFD) sobre diferentes alfabetos y condiciones.  
Cada uno debe definirse formalmente mediante su **5-tupla (Q, Σ, δ, q₀, F)**, validarse en **código Python**, y representarse gráficamente mediante un **diagrama de transición**.

---

### ✅ **Punto final (9): AFD solicitado**

**Enunciado:**  
Diseña un AFD sobre el alfabeto Σ = {a, b} que acepte todas las cadenas donde cada grupo de ‘a’ sea seguido por al menos una ‘b’.

**Descripción de la solución (resumen):**
- **Alfabeto:** Σ = {a, b}  
- **Lenguaje aceptado:** Todas las cadenas donde después de cada grupo de ‘a’ debe venir **al menos una ‘b’**.  
  Ejemplos aceptados: `ab`, `aab`, `abba`, `bab`, `bbabb`  
  Ejemplos no aceptados: `a`, `aa`, `aba`, `baaab`  

**Idea general del autómata:**  
- Se inicia en un estado inicial `q0`.  
- Si se lee una `a`, se pasa a un estado `q1` que indica “esperando al menos una b”.  
- Si en `q1` llega una `b`, se regresa a `q0` (porque ya se cumplió la condición).  
- Si llega otra `a` sin antes una `b`, se rechaza.  
- El estado de aceptación es aquel en el que no hay ninguna ‘a’ pendiente sin ‘b’.

**5-tupla:**
```
Q = {q0, q1, q2}
Σ = {a, b}
q0 = estado inicial
F = {q0}
δ(q0, a) = q1
δ(q0, b) = q0
δ(q1, b) = q0
δ(q1, a) = q2 (rechazo)
δ(q2, a) = q2
δ(q2, b) = q2
```

**Estado de aceptación:** q0  
**Estado de rechazo:** q2  

---

📁 **Estructura recomendada del proyecto**
```
📦 TALLER_LENGUAJE
 ┣ 📜 README.md
 ┣ 📜 afd_ab_par.py     ← Código Python para validar el AFD del punto 9
 ┣ 📜 diagrama_AFD.png  ← Diagrama de transición visual
 ┗ 📄 TALLER LENGUAJE.pdf ← Archivo base con instrucciones originales
```
