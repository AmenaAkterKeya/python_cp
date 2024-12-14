# Problem Statement
# You need to take one non-negative integer (0 or greater than 0) value as input and tell if it is even or odd.
# See the sample input and output for more clarification.

# Sample Input

# 10
# 3

# Sample Output

# even
# odd

n = int(input())
if n >= 0 :
    if n==0:
        print("even")
    elif n%2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("negative integer")
