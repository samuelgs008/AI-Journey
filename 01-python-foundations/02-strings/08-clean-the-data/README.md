# 08 - Clean the Data

Real data is messy: extra spaces, symbols, different formats. Before you can calculate anything, you have to **clean** it. This is a big part of the work in data analysis and automation.

Here you learn to cut a line into **pieces** with `.split()`, and to clean each piece with `.strip()`, `.removeprefix()` and the `.replace()` from exercise 07.

A Brazilian store exported its prices on one line, like `R$ 1.250,50; R$ 3,00`. In Brazil, the dot separates the thousands and the comma separates the decimals, but Python only understands `1250.50`. Read the prices, clean them and show them in the international format, with the total.

## Input

A single line with 1 to 100 prices, separated by `;`. Each price is `R$`, maybe some spaces, then the value with `.` for thousands and `,` for decimals. There may be spaces around each `;`.

## Output

Print each price in the international format, one per line: a comma separating the thousands and 2 decimal places. Then print `TOTAL = X`, in the same format.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
R$ 1.250,50;  R$ 3,00 ;R$ 99,90
</pre></td>
<td><pre>
1,250.50
3.00
99.90
TOTAL = 1,353.40
</pre></td>
</tr>
<tr>
<td><pre>
R$ 1.000.000,00
</pre></td>
<td><pre>
1,000,000.00
TOTAL = 1,000,000.00
</pre></td>
</tr>
<tr>
<td><pre>
R$0,50; R$   2,25
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

1. Try `print("4;9;2".split(";"))`. The result, `['4', '9', '2']`, is a **list** of strings. You'll study lists in Level 03. For now, all you need is that you can go through it with `for`.
2. With an argument, `.split()` cuts exactly there, so the pieces keep their spaces: `" R$ 3,00 "`. Without an argument, `.split()` cuts at **any amount** of spaces and ignores the spaces at the ends. `"a,b,c".split(",")` is how CSV files are read (Level 06).
3. `.strip()` removes the spaces from both ends: `"  hi  ".strip()` gives `"hi"`. `.lstrip()` cleans only the left side, and `.rstrip()` only the right.
4. `.removeprefix("R$")` removes exactly that start, and only if it's there. `.removesuffix()` does the same at the end.
5. Methods can be **chained**: `s.strip().replace("a", "")`. Each one works on the result of the one before it. **Order matters!** If you turn every `,` into `.` first, how will you know which dots to remove?
6. The pieces are still **text**: `"3.00" + "2.25"` gives `"3.002.25"`. Convert each piece before you add it.
7. `f"{1234.5:,.2f}"` gives `"1,234.50"`: the comma separates the thousands. You'll see much more of this in exercise 11.
8. The most famous trap of `.strip()`: it removes **characters**, not words. Try `"test.txt".rstrip(".txt")`. Surprised? It receives a **set of characters** (here `.`, `t` and `x`) and keeps removing while the last character is one of them. That's why `.removeprefix()` and `.removesuffix()` exist.
9. Spaces you can't see are a classic bug. `print(f"{piece!r}")` shows the string with quotes around it, so hidden spaces appear: `'  R$ 3,00 '`.
10. Bonus: try `print(0.1 + 0.2)`. Decimal numbers (floats) are not exact, in Python and in almost every language, and `:.2f` hides that by rounding. That's fine for printing, but programs that handle real money use `Decimal` (you'll be able to import it from Level 05 on).

</details>

## ⚡ Challenge

Here you learn `.join()`, the opposite of `.split()`: it glues pieces together, with a separator between them. And you finally understand the recipe `a, b, c = map(int, input().split())` from Level 01, exercise 05.

Rules: no `for`, and at most **3 lines** of code.

### Input

The same as the main problem: one line of prices separated by `;`.

### Output

Print the whole sum on one line: each price as a plain number with 2 decimal places (no thousands separator), separated by ` + `, then ` = ` and the total.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
R$ 1.250,50;  R$ 3,00 ;R$ 99,90
</pre></td>
<td><pre>
1250.50 + 3.00 + 99.90 = 1353.40
</pre></td>
</tr>
<tr>
<td><pre>
R$ 1.000.000,00
</pre></td>
<td><pre>
1000000.00 = 1000000.00
</pre></td>
</tr>
<tr>
<td><pre>
R$0,50; R$   2,25
</pre></td>
<td><pre>
0.50 + 2.25 = 2.75
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Without a `for`, you can't clean the pieces one by one. But you can clean the **whole line** before you split it. Which characters have to go? Which one becomes a `.`?
2. `"-".join(["a", "b", "c"])` gives `"a-b-c"`. The separator comes first, then the pieces. `.join()` only accepts strings: good news, the pieces from `.split()` are already strings!
3. `map(float, pieces)` applies `float` to each piece, and `sum()` adds up a sequence of numbers.
4. After you solve it, read the recipe again: `.split()` gives the pieces, `map(int, pieces)` applies `int` to each one, and `a, b, c = ...` spreads three values into three variables.
5. Why `.join()` and not `+=` in a loop? With thousands of pieces, `+=` creates a new string on every turn (immutability!), while `.join()` builds it only once.

</details>
