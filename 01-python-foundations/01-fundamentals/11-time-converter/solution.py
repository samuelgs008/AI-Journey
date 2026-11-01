# 11 - Time Converter
S = int(input())
D, Rest = divmod(S, 86400) # 86400 seconds = 1 day  (The left over values are less than 1 day)
H, Rest = divmod(Rest, 3600) #3600 seconds = 1 hour
M, S = divmod(Rest, 60) #60 seconds = 1 minute

print(f"{D}d {H:02}:{M:02}:{S:02}")


