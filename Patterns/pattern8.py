# *********
#  *******
#   *****
#    ***
#     *

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i):
        print("*",end="")
    for k in range(i,0,-1):
        print("*",end="")
    print()


