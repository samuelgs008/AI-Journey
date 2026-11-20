# 09 - Tic-Tac-Toe Judge

Someone shows you a tic-tac-toe board. Say who won... or if the board is impossible. A grid is a list of lists: rows, columns and diagonals are just different ways of walking through it.

## Input

Three lines with three characters each: `X`, `O` or `.` (empty). X always plays first, and the players take turns.

## Output

One line:

- `INVALID` if the board could never happen in a real game
- `X WINS` or `O WINS` if a player has three in a row (a row, a column or a diagonal)
- `DRAW` if the board is full and nobody won
- `GAME ON` otherwise

When is a board impossible? X plays first, so:

- the number of X's must be equal to the number of O's, or one more
- both players can't win at the same time
- if X won, X must have exactly one more piece than O (the game stops when X wins)
- if O won, both must have the same number of pieces

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
XOX
OXO
OOX
</pre></td>
<td><pre>
INVALID
</pre></td>
</tr>
<tr>
<td><pre>
XXO
OOX
XOX
</pre></td>
<td><pre>
DRAW
</pre></td>
</tr>
<tr>
<td><pre>
XO.
...
...
</pre></td>
<td><pre>
GAME ON
</pre></td>
</tr>
<tr>
<td><pre>
XXX
OOO
...
</pre></td>
<td><pre>
INVALID
</pre></td>
</tr>
<tr>
<td><pre>
XXX
...
OO.
</pre></td>
<td><pre>
X WINS
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `list("XO.")` gives `["X", "O", "."]`. Read three lines and you have a 3 × 3 grid: `board[row][col]`.
2. Count the pieces with a nested loop, like the star triangle in Level 01.
3. Sample 1 has a diagonal of X's, but the count gives it away: 4 X's and 5 O's.
4. Build a list with all 8 lines of the board: 3 rows, 3 columns and 2 diagonals. Column `c` is `[board[0][c], board[1][c], board[2][c]]`. The diagonals use `board[i][i]` and `board[i][2 - i]`.
5. Now "did X win?" is just `["X", "X", "X"] in lines`. Lists can be compared with `==`, so `in` works on them too.
6. The **order** of the checks matters, like in FizzBuzz. Check `INVALID` first, then the winners, then `DRAW`.
7. Make up your own impossible boards and test them. For example: O wins, but X has one more piece.

</details>
