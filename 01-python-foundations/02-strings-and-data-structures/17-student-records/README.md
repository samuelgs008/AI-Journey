# 17 - Student Records

A **list of dictionaries** is the shape of almost all real data: JSON from APIs, rows from databases, records from spreadsheets. Read student records into that shape, then answer questions about them.

## Input

The first line contains **N** (1 ≤ N ≤ 100). Then come N lines in the format `name;class;grades`, where the grades are integers from 0 to 10 separated by commas (at least one).

## Output

1. For each student, in the input order: `Name (Class): average STATUS`, with the average to 2 decimal places. The status is `APPROVED` if the average is 6 or more, otherwise `FAILED`.
2. `BEST = Name (average)`: the student with the highest average (the first one if there's a tie).
3. For each class, in alphabetical order:
   `CLASS X: n students, average a, approved: Name1, Name2`.
   The class average is the average of its students' averages. The approved students are in the input order, or `NONE`.

Rules: first read **everything** into a list of dictionaries, one per student, with the keys `"name"`, `"class"`, `"grades"` (a list of numbers) and `"average"`. Then produce all the output from that list.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
5
Ana;A;7,8,9
Bruno;B;5,6
Carla;A;4,5,6
Davi;B;10,9
Eva;A;6
</pre></td>
<td><pre>
Ana (A): 8.00 APPROVED
Bruno (B): 5.50 FAILED
Carla (A): 5.00 FAILED
Davi (B): 9.50 APPROVED
Eva (A): 6.00 APPROVED
BEST = Davi (9.50)
CLASS A: 3 students, average 6.33, approved: Ana, Eva
CLASS B: 2 students, average 7.50, approved: Davi
</pre></td>
</tr>
<tr>
<td><pre>
2
Zoe;C;3,4
Leo;C;5,6,4
</pre></td>
<td><pre>
Zoe (C): 3.50 FAILED
Leo (C): 5.00 FAILED
BEST = Leo (5.00)
CLASS C: 2 students, average 4.25, approved: NONE
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. One student looks like this: `{"name": "Ana", "class": "A", "grades": [7, 8, 9], "average": 8.0}`. Print your list after reading it. Does it look like JSON?
2. Nested access: `students[0]["grades"][-1]` is the last grade of the first student. Read it left to right.
3. Inside an f-string, use the other kind of quotes for the keys: `f"{s['name']}"`.
4. For the classes, group the students: a dictionary class → list of student dictionaries (exercise 13).
5. `.setdefault(key, [])` returns the list for that key and creates it first if it's missing. So `groups.setdefault(c, []).append(s)` does the whole grouping pattern in one line.
6. Comprehensions from exercise 16 fit well here: `[s["name"] for s in group if s["average"] >= 6]`.
7. This is why the rule says "read everything first": once the data has a good shape, every question becomes a short loop. In Level 05 you'll load this same shape straight from a `.json` file.

</details>
