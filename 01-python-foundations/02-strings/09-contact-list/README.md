# 09 - Contact List

Split a text into words, take something from each word, and glue the results together. This pattern solves a huge number of text problems.

Here you also learn that strings can be compared with `<`, `>` and `==`, just like numbers. Python puts them in alphabetical order... almost. There are a few surprises.

Read a list of contacts. Print the initials of each one, then the contacts that come first and last in a phone's contact list.

## Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come N lines, each with a full name: one or more words separated by single spaces, in any mix of uppercase and lowercase. No two names are equal when you ignore case.

## Output

For each name, print its initials in uppercase, with nothing between them. Then print two lines: `FIRST = X` and `LAST = Y`, the names that come first and last in dictionary order, **ignoring** uppercase and lowercase. Print them exactly as they were typed.

Rules: no `min()`, no `max()` and no lists.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4
ana maria lima
Bruno Costa
carla dias
ANDRE SOUZA
</pre></td>
<td><pre>
AML
BC
CD
AS
FIRST = ana maria lima
LAST = carla dias
</pre></td>
</tr>
<tr>
<td><pre>
1
python
</pre></td>
<td><pre>
P
FIRST = python
LAST = python
</pre></td>
</tr>
<tr>
<td><pre>
3
Zoe Alves
bia rocha
Carlos Melo
</pre></td>
<td><pre>
ZA
BR
CM
FIRST = bia rocha
LAST = Zoe Alves
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `.split()` gives you the words, and the first letter of a word is at index `0`. Start with an empty string and add one letter per word, like in the exercise 04 challenge.
2. You can convert each letter to uppercase, or only once at the end. Which one is simpler?
3. `"apple" < "banana"` is `True`. Python compares the first letters. If they are equal, it compares the second ones, and so on. When one word is the start of the other, the shorter one comes first: `"car" < "card"`.
4. Look at sample 3 without ignoring case: `"Zoe Alves" < "bia rocha"` is `True`! Every character has a number, its **code**, and Python compares those codes: all uppercase letters come before the lowercase ones. You'll do math with these codes in exercise 10.
5. So **compare** the lowercase versions, but **save** the original name.
6. Level 01, exercise 05 challenge: the first name you read is the perfect starting value for both `FIRST` and `LAST`.
7. Text compares character by character, even digits: `"10" < "9"` is `True`, because `"1"` comes before `"9"`. Remember this in exercise 11.
8. Bonus, two classic bugs: `"5" == 5` is `False`, because text is never equal to a number (and `input()` always gives text). And compare text with `==`, never with `is`: `is` checks if two values are the **same object** in memory, not if they are equal. It may work in the terminal and fail in a program.
9. Bonus, after you solve it: try `min("banana", "Zebra", "apple")` and then `min("banana", "Zebra", "apple", key=str.lower)` in the terminal. You'll understand `key=` in Level 04.

</details>

## ⚡ Challenge

Here you learn to split **from the right** with `.rsplit()`, to limit the number of cuts with `maxsplit`, and to **unpack** the pieces into variables. You'll also meet `.partition()`.

Rules: get the last name **without** `[ ]` indexing. Use unpacking.

### Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come N lines, each with a full name: at least two names, separated by single spaces, in any mix of uppercase and lowercase.

### Output

Print each name in citation style, one per line: the last name with only its first letter in uppercase, a comma and a space, then the initial of each other name followed by a dot, separated by spaces.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
ana maria lima
LEO SOUZA
joao pedro alves costa
</pre></td>
<td><pre>
Lima, A. M.
Souza, L.
Costa, J. P. A.
</pre></td>
</tr>
<tr>
<td><pre>
1
maria EDUARDA silva
</pre></td>
<td><pre>
Silva, M. E.
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"ana maria lima".split(maxsplit=1)` and `"ana maria lima".rsplit(maxsplit=1)`. What's the difference?
2. Two pieces can go straight into two variables: `first, last = ...`. It's the same trick as in the `map(int, ...)` recipe from exercise 08.
3. Another way: `"ana maria lima".rpartition(" ")` cuts at the **last** space and gives three pieces: what comes before, the separator itself, and what comes after. `.partition()` cuts at the **first** one.
4. Only the first letter in uppercase: one of the methods from exercise 05 does exactly that.
5. When you build `A. M.`, you'll probably get an extra space at the end. `.rstrip()` or `.join()` can fix that.

</details>
