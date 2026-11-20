# 01 - Ticket Printer

Print an event ticket inside a box. To do it you need quotes inside text, backslashes that don't turn into something else, `len()`, centering with f-strings and Unicode box characters.

## Input

Three lines: the event name, the guest's full name and the seat code. The event name may contain double quotes.

## Output

Build these four lines of text:

```
Event: "<event>"
Guest: <guest>
Seat: <seat>
File: C:\tickets\<file>.txt
```

`<file>` is the guest's name in lowercase, with every space replaced by `_`.

Then print the four lines inside a box made with the characters `╔ ═ ╗ ║ ╚ ╝`. The inside of the box is **4 characters wider** than the longest of the four lines, and every line is **centered**. When the free space can't be split evenly, the extra space goes on the right.

Rules: print the whole ticket with **one** `print()` and **one** triple-quoted f-string.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
Python Day
Ana Lima
B12
</pre></td>
<td><pre>
╔═════════════════════════════════╗
║       Event: "Python Day"       ║
║         Guest: Ana Lima         ║
║            Seat: B12            ║
║  File: C:\tickets\ana_lima.txt  ║
╚═════════════════════════════════╝
</pre></td>
</tr>
<tr>
<td><pre>
AI & Data "Live"
Teo
A1
</pre></td>
<td><pre>
╔═════════════════════════════╗
║  Event: "AI & Data "Live""  ║
║         Guest: Teo          ║
║          Seat: A1           ║
║  File: C:\tickets\teo.txt   ║
╚═════════════════════════════╝
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. A string can hold `"` if you open it with `'`: `'Event: "x"'`. Or escape it: `"Event: \"x\""`.
2. Watch the path: `"C:\tickets"` contains `\t`, which is a **TAB**, not a backslash and a `t`! Print it and see. Two fixes: `\\` (an escaped backslash), or a raw string `r"C:\tickets"`. f-strings can be raw too: `rf"..."`.
3. You can find the longest line with the "greatest so far" pattern, or with `max(len(a), len(b), ...)`.
4. In an f-string, the width can be a variable: `f"{text:^{w}}"` centers `text` in `w` characters.
5. A triple-quoted f-string can span many lines, and every line break inside it is printed: `f"""line 1\nline 2"""` is written as two real lines.
6. `"═" * w` builds the top and bottom of the box. In Python 3.12+ you can put it straight inside the f-string: `{"═" * w}`.
7. `═`, `║` and `╔` are normal characters for Python, like `a`: each one has `len()` 1. That's Unicode. If the terminal shows strange symbols, it's the terminal's font, not your code.

</details>
