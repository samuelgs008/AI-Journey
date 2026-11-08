# 11 - Time Converter

A stopwatch only counts **seconds**, but people want to read hours, minutes and seconds. Read a duration in seconds and convert it.

Here you meet the two most useful operators in logic problems: `//` (integer division) and `%` (remainder).

## Input

The input contains an integer **S** (0 ≤ S ≤ 1000000), the duration in seconds.

## Output

Print `H:M:S`, where H is the hours, M the minutes and S the seconds. No leading zeros.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
556
</pre></td>
<td><pre>
0:9:16
</pre></td>
</tr>
<tr>
<td><pre>
1
</pre></td>
<td><pre>
0:0:1
</pre></td>
</tr>
<tr>
<td><pre>
140153
</pre></td>
<td><pre>
38:55:53
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. There are 3600 seconds in an hour and 60 in a minute.
2. `7 // 2` gives `3` (division without the decimal part) and `7 % 2` gives `1` (what is left over).
3. First take out the hours. Then work only with the seconds **left over**.

</details>

## My algorithm

How I worked out the math before writing the code:

![Diagram of converting seconds into hours, minutes and seconds](diagram.png)

## ⚡ Challenge

Now add **days** and show the clock the way a digital watch does, always with 2 digits. Here you learn `divmod()`, which does `//` and `%` at once, and how to fill numbers with zeros.

Rules: don't use `//` or `%` directly, only `divmod()`.

### Input

An integer **S** (0 ≤ S ≤ 10000000).

### Output

Print `Dd HH:MM:SS`. Days have no leading zeros, but hours, minutes and seconds always have 2 digits.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
556
</pre></td>
<td><pre>
0d 00:09:16
</pre></td>
</tr>
<tr>
<td><pre>
90061
</pre></td>
<td><pre>
1d 01:01:01
</pre></td>
</tr>
<tr>
<td><pre>
140153
</pre></td>
<td><pre>
1d 14:55:53
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Try `divmod(17, 5)` in the terminal. It gives two values at once, and you can store both: `q, r = divmod(17, 5)`.
2. `f"{5:02}"` gives `"05"`: width 2, filled with zeros.
3. A day has 86400 seconds.

</details>
