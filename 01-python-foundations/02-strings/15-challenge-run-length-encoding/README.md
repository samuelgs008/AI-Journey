# 15 - 🏆 Final Challenge: Run-Length Encoding

The final challenge of Strings! Long runs of the same character waste space. **Run-length encoding** (RLE) compresses them: `aaabcccc` becomes `a3b1c4`. Old image formats and fax machines used this idea.

Read a text and compress it with RLE: each group of equal characters in a row becomes the character followed by the size of the group. Then show the length before and after.

## Input

The input contains a single line with letters only (1 ≤ length ≤ 1000). Uppercase and lowercase are different letters.

## Output

Print two lines: the compressed text, and `A -> B`, where A is the original length and B is the compressed length.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
aaabcccc
</pre></td>
<td><pre>
a3b1c4
8 -> 6
</pre></td>
</tr>
<tr>
<td><pre>
abc
</pre></td>
<td><pre>
a1b1c1
3 -> 6
</pre></td>
</tr>
<tr>
<td><pre>
zzzzzzzzzzzz
</pre></td>
<td><pre>
z12
12 -> 3
</pre></td>
</tr>
<tr>
<td><pre>
aAAa
</pre></td>
<td><pre>
a1A2a1
4 -> 6
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Go through the text comparing each character with the **previous** one, the pattern from the exercise 05 challenge. The same? The group grows. Different? The group ended.
2. When a group ends, add its character and its size to the result. Don't forget the **last** group: the loop ends before you save it.
3. Draw it in Excalidraw first: the value of each variable for `aaab`, turn by turn.
4. Look at sample 2: compression doesn't always make the text shorter!

</details>

## ⚡ Challenge

Now the **decoder**: turn `a3b1c4` back into `aaabcccc`. Here you learn to **parse** text character by character, including numbers with more than one digit.

Rules: a **single `for`** that goes through the text one character at a time.

### Input

A single line with an RLE text: letters, each one followed by its count (1 ≤ count ≤ 1000). A count can have more than one digit.

### Output

Print the original text.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
a3b1c4
</pre></td>
<td><pre>
aaabcccc
</pre></td>
</tr>
<tr>
<td><pre>
z12
</pre></td>
<td><pre>
zzzzzzzzzzzz
</pre></td>
</tr>
<tr>
<td><pre>
x1y10
</pre></td>
<td><pre>
xyyyyyyyyyy
</pre></td>
</tr>
<tr>
<td><pre>
a1A2a1
</pre></td>
<td><pre>
aAAa
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. `.isalpha()` and `.isdigit()` tell you what each character is.
2. A letter starts a new group, and the digits after it form the count: in `z12`, the count is `12`, not `1` and `2`.
3. Collect the digits as text (`count += ch`) and convert at the end. Or use math: `count * 10 + int(ch)`, just like in Level 01's reverse number.
4. When do you know a group is finished? When the next letter arrives... or when the text ends.

</details>
