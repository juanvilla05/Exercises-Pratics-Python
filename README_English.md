# 🌍 Exploring the Scope of Global Variables in Python 🐍

This set of exercises primarily aims to thoroughly understand the concept 🧠 and behavior of **global variables** in the Python programming language. Through practical and simple examples ✨

[Here you will find the readme in Spanish.](https://github.com/juanvilla05/Exercises-Pratics-Python/blob/038748c4fa1a3906a4c6cb46abbaba7ad57d0805/README.md)

## 🤔 What Will We Learn?

By completing these exercises, you will be able to:

* **↔️ Clearly distinguish between global 🌐 and local 🏘️ variables** in Python.
* **🔑 Understand how to access the value of a global variable** from any point in the program 📍, including inside functions.
* **✍️ Identify the necessity and use of the `global` keyword** to modify the value of a global variable within the body of a function.
* **🔭 Internalize the concept of variable "scope"** in Python and how it influences their accessibility and modification.
* **💡 Reflect on the implications of using global variables** on code organization 📚 and maintainability 🛠️.

## ⚙️ Use Cases

* **⚙️ Global configuration:** Storing configuration parameters that should be accessible throughout the application (e.g., file paths 📂, API keys 🔑).
* **🔢 Counters or accumulators:** Maintaining a record of events or a total that is updated from different parts of the program.
* **🚦 State variables:** Signaling a general state of the application (e.g., whether a database connection 💾 is active).
* **📌 Constants:** Defining values that should not change during program execution 🚫 and are used in multiple places.

## 📤 Input and Output Data Example 📥

**Example:**

**Input:**

```python
GLOBAL_MESSAGE = "¡Global greetings!" 👋

def greeting_function():
    print(GLOBAL_MESSAGE)
```

**Output (Console):**

```
¡Global greetings!
```

## 🧱 General Structures Mostly Implemented

In the development of these exercises, the following fundamental Python structures have been mainly implemented:

* **🏷️ Variables:** To store data, both globally and locally.
* **🧩 Functions (`def`):** To define reusable code blocks and demonstrate the difference in variable scope.
* **📢 Printing (`print()`):** To display the values of variables and observe the results of operations.
* **➡️ Assignment (`=`):** To give initial values and modify the content of variables.
* **🔑 The `global` keyword:** To explicitly indicate the intention to modify a global variable within a function.

## ⬇️ Guide to Clone this Repository (if applicable) 📤

If these exercises were hosted in a repository (for example, on GitHub 🐙), you could clone them using the following command in your terminal 💻:

```bash
git clone [https://github.com/juanvilla05/Exercises-Pratics-Python.git](https://github.com/juanvilla05/Exercises-Pratics-Python.git)
```

Replace `<https://github.com/juanvilla05/Exercises-Pratics-Python.git>` with the web address of the repository where the exercises are located. Once cloned, you can navigate to the project folder 📂 and run the `.py` files with a Python interpreter 🐍.

We hope these exercises are very useful 👍
```
