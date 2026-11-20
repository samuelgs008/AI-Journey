# 02 - Word Detective

Find every place a word appears in a text and mark it. Strings are immutable, so you can't change the text: you have to **build a new one** from slices.

## Input

The first line is a text. The second line is a word to search for.

## Output

Search for the word **ignoring uppercase and lowercase**. It can also be part of a bigger word (`cat` is found inside `Catalog`). After a match, continue searching **after** it, so matches never overlap.

Print three lines:

1. `FOUND = N`, the number of matches.
2. The text with each match wrapped in `[` and `]`, keeping the **original** uppercase and lowercase of the text.
3. `POSITIONS =` and the index where each match starts, separated by spaces, or `POSITIONS = NONE`.

Rules: no `.replace()`, no `.split()`, no lists. Use `.find()` and slices.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
The cat sat on the CAT mat. Catalog!
cat
</pre></td>
<td><pre>
FOUND = 3
The [cat] sat on the [CAT] mat. [Cat]alog!
POSITIONS = 4 19 28
</pre></td>
</tr>
<tr>
<td><pre>
banana
ana
</pre></td>
<td><pre>
FOUND = 1
b[ana]na
POSITIONS = 1
</pre></td>
</tr>
<tr>
<td><pre>
Hello world
python
</pre></td>
<td><pre>
FOUND = 0
Hello world
POSITIONS = NONE
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Search in a lowercase **copy** of the text, but cut the pieces from the **original**. The positions are the same in both.
2. `.find(word, start)` starts searching at `start`. It returns `-1` when there are no more matches: perfect for a `while` loop.
3. Keep a variable `last` with where the previous match ended. Each time, add `text[last:pos]`, then `"["`, the match, `"]"`.
4. Don't forget the piece of text **after** the last match.
5. Sample 2: `banana` has `ana` at index 1 and also at index 3, but they share the `a` in the middle. The next search starts at `1 + len("ana")`, so the second one is skipped.
6. You can build the positions text the same way: start with `""` and add `f" {pos}"` each time. Then check if it's still empty.

</details>
