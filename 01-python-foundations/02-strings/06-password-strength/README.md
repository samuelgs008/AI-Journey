# 06 - Password Strength

Some methods answer **yes-or-no questions** about a string: is it uppercase? Is it a digit? Their names start with `is`, and they return `True` or `False`.

Read a password and count its uppercase letters, lowercase letters, digits and symbols. A **symbol** is any character that is none of the other three, spaces included.

A password is **strong** when it has at least 8 characters **and** at least one character of each of the four kinds.

## Input

The input contains a single line with a password **P** (1 ≤ length ≤ 100).

## Output

Print five lines: `UPPER = A`, `LOWER = B`, `DIGITS = C`, `SYMBOLS = D`, and then `STRONG` or `WEAK`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python123!
</pre></td>
<td><pre>
UPPER = 1
LOWER = 5
DIGITS = 3
SYMBOLS = 1
STRONG
</pre></td>
</tr>
<tr>
<td><pre>
password
</pre></td>
<td><pre>
UPPER = 0
LOWER = 8
DIGITS = 0
SYMBOLS = 0
WEAK
</pre></td>
</tr>
<tr>
<td><pre>
A1b2#
</pre></td>
<td><pre>
UPPER = 1
LOWER = 1
DIGITS = 2
SYMBOLS = 1
WEAK
</pre></td>
</tr>
<tr>
<td><pre>
Hello World 2026
</pre></td>
<td><pre>
UPPER = 2
LOWER = 8
DIGITS = 4
SYMBOLS = 2
STRONG
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Try `"A".isupper()`, `"a".islower()` and `"7".isdigit()`. Each one checks the string and answers `True` or `False`.
2. Go through the characters (`for ch in p:`) and use `if` / `elif` / `else` to decide which counter grows. The `else` catches the symbols.
3. Look at sample 3: it has every kind of character, but is it long enough?
4. Bonus: there are more `is` methods. Try `.isalpha()` (only letters), `.isalnum()` (letters or digits) and `.isspace()` (only spaces).

</details>

## ⚡ Challenge

Here you learn to **validate text before converting it**: `int("abc")` crashes your program, and the proper fix (`try`/`except`) only comes in Level 06. You also meet `.startswith()`.

Rules: the program must **never crash**, whatever the input.

### Input

Several lines. A valid integer is made of digits only, with an optional `-` in front (like `-12`). The last line is always a valid integer, there are no empty lines, and each line has at most 100 characters.

### Output

For each invalid line, print `X is not an integer`, where X is the line. When a valid integer arrives, print `DOUBLE = Y`, where Y is that number times 2, and stop.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
abc
3.5
-
-12
</pre></td>
<td><pre>
abc is not an integer
3.5 is not an integer
- is not an integer
DOUBLE = -24
</pre></td>
</tr>
<tr>
<td><pre>
12a
--5
40
</pre></td>
<td><pre>
12a is not an integer
--5 is not an integer
DOUBLE = 80
</pre></td>
</tr>
<tr>
<td><pre>
7
</pre></td>
<td><pre>
DOUBLE = 14
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"42".isdigit()` and `"-42".isdigit()`. Why is the second one `False`?
2. `s.startswith("-")` checks how the text **begins**. If it begins with `-`, the rest of it (a slice!) must be all digits.
3. Look at the `-` alone in sample 1. What is `"".isdigit()`? Does that help you?
4. Reading until the input is valid: you did that in Level 01, exercise 14.
5. Bonus: `.endswith()` checks how the text **ends**. Try `"photo.png".endswith(".png")`. Both methods also accept several options at once: `name.endswith((".png", ".jpg"))` (the double parentheses will make sense in Level 03).
6. Pro tip: `"²".isdigit()` is `True`, but `int("²")` crashes! `.isdecimal()` is stricter: it only accepts the digits that `int()` understands. When you validate text before converting it, prefer `.isdecimal()`.

</details>
