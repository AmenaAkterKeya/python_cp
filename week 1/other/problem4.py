# Problem Statement
# You need to take one integer value as input and tell if the value is positive or negative or zero.
# See the sample input and output for more clarification.

# Sample Input

# 10
# -50
# 0

# Sample Output

# positive
# negative
# zero

n = int(input())
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
