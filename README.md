# 🧠 TALLER DE LENGUAJE Y AUTÓMATAS FINITOS DETERMINISTAS

## Participantes

- Juan Holguin  
- Sara Leon  
- Samuel Moya  
- Luigi Rincon  
- Uriel Rodriguez  
- Juan Vasquez


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

