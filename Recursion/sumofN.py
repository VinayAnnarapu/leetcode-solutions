#Paramterized Recursion
# Parameterized Recursion is a type of recursion where we pass additional parameters
# to the recursive function to keep track of intermediate results or states, instead of relying solely on return values.

def sumofN(n,sum):
    if(n<0):
        print(sum)
        return
    sumofN(n-1,sum+n)


# sumofN(5,0)

# Functional recursion:
# Functional recursion is a type of recursion where a function directly calls itself to solve a problem by breaking
# it down into smaller instances of the same problem, and returns a value to its caller.



def sumofN(n):
    if(n==0):
        return 0
    return n+sumofN(n-1)

print(sumofN(4))