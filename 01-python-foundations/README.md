# Phase 1 — Python foundations

From Level 02 on, each exercise has two files: `solution.py` for the main problem and `challenge.py` for the ⚡ Challenge. In Level 01, `solution.py` holds the challenge version (the main versions are in the git history), except in 16, which has both files.

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

## Level 02: Strings

| # | Exercise | What you learn | Solved | Challenge |
|---|---|---|:---:|:---:|
| 01 | [Quotes and Escapes](02-strings/01-quotes-and-escapes/) | `'` vs `"`, escape sequences (`\"`, `\\`, `\n`, `\t`), braces in f-strings · ⚡ triple-quoted and raw strings | ✅ | ✅ |
| 02 | [Hangman Hint](02-strings/02-hangman-hint/) | `len()`, indexes, negative indexes, `+` and `*` with text, `str()` · ⚡ counting from 1 vs from 0, `IndexError` | ✅ | ✅ |
| 03 | [Slices](02-strings/03-slices/) | `[start:stop:step]`, slices never crash · ⚡ negative steps, reversing, palindromes | ✅ | ✅ |
| 04 | [Fix the Typo](02-strings/04-fix-the-typo/) | immutability, rebuilding with slices · ⚡ building a string in a loop, `enumerate()` | ✅ | ✅ |
| 05 | [Case Converter](02-strings/05-case-converter/) | methods: `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`, `.casefold()` · ⚡ your own `title()`, the previous-character pattern | ✅ | ⬜ |
| 06 | [Password Strength](02-strings/06-password-strength/) | `.isupper()`, `.islower()`, `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()` · ⚡ validating before `int()`, `.isdecimal()`, `.startswith()`, `.endswith()` | ⬜ | ⬜ |
| 07 | [Find the Word](02-strings/07-find-the-word/) | `in`, `.count()`, `.find()`, `.rfind()`, `.index()` · ⚡ overlapping matches, `.find()` with a start | ⬜ | ⬜ |
| 08 | [Clean the Data](02-strings/08-clean-the-data/) | `.replace()`, `.strip()`, `.lstrip()`, `.rstrip()`, chaining · ⚡ the `.strip()` trap, `.removeprefix()`, `.removesuffix()`, `!r` | ⬜ | ⬜ |
| 09 | [Sum of a Line](02-strings/09-sum-of-a-line/) | `.split()`, the `map(int, input().split())` recipe · ⚡ `.join()`, `sum()` | ⬜ | ⬜ |
| 10 | [Initials](02-strings/10-initials/) | split, transform, glue · ⚡ `.rsplit()`, `maxsplit`, `.partition()`, `.rpartition()`, unpacking | ⬜ | ⬜ |
| 11 | [Dictionary Order](02-strings/11-dictionary-order/) | comparing text, character codes · ⚡ ignoring case, "greatest so far" with text | ⬜ | ⬜ |
| 12 | [🏆 Caesar Cipher](02-strings/12-challenge-caesar-cipher/) | `ord()`, `chr()`, Unicode, bytes · ⚡ `str.maketrans()`, `.translate()` | ⬜ | ⬜ |
| 13 | [Receipt](02-strings/13-receipt/) | format spec: width, alignment, `,` separator, precision · ⚡ fill characters, dynamic width, `.center()`, `.ljust()`, `.rjust()`, `.zfill()`, old `%` and `.format()` | ⬜ | ⬜ |
| 14 | [Log Reader](02-strings/14-log-reader/) | reading until `END`, `.split()` with a separator and `maxsplit`, real-looking data · ⚡ comparing times as text, the `%` format | ⬜ | ⬜ |
| 15 | [🏆 Run-Length Encoding](02-strings/15-challenge-run-length-encoding/) | compressing text: everything together · ⚡ parsing text, numbers with many digits | ⬜ | ⬜ |
