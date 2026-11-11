# 07 - Find the Word · ⚡ Challenge
t = "aaaa"
w = "aa"
i = 0
overlapping = 0
while (s := int(t.find(w, i))) >=0:
    print(s)
    
    i += s
    if i == 0:
        i += 1