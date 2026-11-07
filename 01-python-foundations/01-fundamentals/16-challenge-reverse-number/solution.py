# 16 - 🏆 Final Challenge: Reverse Number



n = int(input()) # 0 ≤ N ≤ 1000000000
S_input = n
rev = 0
digit_count = 0
digit_sum = 0
while n > 0:
    digit = n % 10          # take the last digit
    digit_sum += digit
    digit_count += 1
    rev = rev * 10 + digit  # push rev left, put the digit on the right
    n = n // 10              # remove the last digit from n

print(
    f"Solution:",
    f"REVERSED = {rev}",
    f"DIGIT SUM = {digit_sum}"
    f"\n",
    f"Challenger Solution:",
    f"DIGITS = {digit_count}",
    f"{"PALINDROME" if S_input == rev else "NOT PALINDROME"}",
    sep="\n",end=""
    )