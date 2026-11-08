# 02 - Hangman Hint

w = input()
length = len(w)
print(w[0] + "_" * (length - 2) + (w[-1] if length > 1 else ""))
print("LENGTH = " + str(length))