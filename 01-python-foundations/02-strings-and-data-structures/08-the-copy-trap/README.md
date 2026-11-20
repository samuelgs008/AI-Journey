# 08 - The Copy Trap

This exercise is built to make you fall into the most famous Python bug: **changing one list also changes another**. Fall into it, understand why, then fix it. Here you also meet **lists of lists**, which you use for grids and tables.

## Input

The first line has the grid size: **H** rows and **W** columns (1 ≤ H, W ≤ 20). The second line has **N**, the number of cells to paint. Then come N lines, each with a row and a column (both counting from 1).

## Output

Create a grid of H × W cells, all `.`, and paint the given cells with `#`. Then create a **mirror** of the grid: a copy where each row is reversed (left becomes right).

Print three grids, separated by a line with `---`:

1. the painted grid
2. the mirror
3. the painted grid **again**, which must be unchanged

Each row is printed as one string, without spaces.

Rules: the mirror must be a separate grid. Make a copy of the grid and reverse the rows of the **copy** with `.reverse()`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3 5
4
1 1
2 2
2 5
3 3
</pre></td>
<td><pre>
#....
.#..#
..#..
---
....#
#..#.
..#..
---
#....
.#..#
..#..
</pre></td>
</tr>
<tr>
<td><pre>
2 3
1
1 3
</pre></td>
<td><pre>
..#
...
---
#..
...
---
..#
...
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Start with the "obvious" grid: `grid = [["."] * W] * H`. Paint one cell and print it. What happened?
2. A variable doesn't hold a list. It holds an **arrow** pointing to a list. `[row] * H` makes H arrows to the **same** row. Check it with `grid[0] is grid[1]`.
3. The same happens with `b = a`: there is still only one list, now with two names. `b = a.copy()` or `b = a[:]` creates a new list.
4. To build H **different** rows, create a new row inside a loop: `["."] * W` runs again on each pass.
5. Second trap: `mirror = grid.copy()` makes a new **outer** list, but the rows inside are still the same rows! It's a **shallow** copy. Reverse a row of the mirror and look at the grid.
6. For a list of lists, copy each row too. That's a **deep** copy. Later you'll meet `copy.deepcopy()`, which does it for you.
7. `"".join(row)` turns `["#", ".", "."]` into `"#.."`.
8. Strings never have this problem, because they're immutable. Nobody can change a string through another name.

</details>
