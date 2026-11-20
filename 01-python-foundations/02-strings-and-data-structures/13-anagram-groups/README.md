# 13 - Anagram Groups

`listen` and `silent` use the same letters: they're **anagrams**. Group the words that are anagrams of each other. The secret is choosing the right dictionary **key**. Grouping is the brother of counting: instead of `key → number`, you have `key → list`.

## Input

One line of words separated by spaces, in any mix of uppercase and lowercase.

## Output

Uppercase and lowercase don't matter: work with every word in lowercase. If the same word appears more than once, it only counts once.

Print each group that has **at least 2** different words, in the format `word1, word2, word3 (n)`:

- the words inside a group are in alphabetical order
- the groups are in the alphabetical order of their first word

Then print `BIGGEST GROUP = word`: the first word of the biggest group. If there's a tie, use the group that was printed first.

If there are no groups, print only `NO ANAGRAMS`.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
listen Silent enlist google tinsel stone Notes onset cat act tac
</pre></td>
<td><pre>
act, cat, tac (3)
enlist, listen, silent, tinsel (4)
notes, onset, stone (3)
BIGGEST GROUP = enlist
</pre></td>
</tr>
<tr>
<td><pre>
one two three
</pre></td>
<td><pre>
NO ANAGRAMS
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. What do `listen`, `silent` and `enlist` have in common? Try `sorted("listen")` and `sorted("silent")` in the terminal.
2. `sorted()` on a string gives a list of letters. `"".join(...)` turns it back into a string like `"eilnst"`. That's your key: every anagram gets the **same** key.
3. Lists can't be dictionary keys (they can change). Strings and tuples can. That's why you join the letters.
4. The grouping pattern: `if key not in groups: groups[key] = []`, then `groups[key].append(word)`.
5. Before appending, check that the word isn't already in its group. Otherwise a repeated word would count twice.
6. `groups.values()` gives you just the lists. Keep the ones with 2+ words, sort the words inside each one, then sort the list of groups. Lists are compared item by item, like tuples, so that sorts them by their first word.
7. `google` is alone in its group, so it doesn't show up.

</details>
