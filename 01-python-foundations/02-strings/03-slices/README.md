# 03 - Slices

An index gets **one** character. A **slice** gets a whole piece: `w[start:stop]`. Slices are everywhere in Python: later you'll use them with lists, tables and even images.

Read a word and print four slices of it. Each slice goes between square brackets, so you can see when it is empty.

⚠️ No loops and no `if`: slices do all the work.

## Input

The input contains a single word **W** (1 ≤ length ≤ 100).

## Output

Print four lines:

- `FIRST 3 = [X]`: the first 3 characters
- `LAST 3 = [X]`: the last 3 characters
- `MIDDLE = [X]`: the word without its first and last characters
- `EVERY OTHER = [X]`: the 1st, 3rd, 5th... characters

If the word is too short, a slice takes only what exists (look at sample 2).

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python
</pre></td>
<td><pre>
FIRST 3 = [Pyt]
LAST 3 = [hon]
MIDDLE = [ytho]
EVERY OTHER = [Pto]
</pre></td>
</tr>
<tr>
<td><pre>
Hi
</pre></td>
<td><pre>
FIRST 3 = [Hi]
LAST 3 = [Hi]
MIDDLE = []
EVERY OTHER = [H]
</pre></td>
</tr>
<tr>
<td><pre>
keyboard
</pre></td>
<td><pre>
FIRST 3 = [key]
LAST 3 = [ard]
MIDDLE = [eyboar]
EVERY OTHER = [kyor]
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `w[0:3]` gives the characters at indexes 0, 1 and 2. The **stop** is not included, just like in `range`.
2. You can leave out the start or the stop: `w[:3]` starts at the beginning, and `w[2:]` goes to the end. Negative indexes work too: what does `w[-3:]` give?
3. A third number is the **step**, again like in `range`: try `w[::2]`.
4. Look at sample 2: `"Hi"[:3]` doesn't crash, even though `"Hi"` has only 2 letters. Unlike indexes, slices never cause an `IndexError`.

</details>

## ⚡ Challenge

Here you learn **negative steps**: slices that walk backwards. With them, the palindrome from the Level 01 final challenge becomes one line.

Rules: no loops and no `if` (not even the one-line `if`).

### Input

The same as the main problem: a word **W**.

### Output

Print three lines:

- `REVERSED = X`: the word backwards
- `PALINDROME = True` or `PALINDROME = False`: whether the word reads the same both ways, ignoring uppercase and lowercase
- `MIRROR = X`: the word followed by its reverse, without repeating the last letter (`abc` becomes `abcba`)

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python
</pre></td>
<td><pre>
REVERSED = nohtyP
PALINDROME = False
MIRROR = PythonohtyP
</pre></td>
</tr>
<tr>
<td><pre>
Racecar
</pre></td>
<td><pre>
REVERSED = racecaR
PALINDROME = True
MIRROR = RacecaracecaR
</pre></td>
</tr>
<tr>
<td><pre>
a
</pre></td>
<td><pre>
REVERSED = a
PALINDROME = True
MIRROR = a
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `w[::-1]`. What does a step of `-1` do?
2. `==` gives `True` or `False`, and `print()` can show that value directly. But `"R" == "r"` is `False`... `.lower()` from Level 01 helps.
3. For MIRROR, you need the reversed word without its first character. Two slices in a row work. Bonus: can you do it with **one** slice? Think about where the backwards walk should start.

</details>
