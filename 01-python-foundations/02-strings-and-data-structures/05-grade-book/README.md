# 05 - Grade Book

Turn a line of grades into statistics. Here you meet `min`, `max`, `sum`, and the difference between `sort()` and `sorted()`. That difference causes real bugs.

## Input

One line with N grades (1 ≤ N ≤ 100), integers from 0 to 100, separated by spaces.

## Output

Print, in this order:

```
SORTED: <grades from smallest to largest>
GRADES: <grades in the original order>
COUNT = <how many>
MIN = <smallest>
MAX = <largest>
AVERAGE = <average, 2 decimal places>
MEDIAN = <median, 1 decimal place>
TRIMMED AVERAGE = <average without the highest and lowest, 2 decimal places>
PASSED = <p> of <n> (<percentage, 1 decimal place>%)
```

- The **median** is the middle grade of the sorted list. If N is even, it's the average of the two middle grades.
- The **trimmed average** removes **one** highest and **one** lowest grade, then averages the rest. It needs at least 3 grades. If there are fewer, print `TRIMMED AVERAGE = N/A`.
- A grade **passes** when it's 60 or more.

Notice the order: `SORTED` comes **before** `GRADES`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
70 12 90 60 88 52
</pre></td>
<td><pre>
SORTED: 12 52 60 70 88 90
GRADES: 70 12 90 60 88 52
COUNT = 6
MIN = 12
MAX = 90
AVERAGE = 62.00
MEDIAN = 65.0
TRIMMED AVERAGE = 67.50
PASSED = 4 of 6 (66.7%)
</pre></td>
</tr>
<tr>
<td><pre>
100 35
</pre></td>
<td><pre>
SORTED: 35 100
GRADES: 100 35
COUNT = 2
MIN = 35
MAX = 100
AVERAGE = 67.50
MEDIAN = 67.5
TRIMMED AVERAGE = N/A
PASSED = 1 of 2 (50.0%)
</pre></td>
</tr>
<tr>
<td><pre>
73
</pre></td>
<td><pre>
SORTED: 73
GRADES: 73
COUNT = 1
MIN = 73
MAX = 73
AVERAGE = 73.00
MEDIAN = 73.0
TRIMMED AVERAGE = N/A
PASSED = 1 of 1 (100.0%)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `list(map(int, input().split()))` turns the line into a list of numbers.
2. `grades.sort()` **changes** the list and returns `None`. `sorted(grades)` gives you a **new** sorted list and leaves the original alone. If your `GRADES` line comes out sorted, you know which one you used.
3. `print("SORTED:", *s)` prints the items separated by spaces. It's the `*` from the Level 01 countdown.
4. Middle of a sorted list: `n // 2`. Test it with N = 5 and N = 6 on paper before you code it.
5. Sample 1 shows why the trimmed average exists: one very low grade (12) pulls the normal average down. Judges in sports use this trick.
6. For the trimmed average, `.remove(max(...))` removes one copy of the highest grade. But do it on a **copy** (`grades.copy()`), or you'll destroy the list you still need.
7. `f"{0.6667:.1%}"` gives `66.7%`. The `%` format multiplies by 100 for you.

</details>
