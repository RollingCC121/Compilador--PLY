# La Estructura de un Compilador

Un compilador generalmente consta de varias fases:

1. **Análisis Léxico:** En esta etapa, el código divide los caracteresd e las cadenas de texto en "tokens". Estos tokens representan los elementos básicos del lenguaje, como palabras clave, identificadores, operadores y literales.
2. **Análisis Sintáctico:** Aquí, se definen las reglas del lenguaje, como la procedencia de las operaciones. Verifica si la secuencia de tokens sigue las reglas gramaticales del lenguaje. Se crea un árbol de análisis sintáctico para representar la estructura jerárquica del código.
3. **Análisis Semántico:** Esta fase se encarga de asegurarse de que el código tenga sentido. Se verifican cosas como la asignación correcta de tipos y el uso adecuado de variables.
4. **Generación de Código Intermedio:** Se crea una representación intermedia del código que es más fácil de manipular que el código fuente original y valida que no se encuentren expresiones redundantes.
5. **Generación de Código:** Finalmente, el compilador genera el código de máquina a partir del código intermedio.

# Guia de Ejecución

Este compilador esta divido por modulos, donde cada modulo cumple una de las funciones anteriores; se invocan en el arhivo main.py y se ejecutan para analisaar el archivo texto.txt. Si desea ejecutar el compilador tiene que hacer lo siguiente:

## Paso 1:

Asegúrate de estar en el directorio Compilador--PLY.

## Paso 2:

Activa el entorno virtual con el siguiente comando, dependiendo de tu sistema operativo:

**Windows**

```shell
venv\Scripts\activate
```

**Mac/Linuc**

```shell
source venv\Scripts\activate
```

## Paso 3:

Ejecutar el archivo main.py.

```shell
python main.py
```

# Referencias

https://gist.github.com/dimitrio-m/cf6cde052787ed97164fe6422a5e4cb0#file-readme-md

https://github.com/yetto-tools/compilador_con_ply/tree/main

https://youtu.be/iXArNJWLYes?si=GcZXjKt0SRfZIDX2

chatgpt
