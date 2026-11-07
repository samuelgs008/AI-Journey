# 08 - Clean the Data

Real data is messy: extra spaces, symbols, different formats. Before you can calculate anything, you have to **clean** it. This is a big part of the work in data analysis and automation.

A Brazilian store exported its prices like `R$ 1.250,50`. In Brazil, the dot separates the thousands and the comma separates the decimals, but Python only understands `1250.50`. Read the prices, clean them and show the total.

## Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come N lines, each with a price in the Brazilian format: `R$`, maybe some spaces, then the value with `.` for thousands and `,` for decimals. Some lines start with spaces.

## Output

Print each price as a normal number with 2 decimal places, one per line. Then print `TOTAL = X`, also with 2 decimal places.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
R$ 1.250,50
  R$ 3,00
R$ 99,90
</pre></td>
<td><pre>
1250.50
3.00
99.90
TOTAL = 1353.40
</pre></td>
</tr>
<tr>
<td><pre>
1
R$ 1.000.000,00
</pre></td>
<td><pre>
1000000.00
TOTAL = 1000000.00
</pre></td>
</tr>
<tr>
<td><pre>
2
R$0,50
R$   2,25
</pre></td>
<td><pre>
0.50
2.25
TOTAL = 2.75
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `.replace(old, new)` swaps every `old` for `new`: `"a-b-c".replace("-", "")` gives `"abc"`. A third argument limits how many swaps happen: `"a-b-c".replace("-", "", 1)` gives `"ab-c"`.
2. Methods can be **chained**: `s.replace("a", "").replace("b", "")`. Each one works on the result of the one before it.
3. **Order matters!** If you turn every `,` into `.` first, how will you know which dots to remove?
4. `.strip()` removes the spaces from both ends: `"  hi  ".strip()` gives `"hi"`. `.lstrip()` cleans only the left side, and `.rstrip()` only the right.

</details>

## ⚡ Challenge

Here you learn the most famous trap of `.strip()`: it removes **characters**, not words. And you meet `.removeprefix()` and `.removesuffix()`, made to remove a whole piece.

Rules: no `if` and no slices.

### Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come N lines, each with a file name. Some names have spaces at the start or at the end.

### Output

For each file, print its name without the spaces around it and without the `.txt` extension. Names that don't end in `.txt` (exactly, in lowercase) only lose the spaces.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4
report.txt
test.txt
notes.md
text.txt
</pre></td>
<td><pre>
report
test
notes.md
text
</pre></td>
</tr>
<tr>
<td><pre>
2
  draft.txt
README.TXT
</pre></td>
<td><pre>
draft
README.TXT
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"test.txt".rstrip(".txt")`. Surprised? `.rstrip()` receives a **set of characters** (here `.`, `t` and `x`) and keeps removing from the right while the last character is one of them.
2. `.removesuffix(".txt")` removes exactly that ending, and only if it's there. `.removeprefix()` does the same at the start.
3. Spaces you can't see are a classic bug. `print(f"{name!r}")` shows the string with quotes around it, so hidden spaces appear: `'  draft.txt'`.

</details>
