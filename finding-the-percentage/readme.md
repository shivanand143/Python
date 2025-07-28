# Understanding `name, *line = input().split()` in Python

## Overview

This syntax is part of Python's *iterable unpacking* feature. It allows you to split input values into individual variables efficiently, even when the number of values varies.

---

## Syntax Breakdown

```python
name, *line = input().split()
```

### What It Does:

* Reads a line of input.
* Splits the input into parts using `.split()` (default: whitespace).
* Assigns:

  * The **first part** to `name`
  * The **rest** of the parts to `line` as a **list**

---

## Example

Input:

```
Krishna 67 68 69
```

Code:

```python
name, *line = input().split()
```

Result:

```python
name = 'Krishna'
line = ['67', '68', '69']
```

---

## When to Use

This technique is useful when:

* You know the first value is unique (like a name or ID)
* The rest of the values are a sequence (like scores, prices, etc.)

---

## Real-World Use Case: Average Student Marks Problem

### Problem:

Given a list of student names and their scores, store them in a dictionary and then print the average score of a student (given by name) rounded to two decimal places.

### Sample Input:

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

### Sample Output:

```
56.00
```

### Code:

```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(avg))
```

### How the Code Works:

1. `n = int(input())` — Takes the number of students.
2. Initializes an empty dictionary `student_marks`.
3. For each student:

   * Reads input: e.g., `Krishna 67 68 69`
   * Uses `name, *line = input().split()` to separate the name and scores
   * Converts the score strings to float: `map(float, line)`
   * Stores in dictionary: `student_marks['Krishna'] = [67.0, 68.0, 69.0]`
4. Reads the `query_name` to find.
5. Looks up scores: `student_marks[query_name]`
6. Computes average: `sum(...) / len(...)`
7. Prints the result formatted to 2 decimal places.

---

## Notes

* `*` is called the **extended unpacking operator**.
* You can only use it **once per unpacking line**.
* It always collects the remaining values into a **list**.

---

## Summary

* This is a concise way to separate a fixed portion of input from a variable-length list.
* It helps write cleaner and more readable Python code for input processing tasks.
* This is especially powerful in competitive programming and real-world data parsing.


