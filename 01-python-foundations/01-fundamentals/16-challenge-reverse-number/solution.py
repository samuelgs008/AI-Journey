# 16 - 🏆 Final Challenge: Reverse Number



n = int(1234) # 0 ≤ N ≤ 1000000000
rev = 0
digit_sum = 0

while n > 0:
    digit = n % 10          # take the last digit
    digit_sum += digit      # 
    rev = rev * 10 + digit  # push rev left, put the digit on the right
    n = n // 10              # remove the last digit from n
             
print(
    f"REVERSED = {rev}",
    f"DIGIT SUM = {digit_sum}",
    sep="\n",end=""
    )