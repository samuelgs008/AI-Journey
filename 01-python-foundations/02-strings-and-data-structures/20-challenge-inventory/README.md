# 20 - 🏆 Inventory

The final boss: a small warehouse system. Products are dictionaries inside a dictionary, each one with a set of tags and a history list of tuples. On top of that, there's an `UNDO` command. Everything from this level, together.

## Input

One command per line, until a line with `END`. A SKU is a product code, like `A1` (at most 5 characters). Product names have at most 13 characters and may contain spaces.

| Command | What it does |
|---|---|
| `NEW sku price name` | creates a product with quantity 0. If the SKU already exists, print `ERROR: sku already exists` |
| `IN sku qty` | adds `qty` units to the stock |
| `OUT sku qty` | removes `qty` units. If there aren't enough, print `ERROR: only n of sku` and change nothing |
| `UNDO` | undoes the **last successful** `IN` or `OUT`, of any product, and prints `UNDONE: OUT 12 A1`. You can undo again and again. If there's nothing to undo, print `NOTHING TO UNDO` |
| `TAG sku tag1,tag2,...` | adds tags to the product. Adding a tag it already has changes nothing |
| `FIND tag` | prints the SKUs with that tag, in alphabetical order, separated by `, `, or `NONE` |
| `HISTORY sku` | prints the product's moves in order, like `IN 30, OUT 12`, or `NO MOVES` |
| `LOW n` | prints the products with fewer than `n` units, as `sku (qty)`, from the lowest quantity (ties: SKU in alphabetical order), separated by `, `, or `NONE` |
| `REPORT` | prints the stock table (below) |

`IN`, `OUT`, `TAG` and `HISTORY` with a SKU that doesn't exist print `ERROR: unknown sku`. Commands that print an error change nothing. All other commands print nothing when they work.

**REPORT** prints a header, one row per product (SKUs in alphabetical order) and a total. The columns are: SKU left-aligned in 6, name left-aligned in 14, quantity right-aligned in 5, value (`qty × price`) right-aligned in 11 with a thousands separator and 2 decimal places. The total row is `TOTAL` left-aligned in 25, then the total value right-aligned in 11.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
NEW A1 19.90 USB cable
NEW B7 1250 Monitor 27
NEW A1 5 Other
IN A1 30
IN B7 4
OUT A1 12
OUT B7 10
IN C3 5
TAG A1 cable,usb
TAG B7 screen,usb
FIND usb
FIND sale
HISTORY A1
LOW 10
REPORT
UNDO
UNDO
HISTORY A1
REPORT
END
</pre></td>
<td><pre>
ERROR: A1 already exists
ERROR: only 4 of B7
ERROR: unknown C3
A1, B7
NONE
IN 30, OUT 12
B7 (4)
SKU   NAME            QTY      VALUE
A1    USB cable        18     358.20
B7    Monitor 27        4   5,000.00
TOTAL                       5,358.20
UNDONE: OUT 12 A1
UNDONE: IN 4 B7
IN 30
SKU   NAME            QTY      VALUE
A1    USB cable        30     597.00
B7    Monitor 27        0       0.00
TOTAL                         597.00
</pre></td>
</tr>
<tr>
<td><pre>
UNDO
NEW Z9 2.50 Pen
HISTORY Z9
LOW 1
REPORT
END
</pre></td>
<td><pre>
NOTHING TO UNDO
NO MOVES
Z9 (0)
SKU   NAME            QTY      VALUE
Z9    Pen               0       0.00
TOTAL                           0.00
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. **Design the data first, on paper, before any code.** One product could be:
   `inventory["A1"] = {"name": "USB cable", "price": 19.9, "qty": 18, "tags": {"usb", "cable"}, "history": [("IN", 30), ("OUT", 12)]}`
2. `line.split()` and then `" ".join(parts[3:])` gives you back a name with spaces.
3. Write and test **one command at a time**: `NEW` and `REPORT` first (so you can see what's going on), then `IN`/`OUT`, then the others. Don't write everything and run it at the end.
4. Sets: `tags |= {"a", "b"}` adds tags, and repeated ones don't matter.
5. **UNDO** is a **stack**: the last thing in is the first thing out. Keep a list of the SKUs of successful moves. `.append()` puts one on top, `.pop()` takes the top one. The last move of that SKU's history is the one to undo.
6. Undoing an `IN` removes the units, and undoing an `OUT` puts them back. Look at the second `REPORT`: after undoing `IN 4`, B7 is back to 0.
7. A failed `OUT` must not go into the history or the undo stack. Sample 1 checks that: `OUT B7 10` fails, so the second `UNDO` undoes `IN 4 B7`.
8. `LOW` and `FIND` are a good place for comprehensions and the tuple trick for sorting.
9. When it works, look at your code and ask: "what would I do differently next time?" Write the answer at the top of `main.py` as a comment.

</details>
