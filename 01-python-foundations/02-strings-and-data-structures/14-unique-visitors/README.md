# 14 - Unique Visitors

A website logs the name of each visitor every day, with lots of repeats. Answer the questions every product team asks: how many **unique** people came? Who comes back? Who is new? **Sets** answer all of this in one line each.

## Input

The first line contains **N**, the number of days (2 ≤ N ≤ 30). Then come N lines, one per day, each with the visitors' names separated by spaces. A name can appear many times on the same day. Uppercase and lowercase don't matter: work with every name in lowercase.

## Output

```
DAY 1 = <unique visitors that day> unique
DAY 2 = ...
...
EVERY DAY = <names that came on every day>
ONE DAY ONLY = <names that came on exactly one day>
NEW ON THE LAST DAY = <names that came on the last day and never before>
ALL = <unique visitors over all the days> unique
```

Names in a list are in alphabetical order, separated by `, `. If a list is empty, print `NONE`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
3
Ana bia ana Caio
bia caio DAVI
bia Ana eva
</pre></td>
<td><pre>
DAY 1 = 3 unique
DAY 2 = 3 unique
DAY 3 = 3 unique
EVERY DAY = bia
ONE DAY ONLY = davi, eva
NEW ON THE LAST DAY = eva
ALL = 5 unique
</pre></td>
</tr>
<tr>
<td><pre>
2
zoe
zoe
</pre></td>
<td><pre>
DAY 1 = 1 unique
DAY 2 = 1 unique
EVERY DAY = zoe
ONE DAY ONLY = NONE
NEW ON THE LAST DAY = NONE
ALL = 1 unique
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `set(["ana", "bia", "ana"])` gives `{"ana", "bia"}`: duplicates disappear. `set("ana bia ana".split())` does it straight from a line.
2. Sets have no order and no indexes, but `in` is super fast on them, even with a million items.
3. The set operators: `a | b` (union: in either), `a & b` (intersection: in both), `a - b` (difference: in `a` but not in `b`). Try them in the terminal.
4. A list of sets, one per day, keeps everything organized.
5. "Every day": start with a **copy** of the first day and keep `&=` with each day. Remember exercise 08: without `.copy()` you change day 1 itself.
6. "One day only" is a counting job: a dictionary from exercise 11, counting in how many days each name appears.
7. "New on the last day": the last day `-` the union of all the days before it. `days[:-1]` is every day except the last.
8. `sorted()` works on sets and gives a list back. Then `", ".join(...)`.

</details>
