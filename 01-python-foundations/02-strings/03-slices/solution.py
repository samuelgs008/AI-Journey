# 03 - Slices
w = input()
print(
    f"FIRST 3 = [{w[:3]}]",
    f"LAST 3 = [{w[-3:]}]",
    f"MIDDLE = [{w[1:(len(w) - 1)]}]",
    f"EVERY OTHER = [{w[::2]}]",
    sep="\n"
      )