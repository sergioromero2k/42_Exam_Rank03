# Brackets
---

Write a function brackets(s) that takes a string as argument and returns True if all the brackets in the string are correctly closed and nested, False otherwise. Valid bracket pairs are (), [] and {}. Non-bracket characters must be ignored.

```
brackets("()")        → True
brackets("([{}])")    → True
brackets("(]")        → False
brackets("([)")       → False
brackets("a(b[c]d)")  → True
```