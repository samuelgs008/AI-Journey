# 04 - Fix the Typo · ⚡ Challenge
S = input()
crazy_s = ""
for i,ch in enumerate(S):
    crazy_s += ch.upper() if i % 2 == 0 else ch.lower()
print(crazy_s)