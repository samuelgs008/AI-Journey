# 13 - Receipt

f-strings can do much more than `{x:.2f}`. After the `:` comes the **format spec**: width, alignment, separators and precision. With it, you can line up columns like a real receipt.

Read some products and their prices, and print a receipt.

## Input

The first line contains an integer **N** (1 ≤ N ≤ 20). Then come N lines, each with a product name (one word, at most 12 characters) and its price (0 < price < 10000), separated by a space.

## Output

- One line per product: the name aligned to the **left** in a space of 15 characters, then the price aligned to the **right** in a space of 15 characters, with 2 decimal places and a comma separating the thousands.
- A line with 30 dashes.
- The total, in the same format as the products, with the name `TOTAL`.

Every line has exactly 30 characters.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
Coffee 4.5
Sandwich 12
Notebook 1299.9
</pre></td>
<td><pre>
Coffee                    4.50
Sandwich                 12.00
Notebook              1,299.90
------------------------------
TOTAL                 1,316.40
</pre></td>
</tr>
<tr>
<td><pre>
1
Gum 0.99
</pre></td>
<td><pre>
Gum                       0.99
------------------------------
TOTAL                     0.99
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `f"{'abc':>6}"` gives `"   abc"`: width 6, aligned to the right. `<` aligns to the left and `^` centers.
2. `f"{1234.5:,.2f}"` gives `"1,234.50"`: the comma separates the thousands.
3. All together, in this order: alignment, width, separator, precision. Like `f"{x:>15,.2f}"`.
4. The name and the price come on the same line: `name, price = input().split()`. Then convert the price.
5. Bonus: try `print(0.1 + 0.2)`. Decimal numbers (floats) are not exact, in Python and in almost every language, and `:.2f` hides that by rounding. That's fine for printing, but programs that handle real money use `Decimal` (you'll be able to import it from Level 05 on).

</details>

## ⚡ Challenge

Here you learn to fill the empty space with any character, to choose the width **while the program runs**, and to center text.

Rules: don't count the `=` of the header yourself. Let the format spec (or a string method) do it.

### Input

The first line contains **N** (1 ≤ N ≤ 20) and the receipt width **W** (22 ≤ W ≤ 60), separated by a space. Then come the N products, like in the main problem, but with names of at most 10 characters.

### Output

- A header: the word ` RECEIPT ` (with one space on each side) centered in W characters, with `=` filling the rest. When the `=` can't be split evenly, the extra one goes on the right.
- One line per product and one for `TOTAL`, each with exactly W characters: the name at the left and the price at the right, formatted like in the main problem.
- Between the products and the total, a line with W dashes.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3 30
Coffee 4.5
Sandwich 12
Notebook 1299.9
</pre></td>
<td><pre>
========== RECEIPT ===========
Coffee                    4.50
Sandwich                 12.00
Notebook              1,299.90
------------------------------
TOTAL                 1,316.40
</pre></td>
</tr>
<tr>
<td><pre>
2 22
Tea 2.5
Cake 10
</pre></td>
<td><pre>
====== RECEIPT =======
Tea               2.50
Cake             10.00
----------------------
TOTAL            12.50
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Any character can fill the empty space. Put it before the alignment: `f"{'hi':*^10}"` gives `"****hi****"`.
2. The width can come from a variable, with braces inside the braces: `f"{'hi':>{w}}"`.
3. Each line must have exactly W characters. If the name takes `len(name)`, how much space is left for the price?
4. Strings also have methods for this: `.center()`, `.ljust()` and `.rjust()`. Try `"hi".center(10, "*")`. And `.zfill()`: `"42".zfill(5)` gives `"00042"`.
5. Bonus: in older code you'll find `"%.2f" % x` and `"{:.2f}".format(x)`. They do the same as `f"{x:.2f}"`, with the same format spec. Now you can read them.
6. Bonus: the format spec has more types you'll meet later: `f"{0.00012:.1e}"` gives `1.2e-04` (scientific notation, everywhere in Machine Learning), `f"{5:+}"` gives `+5` (always show the sign) and `f"{10:b}"` gives `1010` (binary, in Level 07).

</details>
