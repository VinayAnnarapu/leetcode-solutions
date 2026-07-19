#     *
#    ***
#   *****
#  *******
# *********



for i in range(6):
    for s in range(6-i):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
    for k in range(i,0,-1):
        print("*",end="")
    print()

