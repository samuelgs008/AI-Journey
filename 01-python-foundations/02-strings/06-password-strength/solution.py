# 06 - Password Strength
up = 0
low = 0
dig = 0
sym = 0
s = input()
for i in range(len(s)):
    if s[i].isupper(): up += 1
    elif s[i].islower(): low += 1
    elif s[i].isdigit(): dig += 1
    elif s[i].isalnum() == False: sym += 1
        
print(
    "UPPER = " + str(up),
    "LOWER = " + str(low),
    "DIGITS = " + str(dig),
    "SYMBOLS = " + str(sym),
    "STRONG" if up * low * dig * sym != 0 and len(s) >= 8 else "WEAK",
    sep="\n",end=""
        )