# 01 - Quotes and Escapes

Text in Python is a **string** (`str`): a sequence of characters between quotes. You've used strings since Level 01, but what if the text itself has quotes in it? Or a backslash?

Here you learn the difference between `'` and `"`, the **escape sequences** (special codes that start with a backslash `\`), and why braces `{ }` are special inside an f-string.

Read a name **N** and print four lines that use it.

## Input

The input contains a single line with a name **N** (letters only).

## Output

Print four lines, exactly as in the samples:

- `She said: "Hi, N!"`
- `It's N's turn.`
- `Files are in C:\Users\N\Desktop`
- `{"name": "N"}`

The last line is **JSON**, a text format that programs use to exchange data. You'll use it a lot from Phase 3 on, when your programs talk to an AI.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Ana
</pre></td>
<td><pre>
She said: "Hi, Ana!"
It's Ana's turn.
Files are in C:\Users\Ana\Desktop
{"name": "Ana"}
</pre></td>
</tr>
<tr>
<td><pre>
Leo
</pre></td>
<td><pre>
She said: "Hi, Leo!"
It's Leo's turn.
Files are in C:\Users\Leo\Desktop
{"name": "Leo"}
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Try `print('It's')`. Why does it break? Python thinks the string ended at the second `'`. A string with `'` inside can use `"` around it, and the other way around.
2. Need both kinds of quotes in the same string? Put a backslash before the quote: `\"` and `\'` are a quote **inside** the text, not the end of it.
3. The backslash starts special codes: `\n` is a new line and `\t` is a tab. Try `print("C:\new")`. Now try `print("C:\Users")`: it doesn't even run, because `\U` is the start of another code. To print one real backslash, write `\\`.
4. Inside an f-string, `{` starts a value. To print a real brace, double it: `f"{{"` prints `{`. Without the `f`, braces are normal characters.
5. Bonus: two strings side by side are glued automatically: `"Py" "thon"` is `"Python"`. It's handy for breaking a long text into several lines inside the parentheses of a `print()`.

</details>

## ⚡ Challenge

Here you learn **triple-quoted strings**, which can span many lines, and **raw strings**, where the backslash is just a backslash.

Rules: a **single `print()`**, and no `\n` or `\\` anywhere in your code.

### Input

The same as the main problem: a name **N**.

### Output

Print a cat saying hi, and then the folder path, exactly as in the samples.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Ana
</pre></td>
<td><pre>
 /\_/\
( o.o )  Hi, Ana!
 > ^ &lt;
C:\Users\Ana\Desktop
</pre></td>
</tr>
<tr>
<td><pre>
Leo
</pre></td>
<td><pre>
 /\_/\
( o.o )  Hi, Leo!
 > ^ &lt;
C:\Users\Leo\Desktop
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Three quotes, `"""`, start a string that can continue over several lines. The line breaks you type become part of the text.
2. An `r` before the quotes makes a **raw string**: in `r"C:\new"`, the `\n` is just two normal characters. You can use `r` and `f` together: `rf"..."`.
3. Is there an empty line at the top of your output? Look at what comes right after the opening `"""`.
4. Careful: if a triple-quoted string is inside an indented block (an `if`, a loop), the spaces at the start of its lines become part of the text too.

</details>
