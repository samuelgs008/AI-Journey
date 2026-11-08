# 07 - Sum Until Zero
total = 0
count = 0
while (n := int(input())) != 0:
    total += n
    count += 1

print(f"SUM = {total}",
      f"COUNT = {count}",
      f"AVERAGE = {total / count if count != 0 else 0:.2f}",
      sep="\n", end=""
      )
