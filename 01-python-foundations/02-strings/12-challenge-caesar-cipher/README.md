# 12 - 🏆 Challenge: Caesar Cipher

Julius Caesar hid his messages by shifting each letter of the alphabet. With a shift of 3, `A` becomes `D`, `B` becomes `E`... and at the end it wraps around: `X` becomes `A`.

Here you learn that, inside the computer, every character is a **number**, and you do math with letters using `ord()` and `chr()`.

Read a shift **K** and a message, and print the encrypted message.

## Input

The first line contains an integer **K** (0 ≤ K ≤ 1000). The second line contains the message (1 ≤ length ≤ 1000), with English letters, digits, spaces and punctuation (no accents).

## Output

Print the encrypted message. Uppercase letters stay uppercase, lowercase letters stay lowercase, and everything that is not a letter stays the same.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
Hello, World!
</pre></td>
<td><pre>
Khoor, Zruog!
</pre></td>
</tr>
<tr>
<td><pre>
1
xyz XYZ 123
</pre></td>
<td><pre>
yza YZA 123
</pre></td>
</tr>
<tr>
<td><pre>
26
Python
</pre></td>
<td><pre>
Python
</pre></td>
</tr>
<tr>
<td><pre>
29
abc
</pre></td>
<td><pre>
def
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `ord("a")` gives `97`, and `chr(97)` gives `"a"`: they are opposites. Try `chr(ord("a") + 3)`.
2. To wrap around, turn the letter into its position in the alphabet, from 0 to 25: `ord(ch) - ord("a")`. Add K and use `% 26`, the same trick as in Level 01's time converter. Then turn the position back into a letter.
3. Uppercase letters have other codes (`ord("A")` is `65`). `.isupper()` and `.islower()` tell you which starting point to use.
4. Bonus: every character in the world has a code, in any language, emojis included. This system is called **Unicode**. Try `ord("ã")` and `ord("😀")`. Then compare `len("😀")` with `len("😀".encode())`: saved in a file (UTF-8), one emoji takes 4 **bytes**.
5. Bonus: you can write any character by its code: `"\u00e7"` is `"ç"` (`e7` is 231, the code of `ç`, written in hexadecimal, which you'll study in Level 07).

</details>

## ⚡ Challenge

Here you learn `str.maketrans()` and `.translate()`: a **translation table** that swaps many characters in one go. Now you **decrypt** the message, without a single loop.

Rules: no loops, no `ord()` and no `chr()`. You may type the alphabet: `"abcdefghijklmnopqrstuvwxyz"`.

### Input

The first line contains the shift **K** (0 ≤ K ≤ 1000) that was used to encrypt. The second line contains the encrypted message.

### Output

Print the original message.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
Khoor, Zruog!
</pre></td>
<td><pre>
Hello, World!
</pre></td>
</tr>
<tr>
<td><pre>
1
yza YZA 123
</pre></td>
<td><pre>
xyz XYZ 123
</pre></td>
</tr>
<tr>
<td><pre>
29
def
</pre></td>
<td><pre>
abc
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `table = str.maketrans("abc", "xyz")` and then `"aabbcc".translate(table)`. Each character of the first string turns into the character at the same position in the second one.
2. Write down the alphabet shifted by 3: `defghijklmnopqrstuvwxyzabc`. Can you build it with two slices of the normal alphabet?
3. Encrypting goes from the normal alphabet to the shifted one. Decrypting goes the other way. And K can be bigger than 26...
4. One table can handle uppercase too: glue the uppercase alphabets after the lowercase ones (`.upper()`!).
5. Typing the alphabet is fine for now. From Level 05 on, `import string` gives you `string.ascii_lowercase`, ready to use.

</details>
