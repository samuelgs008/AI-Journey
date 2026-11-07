# 05 - Case Converter

Strings come with **methods**: functions that belong to them and are called with a dot, like the `.lower()` you used in Level 01. A string method never changes the string (it's immutable!). It gives you a **new** string.

Read a sentence and print it in five different cases.

## Input

The input contains a single line with a sentence **S** (1 ≤ length ≤ 100).

## Output

Print five lines:

- `UPPER = ` followed by S with every letter in uppercase
- `LOWER = ` followed by S with every letter in lowercase
- `TITLE = ` followed by S with the first letter of each word in uppercase and the rest in lowercase
- `CAPITALIZE = ` followed by S with only its first character in uppercase and the rest in lowercase
- `SWAPCASE = ` followed by S with uppercase letters turned into lowercase, and the other way around

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
hello wORLD from python
</pre></td>
<td><pre>
UPPER = HELLO WORLD FROM PYTHON
LOWER = hello world from python
TITLE = Hello World From Python
CAPITALIZE = Hello world from python
SWAPCASE = HELLO World FROM PYTHON
</pre></td>
</tr>
<tr>
<td><pre>
it's a dog's life
</pre></td>
<td><pre>
UPPER = IT'S A DOG'S LIFE
LOWER = it's a dog's life
TITLE = It'S A Dog'S Life
CAPITALIZE = It's a dog's life
SWAPCASE = IT'S A DOG'S LIFE
</pre></td>
</tr>
<tr>
<td><pre>
PYTHON 3.13 rocks
</pre></td>
<td><pre>
UPPER = PYTHON 3.13 ROCKS
LOWER = python 3.13 rocks
TITLE = Python 3.13 Rocks
CAPITALIZE = Python 3.13 rocks
SWAPCASE = python 3.13 ROCKS
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. You already know `.lower()`. The others are `.upper()`, `.title()`, `.capitalize()` and `.swapcase()`. Try each one in the terminal.
2. Try `s = "abc"`, then `s.upper()`, then `print(s)`. Did `s` change? Why not? How would you keep the uppercase version?
3. Look at the TITLE line in sample 2: `It'S`. A bug in your code? No: `.title()` starts a new word after **any** character that isn't a letter, `'` included. You'll fix that in the challenge.
4. Bonus: to compare text ignoring case, use `.casefold()`. It's like `.lower()`, but it also knows rules from other languages: `"Straße".lower()` keeps the `ß`, while `"Straße".casefold()` gives `"strasse"`.
5. You don't need to memorize every method: there are more than 40. `print(dir(""))` lists them all (ignore the ones with `__`), and `help(str.center)` explains one. Knowing how to look things up is a skill too.

</details>

## ⚡ Challenge

Here you fix a method you don't like by writing **your own version** of it. You also learn the **previous character** pattern: deciding what to do with a character by looking at the one before it. You'll need it again in the final challenge.

Rules: no `.title()` and no `.capitalize()`.

### Input

The same as the main problem: a sentence **S**.

### Output

Print S in title case, done right: a letter becomes uppercase when it is the first character of S or comes right after a space. Every other letter becomes lowercase. Characters that aren't letters stay the same.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
it's a dog's life
</pre></td>
<td><pre>
It's A Dog's Life
</pre></td>
</tr>
<tr>
<td><pre>
3rd PLACE in the race
</pre></td>
<td><pre>
3rd Place In The Race
</pre></td>
</tr>
<tr>
<td><pre>
  hello   WORLD
</pre></td>
<td><pre>
  Hello   World
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Go through the characters and keep the **previous** one in a variable, updated at the end of each turn. The rule only asks one question about it: is it a space?
2. What should the "previous character" be before the loop starts, so that the first letter of S becomes uppercase?
3. `.upper()` and `.lower()` don't change characters that aren't letters: `"'".upper()` is `"'"`, and `"3".lower()` is `"3"`. You don't need special cases for them.
4. Build the result like in the exercise 04 challenge: start empty and add one character per turn.
5. Compare with `.title()` on sample 2: `"3rd".title()` gives `"3Rd"`. Your version only looks at spaces, so it gets it right.

</details>
