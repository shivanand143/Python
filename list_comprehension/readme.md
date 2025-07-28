🧠 Theory Behind the Problem: 3D Grid Generation using List Comprehensions
🔹 Objective:
You're given 3 integers x, y, and z, which define a 3D grid.
You need to generate all possible coordinates (i, j, k) such that:

i goes from 0 to x

j goes from 0 to y

k goes from 0 to z

But you exclude the points where the sum i + j + k == n.

🔸 What is a 3D Grid?
A 3D grid is like a cube made of points, where each point has 3 values:

i → position along X-axis

j → position along Y-axis

k → position along Z-axis

If x = 1, y = 1, z = 1, the grid looks like a small cube of size 2x2x2:

Total possible combinations = (x+1)*(y+1)*(z+1) = 8

🔸 What is a List Comprehension?
A list comprehension in Python is a compact way to:

Loop over values

Apply conditions

Collect results into a list

Syntax:
python
Copy
Edit
[expression for item in range if condition]
For this problem, we use 3 nested loops in one line to simulate all combinations of i, j, k.

🔸 Filtering With a Condition
You don’t want to include points where i + j + k == n.
So we simply add if i + j + k != n to the comprehension.

This is filtering — it ensures only valid points are added to the final list.

🔸 Lexicographic Order
Python’s nested loops automatically generate combinations in lexicographic order (like dictionary order).
For example:

[0, 0, 0]

[0, 0, 1]

[0, 1, 0]

[1, 0, 0]

This is the correct order expected by HackerRank.

✅ Summary
Concept	Explanation
3D Grid	All combinations of (i, j, k) in 3 dimensions
Nested Loops	Used to generate every coordinate
List Comprehension	One-liner way to loop and filter
Filtering	if i + j + k != n skips unwanted points
Lexicographic Order	Automatically preserved by Python’s loop
