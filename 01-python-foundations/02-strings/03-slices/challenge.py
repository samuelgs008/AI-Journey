# 03 - Slices · ⚡ Challenge
w = input()

print(
    f"REVERSED = {w[(len(w))::-1]}",
    f"PALINDROME = {w.lower() == w[len(w)::-1].lower()}",
    "MIRROR = " + w + w[::-1][1:],
    sep="\n",end=""
    )