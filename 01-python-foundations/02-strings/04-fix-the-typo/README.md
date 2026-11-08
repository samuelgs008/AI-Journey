# 04 - Fix the Typo

Strings are **immutable**: once created, they can never change, not even one letter. To "change" a string, you build a **new** one and save it in the variable.

A word has one wrong letter. Read the word, the position of the wrong letter and the right letter, then print the fixed word.

⚠️ First, try `w[1] = "y"` in the terminal and read the error. Then fix the word the right way.

## Input

The first line contains a word **W** (1 ≤ length ≤ 100). The second line contains an integer **P** (1 ≤ P ≤ length of W): the position of the wrong letter, counting from 1. The third line contains the right letter **L**.

## Output

Print the fixed word.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
pithon
2
y
</pre></td>
<td><pre>
python
</pre></td>
</tr>
<tr>
<td><pre>
jello
1
h
</pre></td>
<td><pre>
hello
</pre></td>
</tr>
<tr>
<td><pre>
codr
4
e
</pre></td>
<td><pre>
code
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. That error, `TypeError: 'str' object does not support item assignment`, is immutability: Python doesn't let you change a character in place.
2. Build the new word from three pieces: everything **before** the position, the right letter, and everything **after** it.
3. The slices from exercise 03 give you the pieces. Remember: P counts from 1, but indexes count from 0.

</details>

## ⚡ Challenge

Here you learn the most common way to build a string: start **empty** and add one piece per loop turn. You also meet `enumerate()`, which gives you the index and the character together.

Rules: no `[ ]` indexing (no `s[i]`), and a **single `print()`, after the loop**: it must run only once.

### Input

A single line with a sentence **S** (1 ≤ length ≤ 100).

### Output

Print S with alternating case: the character at index 0 in uppercase, index 1 in lowercase, index 2 in uppercase, and so on. Spaces count as characters too.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
hello world
</pre></td>
<td><pre>
HeLlO WoRlD
</pre></td>
</tr>
<tr>
<td><pre>
PYTHON
</pre></td>
<td><pre>
PyThOn
</pre></td>
</tr>
<tr>
<td><pre>
a
</pre></td>
<td><pre>
A
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Create `result = ""` before the loop and do `result += piece` inside it. The string doesn't change: `+=` builds a new one each turn and saves it back in the variable.
2. Try `for i, ch in enumerate("abc"): print(i, ch)`. What does `enumerate` give you on each turn?
3. `"a".upper()` gives `"A"` and `"B".lower()` gives `"b"`. Even index: uppercase. Odd index: lowercase. You already know how to check if a number is even.

</details>
