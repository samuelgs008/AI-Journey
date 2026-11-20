# 18 - Log Analyzer

Every server, app and robot writes **logs**: one line for each thing that happened. When something breaks, someone has to read thousands of them. Write the program that does it for you.

## Input

Log lines, until a line with `END`. Blank lines must be ignored. Every log line has this format:

```
2026-11-19 08:15:02 [ERROR] payment: card declined
```

That's the date, the time, the level in brackets (`INFO`, `WARNING` or `ERROR`), the module, a colon and a message. All lines are from the same day and in time order. There is at least one log line.

## Output

1. `LINES = n`, the number of log lines.
2. One line for each level, **always** in the order `INFO`, `WARNING`, `ERROR` (even when the count is 0): the level left-aligned in 8 characters, the count right-aligned in 3, and the percentage of all lines right-aligned in 8 with 1 decimal place.
3. If there are no errors, print `NO ERRORS`. Otherwise:
   - `ERRORS BY MODULE:`, then each module with errors, from the most errors (ties: alphabetical order): 2 spaces, the module left-aligned in 10, the count
   - `ERRORS BY HOUR:`, then each hour that had errors, in order: 2 spaces, the hour and `h`, a space, and one `#` per error
   - `FIRST ERROR = time` and `LAST ERROR = time`
4. `LONGEST GAP = HH:MM:SS (time1 -> time2)`: the longest time between two lines that come one after the other (the first one if there's a tie). If there's only one line, skip it.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
2026-11-19 08:00:00 [INFO] app: started
2026-11-19 08:15:02 [ERROR] payment: card declined
2026-11-19 08:15:40 [WARNING] login: slow response

2026-11-19 08:16:10 [ERROR] payment: timeout
2026-11-19 09:40:10 [ERROR] login: wrong password
2026-11-19 09:41:00 [INFO] app: stopped
END
</pre></td>
<td><pre>
LINES = 6
INFO      2   33.3%
WARNING   1   16.7%
ERROR     3   50.0%
ERRORS BY MODULE:
  payment   2
  login     1
ERRORS BY HOUR:
  08h ##
  09h #
FIRST ERROR = 08:15:02
LAST ERROR = 09:40:10
LONGEST GAP = 01:24:00 (08:16:10 -> 09:40:10)
</pre></td>
</tr>
<tr>
<td><pre>
2026-11-19 23:58:00 [INFO] app: started
2026-11-19 23:59:59 [INFO] app: stopped
END
</pre></td>
<td><pre>
LINES = 2
INFO      2  100.0%
WARNING   0    0.0%
ERROR     0    0.0%
NO ERRORS
LONGEST GAP = 00:01:59 (23:58:00 -> 23:59:59)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `line.split(maxsplit=3)` cuts only at the first 3 spaces, so the message (which has spaces) stays in one piece. Unpack it into 4 variables.
2. `"[ERROR]".strip("[]")` removes the brackets. `.partition(":")` separates the module from the message.
3. A dictionary that starts as `{"INFO": 0, "WARNING": 0, "ERROR": 0}` keeps the levels in that order and already has the zeros. Dictionaries remember the order their keys were added.
4. The hour is just a slice of the time: `time[:2]`.
5. For the gap, turn each time into seconds: `h * 3600 + m * 60 + s` (`map(int, time.split(":"))` gives you the three numbers). Keep a list of `(seconds, time)` tuples.
6. Turning seconds back into `HH:MM:SS` is the time converter from Level 01: `//`, `%` and `:02`.
7. `.strip()` on a blank line gives `""`, which is "falsy". `if not line.strip(): continue` skips it.
8. Look at sample 1: the longest gap is not between two errors. It's between **any** two lines that come one after the other.

</details>
