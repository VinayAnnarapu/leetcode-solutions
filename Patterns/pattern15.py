
# A
# BB
# CCC
# DDDD
# EEEEE

for i in range(1, 6):
    ch = chr(64 + i)   
    for j in range(i):
        print(ch, end="")
    print()