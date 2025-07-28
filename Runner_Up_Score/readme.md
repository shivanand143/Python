# 📘 Understanding Python List Comprehensions

## 🧠 What is a List Comprehension?

A **list comprehension** is a short and elegant way to create lists in Python.
Instead of using multiple lines with loops, you can use a single line of code to:

* Loop through elements
* Apply a condition (optional)
* Create and return a new list

---

## 🔄 Syntax

```python
[expression for item in iterable if condition]
```

* **expression**: the value to store in the new list
* **item**: the current value from the iterable (like a list)
* **condition**: (optional) a filter to include only specific items

---

## 🔍 Example Breakdown

### Code:

```python
filtered_scores = [score for score in scores if score != max_score]
```

### Explanation:

* Loop through each `score` in the `scores` list
* Check if `score` is **not equal** to `max_score`
* If yes, add it to the `filtered_scores` list

This removes the highest score(s) and keeps the rest.

### Equivalent Regular Loop:

```python
filtered_scores = []
for score in scores:
    if score != max_score:
        filtered_scores.append(score)
```

---

## 💡 Real-World Use Cases

1. **Filter data**:

```python
data = [1, 2, 0, -1, 5]
positive = [x for x in data if x > 0]  # [1, 2, 5]
```

2. **Transform values**:

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]  # [1, 4, 9]
```

3. **Strings**:

```python
names = ["John", "Li", "Maya"]
short_names = [name for name in names if len(name) < 4]  # ["Li"]
```

4. **Nested loops (advanced)**:

```python
pairs = [(i, j) for i in range(2) for j in range(2)]
# [(0, 0), (0, 1), (1, 0), (1, 1)]
```

---

## ✅ Benefits of Using List Comprehension

| Advantage        | Why It Matters                              |
| ---------------- | ------------------------------------------- |
| Cleaner Code     | Reduces 3-4 lines into 1                    |
| Faster Execution | Internally optimized in Python              |
| Readable         | Becomes intuitive with little practice      |
| Pythonic         | Preferred style in professional Python code |

---

## 🎯 Quick Practice

### Task:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]
```

Try modifying this to get odd numbers or squares!

---

## 📆 Summary

* List comprehensions help make your Python code shorter and cleaner.
* They are useful for **filtering**, **transforming**, and **generating** new lists.
* Once you get used to them, they will save you time and make your code more elegant.
