# 09 - Sum of a Line

Back in Level 01, exercise 05, you used `a, b, c = map(int, input().split())` as a recipe. Now you'll understand it. It all starts with `.split()`, which cuts a string into **pieces**.

Read a line with several integers and print their sum. You don't know how many numbers will come.

## Input

The input contains a single line with 1 to 100 integers, separated by one or more spaces.

## Output

Print `SUM = X`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4 9 2
</pre></td>
<td><pre>
SUM = 15
</pre></td>
</tr>
<tr>
<td><pre>
10
</pre></td>
<td><pre>
SUM = 10
</pre></td>
</tr>
<tr>
<td><pre>
-3   7  100
</pre></td>
<td><pre>
SUM = 104
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Try `print("4 9 2".split())`. The result, `['4', '9', '2']`, is a **list** of strings. You'll study lists in Level 03. For now, all you need is that you can go through it with `for`.
2. The pieces are still **text**: `"4" + "9"` gives `"49"`. Convert each piece before you add it.
3. Try sample 3 with `.split(" ")` and then with `.split()`. Where do those `''` come from? Without an argument, `.split()` cuts at **any amount** of spaces and ignores the spaces at the ends. With an argument, it cuts exactly there: `"a,b,c".split(",")` is how CSV files are read (Level 06).
4. After you solve it, read the recipe again: `.split()` gives the pieces, `map(int, pieces)` applies `int` to each one, and `a, b, c = ...` spreads three values into three variables.

</details>

## ⚡ Challenge

Here you learn `.join()`, the opposite of `.split()`: it glues pieces together, with a separator between them.

Rules: no `for`, and at most **3 lines** of code.

### Input

The same as the main problem: a line with 1 to 100 integers.

### Output

Print the whole sum: the numbers exactly as they were typed, separated by ` + `, then ` = ` and the result.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4 9 2
</pre></td>
<td><pre>
4 + 9 + 2 = 15
</pre></td>
</tr>
<tr>
<td><pre>
10
</pre></td>
<td><pre>
10 = 10
</pre></td>
</tr>
<tr>
<td><pre>
-3   7  100
</pre></td>
<td><pre>
-3 + 7 + 100 = 104
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. `"-".join(["a", "b", "c"])` gives `"a-b-c"`. The separator comes first, then the pieces.
2. `.join()` only accepts strings. Good news: the pieces from `.split()` are already strings!
3. `sum()` adds up a sequence of numbers. Where can you get a sequence of numbers? Look at hint 4 of the main problem.
4. Why `.join()` and not `+=` in a loop? With thousands of pieces, `+=` creates a new string on every turn (immutability!), while `.join()` builds it only once.

</details>
