# 11 - Word Counter

Your first **dictionary**: count how many times each word appears in a text. "Counting things" is one of the most common jobs in programming, and dictionaries are made for it.

## Input

The first line contains **K** (1 ≤ K ≤ 20). Then come lines of text, until a line with `END`.

## Output

A **word** is a piece of text between spaces, with these characters removed from its start and end: `. , ! ? ; : " ' ( )`. Uppercase and lowercase don't matter (`The` and `the` are the same word). Pieces that are empty after cleaning are not words.

Print:

```
TOTAL WORDS = <how many words in total>
UNIQUE WORDS = <how many different words>
TOP K:
```

Then the K most common words, from the most common. When two words have the same count, they go in alphabetical order. If there are fewer than K different words, print all of them.

Each word is padded with dots on the right to 15 characters, followed by its count right-aligned in 3 characters. Words have at most 12 letters.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
The cat and the dog.
"The dog" barked; the CAT ran!
END
</pre></td>
<td><pre>
TOTAL WORDS = 11
UNIQUE WORDS = 6
TOP 3:
the............  4
cat............  2
dog............  2
</pre></td>
</tr>
<tr>
<td><pre>
5
Go go GO!
END
</pre></td>
<td><pre>
TOTAL WORDS = 3
UNIQUE WORDS = 1
TOP 5:
go.............  3
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. A dictionary maps **keys** to **values**: `counts = {"the": 4, "cat": 2}`. `counts["dog"] = 1` adds or changes a key.
2. `counts["dog"] += 1` crashes the first time, because `"dog"` isn't there yet. The classic fix: `counts[w] = counts.get(w, 0) + 1`. `.get()` returns `0` when the key is missing.
3. `.strip(".,!?")` removes **any** of those characters from both ends, not the exact text `".,!?"`. Try `"!!hi?.".strip(".,!?")` in the terminal.
4. `len(counts)` is the number of different words.
5. `for word, count in counts.items():` walks through the keys and values together.
6. Sorting: you can't easily sort a dictionary by its values yet (that's `key=` in Level 03). But you know the tuple trick from exercise 10! Build `(-count, word)` tuples. The minus sign makes the biggest count come first, and equal counts fall back to the word, in alphabetical order.
7. `f"{word:.<15}"` pads with dots instead of spaces. The character before `<` is the fill character.

</details>
