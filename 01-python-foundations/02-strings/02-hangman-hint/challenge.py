# 02 - Hangman Hint · ⚡ Challenge
w = input()
k = int(input())

if k > len(w):
    print("OUT OF RANGE")
else:
    print("START = " + w[k - 1])
    print("END = " + w[-k])