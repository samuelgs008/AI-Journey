# 03 - Username Maker

A sign-up form sends you messy data. Check it, clean it and create a username for each person. This is real work: data from people is never clean.

## Input

The first line contains an integer **N** (1 ≤ N ≤ 50). Then come N lines in the format `full name;year;email`. There may be extra spaces anywhere. Every name has at least two words, and names may contain things that are not letters (`'`, `-`, digits).

## Output

For each line, check the fields in this order and print **one** line:

1. If the year is not exactly 4 digits, print `INVALID YEAR`.
2. Otherwise, if the email is not valid, print `INVALID EMAIL`.
3. Otherwise, print the username: the **first** name, a dot, the **last** name and the last two digits of the year. All lowercase, keeping only letters.

An email is valid when **all** of these are true:

- it has exactly one `@`
- the part before the `@` is not empty, has only letters, digits, `.` and `_`, and does not start or end with `.`
- the part after the `@` has at least one `.`, does not start or end with `.`, has no `..`, and has only letters, digits, `.` and `-`

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
4
  Ana   Maria LIMA ;1998; ana.lima@mail.com
Pedro O'Neil-Costa;1985;pedro_oc@work.com.br
Bia Souza;98;bia@mail.com
Carlos Melo;2001;carlos@@mail.com
</pre></td>
<td><pre>
ana.lima98
pedro.oneilcosta85
INVALID YEAR
INVALID EMAIL
</pre></td>
</tr>
<tr>
<td><pre>
3
Leo Dias;2003;.leo@mail.com
Mia Rocha;2000;mia@mail
Joao  Paulo  Alves2;1990;jp@my-site.org
</pre></td>
<td><pre>
INVALID EMAIL
INVALID EMAIL
joao.alves90
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. `"a;b;c".split(";")` gives three pieces, and `name, year, email = ...` puts them in three variables at once (unpacking).
2. `.split()` with **no** argument splits on any amount of spaces and ignores spaces at the start and end. Then `[0]` is the first word and `[-1]` the last.
3. Keep only letters: loop over the characters and add the ones where `.isalpha()` is `True`.
4. `.count("@")` tells you how many `@` there are. Then `.partition("@")` cuts the email into before, `"@"` and after.
5. `.startswith()`, `.endswith()` and `in` cover most of the email rules.
6. For "only these characters": loop over the characters and use `c.isalnum() or c in "._"`. A flag variable (`ok = True`, then `ok = False` when a rule breaks) keeps the code simple.
7. Test the rules one at a time. Write a few bad emails of your own and check that each one is caught for the right reason.

</details>
