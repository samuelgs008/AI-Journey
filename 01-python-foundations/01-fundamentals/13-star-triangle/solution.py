# 13 - Star Triangle
n = int(input())
for line in range(1, n + 1):
    print(" " * (n - line) + "*" * (line * 2 - 1),
    end="\n"
    )


#for tower in range(n,0,-1):
#    print(" " * (tower - 1), end="")
#    i += 2
#    print("*" * (i))
     