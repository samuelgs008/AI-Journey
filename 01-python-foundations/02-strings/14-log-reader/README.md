# 14 - Log Reader

Programs write **logs**: one line of text for each thing that happens, with the date, the time, how serious it is and a message. When something breaks, someone has to read thousands of these lines. Python can read them for you.

Here you use the whole level on real-looking data, and you learn two more tricks of `.split()`: cutting at a **separator you choose**, and limiting the number of cuts with `maxsplit`.

Read a log and report its errors. The report is for a Brazilian team, so the dates must be in the format `DD/MM/YYYY`.

## Input

Several lines (at most 1000), each with a log entry: the date (`YYYY-MM-DD`), the time (`HH:MM:SS`), the level (`INFO`, `WARNING` or `ERROR`) and a message, separated by spaces. The message can have spaces too. The last line is always `END`.

## Output

For each `ERROR` entry, in order, print `[DD/MM/YYYY HH:MM:SS] message`. Then print three lines with how many entries of each level there were: `INFO = A`, `WARNING = B` and `ERROR = C`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
2026-11-07 08:15:02 INFO Server started
2026-11-07 08:20:45 WARNING Disk at 85%
2026-11-07 09:01:13 ERROR Database connection lost
2026-11-07 09:01:20 INFO Retrying connection
2026-11-07 09:02:00 ERROR Timeout after 30 s
END
</pre></td>
<td><pre>
[07/11/2026 09:01:13] Database connection lost
[07/11/2026 09:02:00] Timeout after 30 s
INFO = 2
WARNING = 1
ERROR = 2
</pre></td>
</tr>
<tr>
<td><pre>
2026-12-24 23:59:59 INFO Merry Christmas
END
</pre></td>
<td><pre>
INFO = 1
WARNING = 0
ERROR = 0
</pre></td>
</tr>
<tr>
<td><pre>
2026-01-05 07:30:00 INFO Scanning the ERROR folder
2026-01-05 07:31:10 ERROR Backup failed: disk full
END
</pre></td>
<td><pre>
[05/01/2026 07:31:10] Backup failed: disk full
INFO = 1
WARNING = 0
ERROR = 1
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. Try `"a b c d e".split(maxsplit=3)`. You get 4 pieces: `['a', 'b', 'c', 'd e']`. The last piece keeps the rest of the line, spaces included. Perfect for the message.
2. Four pieces can go straight into four variables: `date, time, level, message = ...`.
3. `.split()` can also cut at a separator you choose: `"2026-11-07".split("-")` gives `['2026', '11', '07']`.
4. You don't know how many lines will come, so read until `END`. The walrus from Level 01, exercise 07, fits here.
5. Look at sample 3: an `INFO` entry has the word `ERROR` in its message. `"ERROR" in line` would be fooled. Check the level, not the whole line.
6. Bonus: in Level 06 you'll read whole files into one string. Then `text.splitlines()` gives you the lines, like `.split()` gives you the words.

</details>

## ⚡ Challenge

Here you learn why logs write dates and times like `2026-11-07 09:01:13`: with a fixed width and zeros on the left, comparing the **text** gives the same answer as comparing the **time**. You also meet the `%` format, for percentages.

Rules: compare the times as text. Don't convert them to numbers.

### Input

The first line contains two times, **A** and **B** (`HH:MM:SS`, with A ≤ B), separated by a space. Then comes a log like in the main problem, ending with `END`. All entries are from the same day.

### Output

For each entry whose time is between A and B (both included), print `[HH:MM:SS] LEVEL message`. Then print `ERRORS = X of Y (Z%)`, where Y is the number of entries between A and B, X is how many of them are errors, and Z is the percentage of errors among them, with 1 decimal place. When Y is 0, the percentage is `0.0%`.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
09:00:00 09:30:00
2026-11-07 08:15:02 INFO Server started
2026-11-07 08:20:45 WARNING Disk at 85%
2026-11-07 09:01:13 ERROR Database connection lost
2026-11-07 09:01:20 INFO Retrying connection
2026-11-07 09:02:00 ERROR Timeout after 30 s
END
</pre></td>
<td><pre>
[09:01:13] ERROR Database connection lost
[09:01:20] INFO Retrying connection
[09:02:00] ERROR Timeout after 30 s
ERRORS = 2 of 3 (66.7%)
</pre></td>
</tr>
<tr>
<td><pre>
09:59:00 10:01:00
2026-11-07 09:58:59 INFO Job started
2026-11-07 09:59:30 ERROR Job crashed
2026-11-07 10:00:15 INFO Job restarted
2026-11-07 10:01:00 INFO Job running
2026-11-07 10:05:00 ERROR Job crashed again
END
</pre></td>
<td><pre>
[09:59:30] ERROR Job crashed
[10:00:15] INFO Job restarted
[10:01:00] INFO Job running
ERRORS = 1 of 3 (33.3%)
</pre></td>
</tr>
<tr>
<td><pre>
12:00:00 13:00:00
2026-11-07 08:15:02 INFO Server started
END
</pre></td>
<td><pre>
ERRORS = 0 of 0 (0.0%)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `"09:01:13" < "09:30:00"`, and then `"9:01:13" < "10:00:00"`. Why does the second one give the wrong answer? Remember `"10"` and `"9"` in exercise 11.
2. Chained comparisons work with text too: `a <= t <= b`.
3. `f"{2 / 3:.1%}"` gives `"66.7%"`: the `%` type multiplies by 100 and adds the sign.
4. Look at sample 3: 0 errors out of 0 entries. What happens when you divide by zero? (Level 01, exercise 07.)

</details>
