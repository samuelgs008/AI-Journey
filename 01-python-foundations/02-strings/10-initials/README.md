# 10 - Initials

Split a text into words, take something from each word, and glue the results together. This pattern solves a huge number of text problems.

Read a name or an expression and print its initials in uppercase.

## Input

The input contains a single line with one or more words, separated by one or more spaces (1 ≤ length ≤ 100).

## Output

Print the initials in uppercase, with nothing between them.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Portable Network Graphics
</pre></td>
<td><pre>
PNG
</pre></td>
</tr>
<tr>
<td><pre>
as soon as possible
</pre></td>
<td><pre>
ASAP
</pre></td>
</tr>
<tr>
<td><pre>
python
</pre></td>
<td><pre>
P
</pre></td>
</tr>
<tr>
<td><pre>
  machine   learning
</pre></td>
<td><pre>
ML
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `.split()` gives you the words, and the first letter of a word is at index `0`.
2. Start with an empty string and add one letter per word, like in the exercise 04 challenge.
3. You can convert each letter to uppercase, or only once at the end. Which one is simpler?

</details>

## ⚡ Challenge

Here you learn to split **from the right** with `.rsplit()`, to limit the number of cuts with `maxsplit`, and to **unpack** the pieces into variables. You'll also meet `.partition()`.

Rules: get the last name **without** `[ ]` indexing. Use unpacking.

### Input

A single line with a full name: at least two names, separated by single spaces, in any mix of uppercase and lowercase.

### Output

Print the name in citation style: the last name with only its first letter in uppercase, a comma and a space, then the initial of each other name followed by a dot, separated by spaces.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
ana maria lima
</pre></td>
<td><pre>
Lima, A. M.
</pre></td>
</tr>
<tr>
<td><pre>
LEO SOUZA
</pre></td>
<td><pre>
Souza, L.
</pre></td>
</tr>
<tr>
<td><pre>
joao pedro alves costa
</pre></td>
<td><pre>
Costa, J. P. A.
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"ana maria lima".split(maxsplit=1)` and `"ana maria lima".rsplit(maxsplit=1)`. What's the difference?
2. Two pieces can go straight into two variables: `first, last = ...`. It's the same trick as in the `map(int, ...)` recipe.
3. Another way: `"ana maria lima".rpartition(" ")` cuts at the **last** space and gives three pieces: what comes before, the separator itself, and what comes after. `.partition()` cuts at the **first** one.
4. When you build `A. M.`, you'll probably get an extra space at the end. `.rstrip()` or `.join()` can fix that.

</details>
