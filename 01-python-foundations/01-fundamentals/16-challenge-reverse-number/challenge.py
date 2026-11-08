# 16 - 🏆 Final Challenge: Reverse Number · ⚡ Challenge
n = int(input())  # 0 ≤ N ≤ 1000000000
original = n  # save a copy: the loop below destroys n
rev = 0
digit_count = 0
while n > 0:
    digit = n % 10          # take the last digit
    digit_count += 1
    rev = rev * 10 + digit  # push rev left, put the digit on the right
    n = n // 10             # remove the last digit from n

if original == 0:
    digit_count = 1  # the loop never runs for 0, but 0 still has 1 digit

print(f"DIGITS = {digit_count}",
      "PALINDROME" if original == rev else "NOT PALINDROME",
      sep="\n")
