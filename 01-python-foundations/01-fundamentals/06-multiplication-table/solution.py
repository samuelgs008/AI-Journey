# 06 - Multiplication Table

n = int(input())
#columns
for row in range(1,n + 1):
    for col in range(1,n + 1):
        print(f"{row * col:4}",end="")
    print("")
    
    