# 07 - Find the Word
t = input()
w = input()
check = ""
COUNT = t.count(w)
FIRST = t.find(w)
LAST = t.rfind(w)
if COUNT == 0:
    print("NOT FOUND")
else:
    print(
    f"COUNT = {COUNT}",
    f"FIRST = {FIRST}",
    f"LAST = {LAST}",
    sep="\n",end=""
        )
