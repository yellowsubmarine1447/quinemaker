# Quinemaker
A program that makes any program print itself at the end of execution
`quinemaker.py` is the actual cmdline program
`quinemaker_poc.py` is the proof of concept

Basic idea was inspired by the shortest Python 3 Quine:
```py
a='a=%r;print(a%%a)';print(a%a)
```

Wanted to challenge myself by using `.replace` instead for universality between languages. Two challenges were dealing with quotes and having to account for potentially replacing arguments to the replace statement itself. These were both solved by making use of the `chr` function.

EDIT: Two other issues were discovered: one was the inclusion of triple quotes in the source code itself, and the other was chained replacing (so basically certain characters in the source code would be replaced with stuff that they shouldn't be)). These have been fixed, so hopefully this should work with any synchronous python program.

Note backslashes (for escaping and control characters) aren't handled in the POC, but are in the cmdline program.
