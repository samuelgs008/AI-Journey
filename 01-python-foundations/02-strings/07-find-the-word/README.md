# 07 - Find the Word

In Level 01 you used `in` to check **if** a letter is in a string. It works with whole words too. To know **where** a word is and **how many times** it appears, there are methods.

Read a text and a word. Say how many times the word appears in the text, and where its first and last appearances start.

## Input

The first line contains a text **T** (1 ≤ length ≤ 1000). The second line contains a word **W** (1 ≤ length ≤ 100). Uppercase and lowercase are different: `Python` is not `python`.

## Output

If W appears in T, print three lines: `COUNT = X` (how many times it appears), `FIRST = Y` (the index where the first one starts) and `LAST = Z` (the index where the last one starts).

Otherwise, print `NOT FOUND`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
banana
an
</pre></td>
<td><pre>
COUNT = 2
FIRST = 1
LAST = 3
</pre></td>
</tr>
<tr>
<td><pre>
the cat and the hat
the
</pre></td>
<td><pre>
COUNT = 2
FIRST = 0
LAST = 12
</pre></td>
</tr>
<tr>
<td><pre>
Python
python
</pre></td>
<td><pre>
NOT FOUND
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `"an" in "banana"` gives `True`.
2. `.count(w)` tells how many times `w` appears, and `.find(w)` gives the index of the first one. `.rfind(w)` is like `.find()`, but searches from the **right**.
3. What does `.find()` give when the word isn't there? Try it.
4. There is also `.index()`: the same as `.find()`, but it crashes with a `ValueError` when the word isn't there. Try both with a missing word and compare.
5. Bonus: to search ignoring case, convert both texts before searching: `t.lower().find(w.lower())`.

</details>

## ⚡ Challenge

Here you learn that `.count()` skips **overlapping** matches, and how to search step by step with the second argument of `.find()`.

Rules: don't use `.count()` or slices to find the overlapping matches.

### Input

The same as the main problem: a text **T** and a word **W**.

### Output

Print two lines: `COUNT = X`, the result of `.count()`, and `OVERLAPPING = Y`, the number of matches when they are allowed to share characters. In `aaaa`, the word `aa` starts at indexes 0, 1 and 2: that's 3 overlapping matches.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
aaaa
aa
</pre></td>
<td><pre>
COUNT = 2
OVERLAPPING = 3
</pre></td>
</tr>
<tr>
<td><pre>
banana
ana
</pre></td>
<td><pre>
COUNT = 1
OVERLAPPING = 2
</pre></td>
</tr>
<tr>
<td><pre>
abc
d
</pre></td>
<td><pre>
COUNT = 0
OVERLAPPING = 0
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. `.find()` accepts a second number: where to **start** searching. Try `"banana".find("ana", 2)`.
2. When you find a match at index `p`, the next search starts at `p + 1`. Why not at `p + len(w)`? (That's what `.count()` does!)
3. Keep searching until `.find()` gives `-1`. The walrus `:=` from Level 01 fits nicely in this `while`.

</details>
