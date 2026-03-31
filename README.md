# Exam - Python Common Core

Practice exercises for the **Milestone 3** exam at 42. 
Each folder contains the subject and a Python solution.

---

## Structure

```
42_Exam_Rank03/
├── atoi/
│   ├── atoi.py
│   └── subject.md
├── brackets/
│   ├── brackets.py
│   └── subject.md
├── convert_base/
│   ├── conver_base.py
│   └── conver_base.md
├── mirror_matrix/
│   ├── mirror_matrix.py
│   └── subject.md
└── sorted/
    └── sorted.py
    └── subject.md

```

---

## Exercises

### `brackets`
Validates whether all brackets in a string are correctly closed and nested.  
Supports `()`, `[]` and `{}`. Non-bracket characters are ignored.
```
brackets("([{}])")  → True
brackets("(]")      → False
```

---

### `atoi`
Converts a string to an integer without using `int()`.  
Handles leading whitespace, optional sign, and stops at the first non-digit character.
```
atoi("  -42abc")  → -42
atoi("+123")      → 123
```

---

### `convert_base`
Converts a number represented as a string from one base to another.
```
convert_base("ff", 16, 2)  → "11111111"
convert_base("10", 2, 10)  → "2"
```

---

### `mirror_matrix`
Returns a new 2D list mirrored horizontally (each row reversed).  
The original matrix is never modified.
```
[[1,2,3],    →    [[3,2,1],
 [4,5,6],          [6,5,4],
 [7,8,9]]          [9,8,7]]
```

---

### `sorted`
Sorting lists of strings, tuples, or objects using `sorted()` with `key=lambda`.  
Covers single criteria, reverse order, and multi-criteria sorting via tuples.
```python
sorted(["banana", "kiwi", "fig"], key=lambda x: len(x))
→ ["fig", "kiwi", "banana"]
```

---

## Usage

```bash
git clone https://github.com/<your-username>/42_Exam_Rank03.git
cd 42_Exam_Rank03
python3 <exercise>/<exercise>.py
```

---

## About

These are common Python exam exercises from the **new Common Core** curriculum at 42 Madrid.  
Similar problems can be found on [LeetCode](https://leetcode.com/) and other coding platforms.

---

*42 Madrid — Common Core · Python · Milestone 3*