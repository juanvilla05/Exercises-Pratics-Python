# 🌍 Explorando el Alcance de las Variables Globales en Python 🐍

Este conjunto de ejercicios tiene como finalidad principal comprender a fondo el concepto 🧠 y el comportamiento de las **variables globales** en el lenguaje de programación Python. A través de ejemplos prácticos y sencillos ✨

[Aquí encontraras el README en ingles](https://github.com/juanvilla05/Exercises-Pratics-Python/blob/2bbb02ff2251717eebcf836afd76137b31d9b02c/README_English.md)

## 🤔 ¿Qué Aprenderemos?

Al completar estos ejercicios, podrás:

* **↔️ Distinguir claramente entre variables globales 🌐 y variables locales 🏘️** en Python.
* **🔑 Comprender cómo acceder al valor de una variable global** desde cualquier punto del programa 📍, incluyendo el interior de las funciones.
* **✍️ Identificar la necesidad y el uso de la palabra clave `global`** para modificar el valor de una variable global dentro del cuerpo de una función.
* **🔭 Internalizar el concepto de "alcance" (scope)** de las variables en Python y cómo influye en su accesibilidad y modificación.
* **💡 Reflexionar sobre las implicaciones del uso de variables globales** en la organización 📚 y mantenibilidad 🛠️ del código.

## ⚙️ Casos de Uso

* **⚙️ Configuración global:** Almacenar parámetros de configuración que deben ser accesibles en toda la aplicación (por ejemplo, rutas de archivos 📂, claves de API 🔑).
* **🔢 Contadores o acumuladores:** Mantener un registro de eventos o un total que se actualiza desde diferentes partes del programa.
* **🚦 Variables de estado:** Señalar un estado general de la aplicación (por ejemplo, si una conexión a una base de datos 💾 está activa).
* **📌 Constantes:** Definir valores que no deberían cambiar durante la ejecución del programa 🚫 y que son utilizados en múltiples lugares.

## 📤 Ejemplo de Datos de Entrada y Salida 📥

**Ejemplo:**

**Entrada:**

```python
MENSAJE_GLOBAL = "¡Saludos globales!" 👋

def funcion_saludo():
    print(MENSAJE_GLOBAL)

````

**Salida (Consola):**

```
¡Saludos globales!

```

## 🧱 Estructuras Generales Mayormente Implementadas

En el desarrollo de estos ejercicios, se han implementado principalmente las siguientes estructuras fundamentales de Python:

  * **🏷️ Variables:** Para almacenar los datos, tanto a nivel global como local.
  * **🧩 Funciones (`def`):** Para definir bloques de código reutilizables y demostrar la diferencia en el alcance de las variables.
  * **📢 Impresión (`print()`):** Para mostrar los valores de las variables y observar los resultados de las operaciones.
  * **➡️ Asignación (`=`):** Para dar valores iniciales y modificar el contenido de las variables.
  * **🔑 La palabra clave `global`:** Para indicar explícitamente la intención de modificar una variable global dentro de una función.

## ⬇️ Guía para Clonar este Repositorio (si aplica) 📤

Si estos ejercicios estuvieran alojados en un repositorio (por ejemplo, en GitHub 🐙), podrías clonarlos utilizando el siguiente comando en tu terminal 💻:

```bash
git clone <https://github.com/juanvilla05/Exercises-Pratics-Python.git>
```

Reemplaza `<https://github.com/juanvilla05/Exercises-Pratics-Python.git>` con la dirección web del repositorio donde se encuentren los ejercicios. Una vez clonado, podrás navegar a la carpeta del proyecto 📂 y ejecutar los archivos `.py` con un intérprete de Python 🐍.

¡Esperamos que estos ejercicios te sean de gran utilidad 👍
