# 📘 List Comprehensions – 3D Grid Theory Explanation

## 🧠 Objective

You are given 4 integers: `x`, `y`, `z`, and `n`.
You need to generate a list of all possible 3D coordinates `[i, j, k]` such that:

* `0 ≤ i ≤ x`
* `0 ≤ j ≤ y`
* `0 ≤ k ≤ z`
* But **exclude** those combinations where `i + j + k == n`

---

## 🔷 What is a 3D Grid?

A 3D grid is a set of points in space, like a cube.
Each point has 3 components:

* `i` → position along X-axis
* `j` → position along Y-axis
* `k` → position along Z-axis

If:

```
x = 1  
y = 1  
z = 1
```

Then valid ranges are:

```
i ∈ [0, 1], j ∈ [0, 1], k ∈ [0, 1]
```

All combinations:

```
[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
```

---

## 🧹 Filtering Condition

You need to **exclude** any coordinate where:

```
i + j + k == n
```

So if `n = 2`, remove combinations like:

* \[0, 1, 1]
* \[1, 0, 1]
* \[1, 1, 0]

Remaining:

```
[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]
```

---

## 📟 What is List Comprehension?

List Comprehension is a compact syntax in Python for:

* Generating sequences using loops
* Applying conditions
* Creating lists in one line

**Syntax:**

```python
[expression for item in iterable if condition]
```

In this problem, you use **three nested loops**:

```python
[i, j, k for i in range(x+1) for j in range(y+1) for k in range(z+1)]
```

Add the condition to filter:

```python
if i + j + k != n
```

---

## 📙 Lexicographic Order

Python's nested `for` loops (used in the comprehension) automatically generate combinations in **lexicographic order**, which is:

* Like dictionary order
* Example:

  ```
  [0, 0, 0]
  [0, 0, 1]
  [0, 1, 0]
  [1, 0, 0]
  ```

So no need to sort the result manually.

---

## ✅ Key Concepts Summary

| Concept             | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| 3D Grid             | All (i, j, k) combinations for a cube of size (x+1, y+1, z+1) |
| List Comprehension  | Short syntax to build lists using loops and conditions        |
| Filtering Condition | `if i + j + k != n` filters out unwanted results              |
| Lexicographic Order | Python naturally preserves it via nested loops                |

---

## 🎯 Goal

Master:

* Looping in 3 dimensions
* Writing efficient and readable Python code
* Using list comprehensions with conditions
* Understanding filtering and combination generation in Python

---
