# 14 - Grade Validator
total = 0
count = 0

while True:
    grade = float(input())
    if not (0 <= grade <= 10):
        print("invalid grade")
        continue
    total += grade
    count += 1
    if count == 2:
        print(f"AVERAGE = {total / count:.2f}")
        answer = 0
        while answer != 1 and answer != 2:
            print("new calculation (1-yes 2-no)")
            answer = int(input())
        if answer == 2:
            break
        total = 0
        count = 0
