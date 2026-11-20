# 04 - Shopping List

Your first **list**: a shopping list app that reads commands. Lists are like strings in many ways (indexes, slices, `len`, `in`), but you **can** change them.

## Input

One command per line, until a line with `END`. Items are text and may contain spaces.

| Command | What it does |
|---|---|
| `ADD item` | adds the item at the **end**. If it's already in the list, print `ALREADY IN LIST: item` |
| `FIRST item` | adds the item at the **start**. Same rule for repeated items |
| `REMOVE item` | removes the item. If it's not there, print `NOT FOUND: item` |
| `POP` | removes the **last** item and prints `BOUGHT: item` |
| `SHOW` | prints `LIST (n)`, then each item as `1. milk`, `2. eggs`... |
| `TOP n` | prints the first `n` items, separated by `, ` |
| `LAST n` | prints the last `n` items, separated by `, ` |
| `REVERSE` | reverses the order of the list |
| `GET i` | prints the item at position `i`, counting from **1**. A negative `i` counts from the end: `-1` is the last one. If there's no item there (or `i` is `0`), print `NO ITEM` |

If the list is empty, `POP`, `SHOW`, `TOP` and `LAST` print `EMPTY LIST`. `n` is always at least 1.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
ADD milk
ADD eggs
FIRST coffee
ADD milk
SHOW
REMOVE bread
TOP 2
LAST 1
GET 2
GET -1
GET 9
REVERSE
SHOW
POP
REMOVE coffee
POP
POP
END
</pre></td>
<td><pre>
ALREADY IN LIST: milk
LIST (3)
1. coffee
2. milk
3. eggs
NOT FOUND: bread
coffee, milk
eggs
milk
eggs
NO ITEM
LIST (3)
1. eggs
2. milk
3. coffee
BOUGHT: coffee
NOT FOUND: coffee
BOUGHT: milk
BOUGHT: eggs
</pre></td>
</tr>
<tr>
<td><pre>
ADD olive oil
ADD rice
GET 0
TOP 10
LAST 5
END
</pre></td>
<td><pre>
NO ITEM
olive oil, rice
olive oil, rice
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `items = []` is an empty list. Try these in the terminal: `.append(x)`, `.insert(0, x)`, `.remove(x)`, `.pop()`, `.reverse()`.
2. `.remove(x)` crashes if `x` is not in the list. Check with `in` first.
3. `"ADD olive oil".partition(" ")` gives `("ADD", " ", "olive oil")`: the command and the item, even when the item has spaces.
4. The walrus from Level 01 works great here: `while (line := input()) != "END":`.
5. Slices work on lists exactly like on strings: `items[:2]`, `items[-1:]`. And just like with strings, a slice never crashes, even if `n` is bigger than the list.
6. `", ".join(items)` glues a list of strings together.
7. Python counts from 0, the user counts from 1. For a positive `i`, the item is `items[i - 1]`. For a negative one, Python already counts from the end. Write the "is it in range?" condition carefully, because an empty list is also a case.
8. An empty list is "falsy": `if items:` is `True` only when the list has something in it.

</details>
