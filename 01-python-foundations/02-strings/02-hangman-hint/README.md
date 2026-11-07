# 02 - Hangman Hint

A string is a **sequence**: its characters are in order, and each one has a **position**, called its **index**. The first character is at index **0**, not 1.

Here you meet the basic tools for any sequence: `len()` to measure it, `[ ]` to pick one character, `+` to glue strings together (**concatenation**) and `*` to repeat them.

In the game of hangman, the player only sees the first and the last letters of the secret word, with a `_` for each hidden letter. Read the secret word and print the hint.

⚠️ In this exercise, no f-strings and no commas inside `print()`: build each line with `+`. You'll see why `str()` exists.

## Input

The input contains a single word **W** (1 ≤ length ≤ 50).

## Output

Print two lines: the hint (the first letter, one `_` for each letter in the middle, and the last letter) and `LENGTH = X`, where X is the number of letters in W.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python
</pre></td>
<td><pre>
P____n
LENGTH = 6
</pre></td>
</tr>
<tr>
<td><pre>
keyboard
</pre></td>
<td><pre>
k______d
LENGTH = 8
</pre></td>
</tr>
<tr>
<td><pre>
hi
</pre></td>
<td><pre>
hi
LENGTH = 2
</pre></td>
</tr>
<tr>
<td><pre>
a
</pre></td>
<td><pre>
a
LENGTH = 1
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `len("Python")` gives `6`. `w[0]` is the first character: try `w[1]` and `w[2]` in the terminal too.
2. A word with 6 letters has indexes from 0 to 5. You could find the last one with `len(w)`, but Python has a shortcut: **negative indexes** count from the end. Try `w[-1]` and `w[-2]`.
3. `"_" * 4` gives `"____"`. How many `_` does a word with 6 letters need?
4. Try `"LENGTH = " + 6` and read the error: `TypeError: can only concatenate str (not "int") to str`. Python doesn't guess: to it, text plus a number makes no sense. `str(6)` gives `"6"`, the number turned into text.
5. Look at sample 4: in a word with one letter, the first letter is also the last one. Does your code print it twice?

</details>

## ⚡ Challenge

Here you learn to convert between how **people** count (from 1) and how **Python** counts (from 0), what an `IndexError` is, and how to avoid it. f-strings are allowed again.

Rules: the program must **never crash**.

### Input

The first line contains a word **W** (1 ≤ length ≤ 100). The second line contains an integer **K** (1 ≤ K ≤ 1000).

### Output

If W has at least K letters, print two lines: `START = X`, where X is the K-th letter counting from the start, and `END = Y`, where Y is the K-th letter counting from the end. Both count from 1, the way people do.

Otherwise, print `OUT OF RANGE`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python
2
</pre></td>
<td><pre>
START = y
END = o
</pre></td>
</tr>
<tr>
<td><pre>
Python
6
</pre></td>
<td><pre>
START = n
END = P
</pre></td>
</tr>
<tr>
<td><pre>
Python
7
</pre></td>
<td><pre>
OUT OF RANGE
</pre></td>
</tr>
<tr>
<td><pre>
a
1
</pre></td>
<td><pre>
START = a
END = a
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"abc"[5]` and read the error: `IndexError: string index out of range`. That's what you must avoid.
2. The 1st letter is at index 0, the 2nd at index 1... so the K-th is at which index?
3. From the end, the 1st letter is `w[-1]` and the 2nd is `w[-2]`. See the pattern?
4. Check K against `len(w)` **before** you use it as an index.

</details>
