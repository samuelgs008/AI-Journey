# 05 - Greatest of Three
number_follows = int(input())
big = small = int(input())
for _ in range(number_follows - 1):
    n = int(input())
    if n > big:
        big = n
    elif n < small:
        small = n

print(f"GREATEST = {big}\nSMALLEST = {small}")
