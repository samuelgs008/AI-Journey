# 06 - Password Strength · ⚡ Challenge
while True:
    s = input()
    if s.startswith("-"):
        if s[1:].isdecimal():
            break;
    elif s.isdecimal():
        break;
    print(f"{s} is not an integer")
s = int(s)
print(f"DOUBLE = {s * 2}")
