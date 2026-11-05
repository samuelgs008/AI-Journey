# 14 - Grade Validator
total = 0
count = 0
grade_validator = True

while grade_validator:
    n = float(input())
    if(n < 0 or n > 10):
        print("invalid grade")
        continue
    total += n
    count += 1
    if count == 2:
        print(f"AVERAGE = {float(total / count):.2f}")
        n = 0
        while n != 1 and n != 2:
            print("new calculation (1-yes 2-no)")
            n = int(input())

        if n == 1:
            count = 0
            total = 0
        elif n == 2:
            grade_validator = False