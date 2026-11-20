# 15 - Ranking Table

Build a leaderboard like the ones in games and sales dashboards: positions, ties, percentages and arrows that show who moved up or down. `zip` and `enumerate` make it clean.

## Input

Three lines:

1. the players' names (at most 10 characters each), separated by spaces
2. this week's scores, in the same order as the names
3. last week's scores, in the same order as the names

## Output

Sort the players by score, from highest. When scores are equal, sort by name in alphabetical order.

**Positions with ties:** players with the same score share the same position, and the next position skips. Scores `500 300 300 100` get the positions `1 2 2 4` (like at the Olympics).

**Move:** compare each player's position last week (same rules) with this week:

- `▲n`: moved up `n` positions
- `▼n`: moved down `n` positions
- `=`: same position

Print a header, one row per player and a total row:

```
POS  NAME         SCORE   SHARE  MOVE
```

Each row has: the position right-aligned in 3 characters, 2 spaces, the name left-aligned in 10, the score right-aligned in 8 with a thousands separator, the share of the total score right-aligned in 8 as a percentage with 1 decimal place, 2 spaces, the move. The total row has 5 spaces, `TOTAL` left-aligned in 10 and the total score right-aligned in 8.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
ana bia caio davi eva
12500 8000 12500 3000 8000
9000 15000 4000 3000 10000
</pre></td>
<td><pre>
POS  NAME         SCORE   SHARE  MOVE
  1  ana         12,500   28.4%  ▲2
  1  caio        12,500   28.4%  ▲3
  3  bia          8,000   18.2%  ▼2
  3  eva          8,000   18.2%  ▼1
  5  davi         3,000    6.8%  =
     TOTAL       44,000
</pre></td>
</tr>
<tr>
<td><pre>
solo
7
7
</pre></td>
<td><pre>
POS  NAME         SCORE   SHARE  MOVE
  1  solo             7  100.0%  =
     TOTAL            7
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `zip(names, scores)` pairs the two lists: `("ana", 12500), ("bia", 8000)...`. Try `list(zip(...))` in the terminal to see it.
2. Sorting from the highest score, with ties by name: the tuple trick again, with `(-score, name)`.
3. `enumerate(things, start=1)` gives you `(1, first), (2, second)...`. No more counting by hand.
4. Ties: a player's position is their count in the sorted list, **unless** their score is equal to the previous player's. Then they get the previous player's position.
5. Save the positions in a dictionary `name → position`, once for this week and once for last week. Then the move is just a subtraction. Which order of subtraction makes "moved up" positive?
6. You'll do the ranking twice (this week and last week). Write it for one week, check it, then copy it. In Level 03 you'll learn to write it once as a **function**.
7. `f"{12500:>8,}"` gives `  12,500`, and `f"{0.284:>8.1%}"` gives `   28.4%`. A format can have alignment, width, separator and type all at once.

</details>
