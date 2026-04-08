# Python: Variable annotations
**Python** is a dynamically-typed language, which means that variable types are determined as the program is run, when a value gets assigned to them.

Variable annotations help developers to know what type each variable is when reading the code, and also allows for code validators to catch any issues regarding types before the code itself is executed.

## Basic example
Below is the definition of a function that adds two numbers, without annotations:
```py
def add(a, b):
  return a + b
```
Below is the same function with annotations.
```py
def add(a: float, b: float) -> float:
  return a + b
```
In this particular case the types of `a` and `b` and the type of the return value are obvious without annotations. However, in more complex functions, annotations can save a significant amount of time and effort when attempting to understand or debug the code.
