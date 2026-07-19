
# 1
# 01
# 101
# 0101
# 10101

for i in range(1, 6):
    flag = i % 2
    for j in range(i):
        print(flag, end="")
        flag = 1 - flag   
    print()