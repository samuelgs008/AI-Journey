# 06 - Word Wrap

Your editor, your phone and every website do this all the time: break a long text into lines that fit a width. It looks simple, but there are a few traps.

## Input

The first line contains the maximum width **W** (1 ≤ W ≤ 80). The second line contains a text: words separated by one or more spaces.

## Output

Break the text into lines:

- Put as many words as possible on each line, separated by **one** space, without passing W characters.
- A word longer than W goes **alone** on its own line (never cut a word).

Print the lines inside a box made with `+`, `-` and `|`, each line padded with spaces on the right. The inside of the box is W characters wide, or the length of the longest line if that's bigger.

Then print:

```
WORDS = <number of words>
LINES = <number of lines>
LONGEST = <the longest word; the first one if there's a tie>
```

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
16
The quick brown fox jumps over the lazy dog
</pre></td>
<td><pre>
+----------------+
|The quick brown |
|fox jumps over  |
|the lazy dog    |
+----------------+
WORDS = 9
LINES = 3
LONGEST = quick
</pre></td>
</tr>
<tr>
<td><pre>
5
Python is extraordinary
</pre></td>
<td><pre>
+-------------+
|Python       |
|is           |
|extraordinary|
+-------------+
WORDS = 3
LINES = 3
LONGEST = extraordinary
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Keep a list `lines` with the finished lines and a string `current` with the line you're building.
2. For each word, ask: "if I add a space and this word to `current`, is it still at most W?" If yes, add it. If no, save `current` to `lines` and start a new line with this word.
3. Careful with the very first word of a line: it has no space before it. An empty `current` is the special case.
4. When the loop ends, the last line is still in `current`. Don't forget to save it! That's the classic bug of this exercise.
5. Sample 2: `Python` (6 letters) is already longer than W = 5, so it goes alone. Then `is` can't join it either.
6. `f"|{line:<{width}}|"` pads the line with spaces on the right.
7. Walk through sample 1 on paper, word by word, writing down `current` each time. It's faster than guessing.

</details>
