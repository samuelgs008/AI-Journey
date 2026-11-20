# 16 - Comprehension Gym

Comprehensions build a list, dictionary or set in **one line**, and they're everywhere in real Python code. This is a gym: seven exercises, each solved with one comprehension.

## Input

Two lines: integers separated by spaces (at least one), and a sentence.

## Output

Work with the words of the sentence in lowercase. Print each line with `print("NAME =", value)`, so Python shows lists, sets and dictionaries in its own format.

| Line | Value |
|---|---|
| `SQUARES OF EVENS` | a list with the square of each **even** number |
| `SIGNS` | a list with `"+"`, `"-"` or `"0"` for each number |
| `LAST DIGITS` | the last digit of each number, without repeats, as a sorted list. The last digit of `-7` is `7` |
| `LENGTHS` | a dictionary word → its length |
| `LONG WORDS` | a list with the words of 5+ letters, in UPPERCASE |
| `FIRST LETTERS` | a string with the first letter of each word |
| `TABLE` | for each of the **first 3** numbers (or fewer, if there are fewer), the list `[n×1, n×2, n×3]`. A list of lists |

Rules: each value is built by **one** comprehension. No `for` loops with `.append()`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4 -7 10 0 -3 6
Python is a great tool and coding is fun
</pre></td>
<td><pre>
SQUARES OF EVENS = [16, 100, 0, 36]
SIGNS = ['+', '-', '+', '0', '-', '+']
LAST DIGITS = [0, 3, 4, 6, 7]
LENGTHS = {'python': 6, 'is': 2, 'a': 1, 'great': 5, 'tool': 4, 'and': 3, 'coding': 6, 'fun': 3}
LONG WORDS = ['PYTHON', 'GREAT', 'CODING']
FIRST LETTERS = piagtacif
TABLE = [[4, 8, 12], [-7, -14, -21], [10, 20, 30]]
</pre></td>
</tr>
<tr>
<td><pre>
5
hi Hi HELLO
</pre></td>
<td><pre>
SQUARES OF EVENS = []
SIGNS = ['+']
LAST DIGITS = [5]
LENGTHS = {'hi': 2, 'hello': 5}
LONG WORDS = ['HELLO']
FIRST LETTERS = hhh
TABLE = [[5, 10, 15]]
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. The pattern is a `for` loop written backwards: `[n * 2 for n in nums]` is the same as a loop that appends `n * 2` for each `n`.
2. A filter goes at the **end**: `[n for n in nums if n > 0]`.
3. To choose a value, the `if`/`else` goes at the **start**: `["big" if n > 9 else "small" for n in nums]`. You can chain them: `a if ... else b if ... else c`. That's the one-line `if` from Level 01, inside a comprehension.
4. Curly braces make a **set**: `{n % 10 for n in nums}`. With `key: value` inside, they make a **dictionary**: `{w: len(w) for w in words}`.
5. In a dictionary comprehension, a repeated key just gets overwritten. That's why `is` appears only once in sample 1.
6. `"".join(...)` accepts a comprehension directly.
7. A comprehension inside a comprehension makes a list of lists: `[[... for i in ...] for n in ...]`. Read it from the outside in.
8. A good rule for real code: if a comprehension doesn't fit on one line, or you have to think hard to read it, use a normal loop.

</details>
