# 07 - Secret Code

Every character is a number inside the computer. Here you do math with those numbers to build the **Vigenère cipher**: a secret code that was called "the unbreakable cipher" for 300 years.

## How it works

Each letter of the key says how far to move a letter of the text: `a` moves 0, `b` moves 1, `c` moves 2... up to `z`, which moves 25. After `z`, it goes back to `a`.

With the key `lemon`, the 1st letter of the text moves by `l` (11), the 2nd by `e` (4), the 3rd by `m` (12), and so on. When the key ends, it starts again from its first letter.

```
text:  A t t a c k   a t   d a w n !
key:   l e m o n l   e m   o n l e
       ↓ ↓ ↓ ↓ ↓ ↓   ↓ ↓   ↓ ↓ ↓ ↓
code:  L x f o p v   e f   r n h r !
```

Only the letters `a`-`z` and `A`-`Z` change, and they keep their uppercase or lowercase. Everything else (spaces, punctuation, digits, accented letters like `ç` or `ã`) stays the same and does **not** use a letter of the key.

To **decode**, move each letter **backwards** by the same amount.

## Input

Three lines: `ENCODE` or `DECODE`, the key (only letters, uppercase or lowercase), and the text.

## Output

One line: the encoded or decoded text.

Rules: build the result in a **list** of characters and glue it with `"".join()` at the end.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
ENCODE
lemon
Attack at dawn!
</pre></td>
<td><pre>
Lxfopv ef rnhr!
</pre></td>
</tr>
<tr>
<td><pre>
DECODE
lemon
Lxfopv ef rnhr!
</pre></td>
<td><pre>
Attack at dawn!
</pre></td>
</tr>
<tr>
<td><pre>
ENCODE
b
Ação 123
</pre></td>
<td><pre>
Bçãp 123
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `ord("a")` gives `97` and `chr(97)` gives `"a"`. Play with them in the terminal: `ord("A")`, `ord("z")`, `ord("ç")`, `ord("😀")`. Every character in the world has a number: that's **Unicode**.
2. The move for a key letter: `ord(k) - ord("a")`. Convert the key to lowercase first.
3. To move a letter and wrap around after `z`: turn it into 0-25, add the move, use `% 26`, and turn it back. Try `(25 + 3) % 26`.
4. Uppercase letters use `ord("A")` as their base, and lowercase ones use `ord("a")`.
5. Sample 3 is a trap: `"ç".isalpha()` is `True`! You need "is it between `a` and `z`?". Strings compare by their codes, so `"a" <= c <= "z"` works.
6. Use a separate counter for the key position, and only add 1 to it when you change a letter. `counter % len(key)` takes you back to the start of the key.
7. Decoding is the same code with the move turned negative. In Python, `-3 % 26` is `23`, so the wrap-around still works.
8. Bonus: a key with only one letter makes this the **Caesar cipher**, Julius Caesar's code. Sample 3 is a Caesar cipher with a move of 1.

</details>
