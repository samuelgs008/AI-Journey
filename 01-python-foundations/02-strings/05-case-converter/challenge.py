# 05 - Case Converter · ⚡ Challenge
s = input()
for i in range(len(s)):
    print(
        s[i].upper() if s[(i-1)] == " " or i == 0 else s[i].lower(),
        end=""
        )
