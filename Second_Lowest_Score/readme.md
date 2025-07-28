# 🎓 Find Students with Second Lowest Score - Python Explained

## 🔎 Problem Statement

Given a list of students with their scores, you need to **find and print the names of all students who have the second lowest score**, in alphabetical order.

---

## 📄 Sample Input

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

## 🔢 Expected Output

```
Berry
Harry
```

---

## 🧮 Concept Explanation

### ✅ Step-by-step Logic:

1. **Store student data**:

   * Read name and score for each student.
   * Store it as a list of lists: `[['Harry', 37.21], ['Berry', 37.21], ...]`

2. **Extract unique scores**:

   * Use list comprehension and `set` to get all unique scores.
   * Then sort them to find the second lowest.

3. **Filter names of students with second lowest score**:

   * Use list comprehension to check each student's score.
   * If the score matches the second lowest, collect the name.

4. **Sort the collected names alphabetically** and print them.

---

## 🔍 Code Concept Highlight

### Line:

```python
names = [student[0] for student in lis if student[1] == second_lowest]
```

### 🧵 Meaning:

* Go through each student in the list.
* If the student's score (`student[1]`) is equal to `second_lowest`,
* Take their name (`student[0]`) and add it to the `names` list.

### 🤔 In Simple Words:

> “Take the names of students whose marks are equal to the second lowest and save them in a new list.”

---

## 🧰 Example:

```python
lis = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
scores = sorted(set([student[1] for student in lis]))  # [37.2, 37.21, 39.0, 41.0]
second_lowest = scores[1]  # 37.21
names = [student[0] for student in lis if student[1] == second_lowest]  # ['Harry', 'Berry']
```

Final output (after sorting `names`):

```
Berry
Harry
```

---

## ✨ Where can I use this?

* Any time you want to **filter data based on a specific condition**.
* Useful in:

  * Rankings
  * Filtering lowest/highest values
  * Student grade reports
  * Leaderboards

---

Let me know if you want a version in Kannada or PDF format!
