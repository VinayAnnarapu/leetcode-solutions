#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *




for i in range(6):
    for s in range(6-i):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
    for k in range(i,0,-1):
        print("*",end="")
    print()
for i in range(6,0,-1):
    for s in range(6,i,-1):
        print(" ",end="")
    for j in range(1,i):
        print("*",end="")
    for k in range(i,0,-1):
        print("*",end="")
    print()