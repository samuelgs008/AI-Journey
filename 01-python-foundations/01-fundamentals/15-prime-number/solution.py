# 15 - Prime Number
n = int(input())
print(f"{n} is ",
      (n % n != 0) * "not ",
      "prime",
      sep=""
      )