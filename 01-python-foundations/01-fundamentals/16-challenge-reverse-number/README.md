# 16 - 🏆 Final Challenge: Reverse Number

The final challenge of the Fundamentals! Read a number and reverse its digits, and also add them up.

⚠️ **No text allowed**: don't convert the number to `str`. Use only math, with `//` and `%`.

## Input

The input contains an integer **N** (0 ≤ N ≤ 1000000000).

## Output

Print two lines: `REVERSED = X` and `DIGIT SUM = Y`. The reversed number has no leading zeros: 1200 reversed is 21.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
1234
</pre></td>
<td><pre>
REVERSED = 4321
DIGIT SUM = 10
</pre></td>
</tr>
<tr>
<td><pre>
1200
</pre></td>
<td><pre>
REVERSED = 21
DIGIT SUM = 3
</pre></td>
</tr>
<tr>
<td><pre>
7
</pre></td>
<td><pre>
REVERSED = 7
DIGIT SUM = 7
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `1234 % 10` gives `4`, the last digit. `1234 // 10` gives `123`, the number without it.
2. Repeat those two steps while there are digits left. When does the number reach 0?
3. To put a digit at the end of another number: `43 * 10 + 2` gives `432`.

</details>

## My algorithm

How I planned the solution in [Excalidraw](https://excalidraw.com/) before writing the code:

![Flowchart of the reverse number algorithm](Algorithm.png)

## ⚡ Challenge

A number is a **palindrome** when it reads the same both ways, like 12321. Here you learn that some loops **destroy** the value they use, and you hunt for **edge cases**.

Rules: still no text, only math.

### Input

An integer **N** (0 ≤ N ≤ 1000000000).

### Output

Print two lines: `DIGITS = X` (how many digits N has) and `PALINDROME` or `NOT PALINDROME`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
12321
</pre></td>
<td><pre>
DIGITS = 5
PALINDROME
</pre></td>
</tr>
<tr>
<td><pre>
1200
</pre></td>
<td><pre>
DIGITS = 4
NOT PALINDROME
</pre></td>
</tr>
<tr>
<td><pre>
0
</pre></td>
<td><pre>
DIGITS = 1
PALINDROME
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. After your loop, N became 0. How will you compare it with the reversed number? Save a copy **before** the loop.
2. Look at sample 3: 0 has **1** digit. How many does your loop count?
3. Bonus, after you solve it: in Level 02 you'll see that with text this becomes one line, `s == s[::-1]`. Try it in the terminal with `s = "12321"`.

</details>
