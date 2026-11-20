# 12 - Phone Book

A phone book where each person can have several numbers, and you can also find **who** owns a number. You need two dictionaries that must always agree with each other.

## Input

One command per line, until a line with `END`. Names are a single word. Uppercase and lowercase don't matter in names (`ana`, `ANA` and `Ana` are the same person). Always print names with the first letter in uppercase and the rest in lowercase.

| Command | What it does |
|---|---|
| `ADD name number` | saves the number for that person. Prints nothing, except: if the number already belongs to this person, print `ALREADY SAVED`, and if it belongs to someone else, print `TAKEN BY Name` and don't save it |
| `FIND name` | prints `Name: n1, n2` (numbers in the order they were added), or `NOT FOUND: Name` |
| `WHO number` | prints the owner's name, or `UNKNOWN` |
| `DEL name` | deletes the person and all their numbers, then prints `DELETED Name`. If the person doesn't exist, print `NOT FOUND: Name` |
| `LIST` | prints every person as in `FIND`, in alphabetical order, or `EMPTY` |

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
ADD ana 1111
ADD ana 2222
ADD bruno 3333
ADD Bruno 1111
ADD ana 2222
FIND ANA
WHO 3333
WHO 9999
LIST
DEL ana
WHO 1111
FIND ana
LIST
END
</pre></td>
<td><pre>
TAKEN BY Ana
ALREADY SAVED
Ana: 1111, 2222
Bruno
UNKNOWN
Ana: 1111, 2222
Bruno: 3333
DELETED Ana
UNKNOWN
NOT FOUND: Ana
Bruno: 3333
</pre></td>
</tr>
<tr>
<td><pre>
LIST
DEL zoe
END
</pre></td>
<td><pre>
EMPTY
NOT FOUND: Zoe
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Dictionary 1: name → **list** of numbers, like `{"Ana": ["1111", "2222"]}`. A value can be any type, even a list.
2. Dictionary 2: number → name, like `{"1111": "Ana"}`. This is the **reverse lookup**: without it, `WHO` would have to search every person's list.
3. Keep numbers as text. They are labels, not quantities: nobody adds two phone numbers together.
4. Normalize the name once, right after reading it (`.capitalize()`), and use only that version from then on.
5. When a person is new, create their list first: `if name not in book: book[name] = []`.
6. `.get(key, default)` is great for `WHO`: one line, no `if`.
7. `book.pop(name)` removes a key **and** gives you its value back. That's useful for `DEL`, because you also have to clean those numbers out of the second dictionary. If you forget, `WHO 1111` will say `Ana` after Ana was deleted.
8. `sorted(book)` gives the keys of a dictionary in order.

</details>
