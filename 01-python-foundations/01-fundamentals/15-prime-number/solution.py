# 15 - Prime Number
n = int(input())
print(f"{n} is ", end="")
if n < 2:
    print("not prime")
elif n == 2:
    print("prime")
elif n % 2 == 0:
    print("not prime")
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
