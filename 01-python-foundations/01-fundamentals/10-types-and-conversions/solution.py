# 10 - Types and Conversions
A, B, C = int(input()), float(input()), input()
print(
    f"{A = !s} -> {type(A).__name__}",
    f"{B = !s} -> {type(B).__name__}",
    f"{C = !s} -> {type(C).__name__}",
    f"{A + B = !s} -> {type(A + B).__name__}",
    f"{C * 2 = !s}",
    f"{int(C) * 2 = !s}",
    f"{bool(A) = !s}",
    sep="\n"
)
