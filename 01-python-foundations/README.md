# Phase 1 — Python foundations

From Level 02 on, each exercise is **one** problem with **one** file, `main.py`, and mixes everything learned so far. The hints are hidden in each README: I try on my own first. In Level 01, `solution.py` holds the challenge version (the main versions are in the git history), except in 16, which has both files.

🚩 = has a bug, must fix it · 🔧 = works, but can be refactored · <img src="../assets/excalidraw-logo.png" alt="Excalidraw" width="16"> = has an algorithm drawing

## Level 01: Fundamentals

| # | Exercise | What you learn | Solved | Challenge |
|----|---|---|:---:|:---:|
| 01 | [Hello World](01-fundamentals/01-hello-world/) | `print()`, text between quotes · ⚡ `*` with text, `"\n"`, the `end` parameter | ✅ | ✅ |
| 02 | [Greeting](01-fundamentals/02-greeting/) | `input()`, variables, f-strings · ⚡ `input()` inside an f-string, when `int()` isn't needed | ✅ | ✅ |
| 03 | [Simple Calculator](01-fundamentals/03-simple-calculator/) | `int()`, `+` `-` `*` `/`, 2 decimal places with `:.2f` · ⚡ two variables in one line, `"\n"` in an f-string | ✅ | ✅ |
| 04 | [Even or Odd](01-fundamentals/04-even-or-odd/) | `%` (remainder), `if` / `else`, `==` · ⚡ the one-line `if`, `%` with negative numbers | ✅ | ✅ |
| 05 | [Greatest of Three](01-fundamentals/05-greatest-of-three/) | `if` / `elif` / `else`, `and`, comparisons · ⚡ the "greatest so far" pattern, `for _ in range(N)` | ✅ | ✅ |
| 06 | [Multiplication Table](01-fundamentals/06-multiplication-table/) | `for`, `range()` · ⚡ nested loops, aligning columns with f-strings | ✅ | ✅ |
| 07 | [Sum Until Zero](01-fundamentals/07-sum-until-zero/) | `while`, `break`, a running total · ⚡ the walrus `:=`, avoiding division by zero | ✅ | ✅ |
| 08 | [Count Vowels](01-fundamentals/08-count-vowels/) | looping over text, `in`, `.lower()`, counters · ⚡ `True` and `False` as numbers, `len()`, `.replace()` | ✅ | ✅ |
| 09 | [🏆 FizzBuzz](01-fundamentals/09-challenge-fizzbuzz/) | the order of `if` / `elif`, multiples with `%` · ⚡ building a word piece by piece, `"Fizz" * True`, `"" or n` | ✅ | ✅ |
| 10 | [Types and Conversions](01-fundamentals/10-types-and-conversions/) | `type()`, `int()`, `float()`, `str()`, `bool()` · ⚡ the f-string `=` debug trick, `!s`, `sep` | ✅ | ✅ |
| 11 | [Time&nbsp;Converter](01-fundamentals/11-time-converter/)&nbsp;[<img src="../assets/excalidraw-logo.png" alt="Algorithm drawing" width="16" align="center">](01-fundamentals/11-time-converter/README.md#my-algorithm) | `//` (integer division) and `%` (remainder) · ⚡ `divmod()`, zeros on the left with `:02` | ✅ | ✅ |
| 12 | [Countdown](01-fundamentals/12-countdown/) | `range()` counting down (negative step) · ⚡ the unpacking operator `*`, `sep` | ✅ | ✅ |
| 13 | [Star Triangle](01-fundamentals/13-star-triangle/) | nested loops, `print(..., end="")` · ⚡ finding the formula of a pattern, `"*" * i` | ✅ | ✅ |
| 14 | [Grade Validator](01-fundamentals/14-grade-validator/) | validating input with `while`, `continue`, chained comparisons (`0 <= g <= 10`) · ⚡ a program that keeps running (`while True`), a loop inside another loop | ✅ | ✅ |
| 15 | [Prime Number](01-fundamentals/15-prime-number/) | `break`, a flag variable · ⚡ fast code (testing only up to √N), `for ... else` | ✅ | ✅ |
| 16 | [🏆&nbsp;Reverse&nbsp;Number](01-fundamentals/16-challenge-reverse-number/)&nbsp;[<img src="../assets/excalidraw-logo.png" alt="Excalidraw drawing" width="16" align="center">](01-fundamentals/16-challenge-reverse-number/README.md#my-algorithm) | taking digits apart with `//` and `%`, `while` until 0 · ⚡ palindromes, saving a copy before the loop, edge cases | ✅ | ✅ |

## Level 02: Strings + Data Structures

| # | Exercise | What you learn | Solved |
|---|---|---|:---:|
| 01 | [Ticket Printer](02-strings-and-data-structures/01-ticket-printer/) | quotes inside text, escapes, raw strings (the `\t` trap in Windows paths), triple-quoted f-strings, `len()`, centering with `^` and a variable width, Unicode box characters | ✅ |
| 02 | [Word Detective](02-strings-and-data-structures/02-word-detective/) | `.find()` with a start, slices, immutability (building a new string), searching while ignoring case | ⬜ |
| 03 | [Username Maker](02-strings-and-data-structures/03-username-maker/) | cleaning messy input, `.split()`, `.partition()`, `.isalpha()`, `.isdigit()`, `.isalnum()`, `.count()`, `.startswith()`/`.endswith()`, validating an email step by step | ⬜ |
| 04 | [Shopping List](02-strings-and-data-structures/04-shopping-list/) | first lists: `append`, `insert`, `remove`, `pop`, `reverse`, `in`, indexes (also negative), slices, `", ".join()`, a command loop | ⬜ |
| 05 | [Grade Book](02-strings-and-data-structures/05-grade-book/) | `min`/`max`/`sum`, `sort()` vs `sorted()`, median, trimmed average, `.copy()`, percentages with `:.1%` | ⬜ |
| 06 | [Word Wrap](02-strings-and-data-structures/06-word-wrap/) | building lines from words, the "don't forget the last one" bug, padding with a variable width | ⬜ |
| 07 | [Secret Code](02-strings-and-data-structures/07-secret-code/) | `ord()`/`chr()`, Unicode, wrapping around with `%`, the Vigenère and Caesar ciphers, building with a list and `"".join()` | ⬜ |
| 08 | [The Copy Trap](02-strings-and-data-structures/08-the-copy-trap/) | lists of lists (grids), mutability, why `[row] * H` breaks, `is`, shallow vs deep copies | ⬜ |
| 09 | [Tic-Tac-Toe Judge](02-strings-and-data-structures/09-tic-tac-toe-judge/) | walking a grid by rows, columns and diagonals, comparing lists, `in` with lists, the order of checks | ⬜ |
| 10 | [Map Points](02-strings-and-data-structures/10-map-points/) | tuples, unpacking in a `for`, swapping with `a, b = b, a`, sorting by several things with tuples | ⬜ |
| 11 | [Word Counter](02-strings-and-data-structures/11-word-counter/) | first dictionaries, counting with `.get()`, `.items()`, sorting counts with `(-count, word)`, fill characters | ⬜ |
| 12 | [Phone Book](02-strings-and-data-structures/12-phone-book/) | a dictionary of lists, a reverse-lookup dictionary, keeping two dictionaries in sync, `.pop()` on dictionaries | ⬜ |
| 13 | [Anagram Groups](02-strings-and-data-structures/13-anagram-groups/) | grouping (key → list), choosing a good key, why lists can't be keys, `.values()` | ⬜ |
| 14 | [Unique Visitors](02-strings-and-data-structures/14-unique-visitors/) | sets: removing duplicates, fast `in`, union `\|`, intersection `&`, difference `-` | ⬜ |
| 15 | [Ranking Table](02-strings-and-data-structures/15-ranking-table/) | `zip`, `enumerate(start=1)`, positions with ties, ▲▼ moves, a table with separators and percentages | ⬜ |
| 16 | [Comprehension Gym](02-strings-and-data-structures/16-comprehension-gym/) | list, set and dict comprehensions, filters, `if`/`else` inside them, nested comprehensions | ⬜ |
| 17 | [Student Records](02-strings-and-data-structures/17-student-records/) | a list of dictionaries (the shape of JSON), nested access, `.setdefault()`, grouping records | ⬜ |
| 18 | [Log Analyzer](02-strings-and-data-structures/18-log-analyzer/) | parsing log files, `maxsplit`, counting by level, module and hour, time gaps in seconds | ⬜ |
| 19 | [Sales Report](02-strings-and-data-structures/19-sales-report/) | parsing CSV with columns in any order, a column → index dictionary, skipping broken rows, a money report | ⬜ |
| 20 | [🏆 Inventory](02-strings-and-data-structures/20-challenge-inventory/) | everything together: nested dictionaries, sets, a history of tuples, an `UNDO` stack, a report table | ⬜ |
