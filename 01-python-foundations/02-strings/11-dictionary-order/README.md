# 11 - Dictionary Order

Strings can be compared with `<`, `>` and `==`, just like numbers. Python puts them in alphabetical order... almost. There are a few surprises.

Read two words and print them in the order Python sorts them.

## Input

Two lines, each with a word.

## Output

Print the two words, one per line: first the one that is **smaller** for Python, then the other one.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
banana
apple
</pre></td>
<td><pre>
apple
banana
</pre></td>
</tr>
<tr>
<td><pre>
apple
Zebra
</pre></td>
<td><pre>
Zebra
apple
</pre></td>
</tr>
<tr>
<td><pre>
10
9
</pre></td>
<td><pre>
10
9
</pre></td>
</tr>
<tr>
<td><pre>
card
car
</pre></td>
<td><pre>
car
card
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `"apple" < "banana"` is `True`. Python compares the first letters. If they are equal, it compares the second ones, and so on.
2. Sample 2 looks wrong, doesn't it? Every character has a number, its **code**: try `ord("Z")` and `ord("a")`. Python compares those codes, and all uppercase letters come before the lowercase ones.
3. Sample 3: `"10"` and `"9"` are **text**, not numbers. The first characters, `"1"` and `"9"`, already decide.
4. Sample 4: when one word is the start of the other, the shorter one comes first.
5. Bonus, two classic bugs: `"5" == 5` is `False`, because text is never equal to a number (and `input()` always gives text). And compare text with `==`, never with `is`: `is` checks if two values are the **same object** in memory, not if they are equal. It may work in the terminal and fail in a program.

</details>

## ⚡ Challenge

Here you learn to sort like a real dictionary, **ignoring case**, without losing the original spelling. And you'll see that the "greatest so far" pattern from Level 01 works with text too.

Rules: no `min()`, no `max()` and no lists.

### Input

The first line contains an integer **N** (1 ≤ N ≤ 100). Then come N words, one per line. No two words are equal when you ignore case.

### Output

Print two lines: `FIRST = X` and `LAST = Y`, the words that come first and last in dictionary order, ignoring uppercase and lowercase. Print them exactly as they were typed.

### Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4
banana
Zebra
apple
Mango
</pre></td>
<td><pre>
FIRST = apple
LAST = Zebra
</pre></td>
</tr>
<tr>
<td><pre>
1
Python
</pre></td>
<td><pre>
FIRST = Python
LAST = Python
</pre></td>
</tr>
<tr>
<td><pre>
3
car
Card
CAB
</pre></td>
<td><pre>
FIRST = CAB
LAST = Card
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints</summary>

1. Level 01, exercise 05 challenge: the first word you read is the perfect starting value for both.
2. **Compare** the lowercase versions, but **save** the original word.
3. After you solve it, try `min("banana", "Zebra", "apple")` and then `min("banana", "Zebra", "apple", key=str.lower)` in the terminal. You'll understand `key=` in Level 04.

</details>
