# Quinemaker
A program that makes any program print itself at the end of execution

Basic idea was inspired by the shortest Python 3 Quine:
```py
a='a=%r;print(a%%a)';print(a%a)
```

Wanted to challenge myself by using `.replace` instead for universality between languages. Two challenges were dealing with quotes and having to account for potentially replacing arguments to the replace statement itself. These were both solved by making use of the `chr` function.

The proof of concept is located in quinemaker_poc.py (replace `a = 1` with whatever code you wish to print in the beginning).
