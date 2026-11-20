# 10 - Map Points

Places on a map are pairs of numbers. Pairs that never change are perfect for **tuples**. Here you also see unpacking at its best, and a trick for sorting by several things at once.

## Input

The first line contains **N** (1 ≤ N ≤ 50). Then come N lines in the format `name: x,y`, where x and y are integers (they can be negative). There may be spaces around the name.

## Output

The **distance** of a point is how far a taxi drives from the origin `(0, 0)` on city blocks: `|x| + |y|`.

1. Print all points, sorted by distance from the closest. When the distance is equal, sort by name in alphabetical order. Format: `1. name (x, y) distance d`.
2. `ROUTE = r`: the total taxi distance to start at `(0, 0)`, visit the points **in the input order** and come back to `(0, 0)`. The taxi distance between two points is `|x1 - x2| + |y1 - y2|`.
3. `BOX = (min x, min y) to (max x, max y)`: the smallest rectangle that holds every point.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4
home: 3,4
work : -2,1
gym: 0,-5
bank: 1,1
</pre></td>
<td><pre>
1. bank (1, 1) distance 2
2. work (-2, 1) distance 3
3. gym (0, -5) distance 5
4. home (3, 4) distance 7
ROUTE = 32
BOX = (-2, -5) to (3, 4)
</pre></td>
</tr>
<tr>
<td><pre>
2
zoo: 2,2
art: -1,-3
</pre></td>
<td><pre>
1. art (-1, -3) distance 4
2. zoo (2, 2) distance 4
ROUTE = 16
BOX = (-1, -3) to (2, 2)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `.partition(":")` and then `.partition(",")` take the line apart. Don't forget `.strip()` on the name.
2. Save each point as a tuple `(name, x, y)` in a list. A tuple is like a list that can't change.
3. Unpacking in a loop is very clean: `for name, x, y in points:`.
4. `abs(-5)` is `5`.
5. **The trick:** tuples are compared item by item, like strings are compared letter by letter. `(2, "zoo") > (2, "art")` because the first items are equal, so Python compares the second ones. So if you build tuples `(distance, name, x, y)`, `sorted()` sorts by distance and then by name, for free!
6. `print((3, 4))` prints `(3, 4)`. A tuple inside an f-string looks exactly like the output format.
7. For the route, keep the "previous point" in two variables. You can update both at once: `px, py = x, y`.
8. Swapping two variables uses the same trick: `a, b = b, a`. No temporary variable needed.

</details>
