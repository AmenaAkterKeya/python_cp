# Problem Statement

# You will be given a positive integer N, you need to print from 1 to N and besides the value, print Yes or No. Print Yes if the value is divisible by 5 and print No otherwise.

# Input Format

# Input will contain a positive integer N.
# Constraints

# 1 <= N <= 1000
# Output Format

# Output as mentioned in the question. See the sample input output for more clarifications. Put a new line after every line.

# Sample Input 1

# 5
# Sample Output 1

# 1 No
# 2 No
# 3 No
# 4 No
# 5 Yes

n = int(input())
for i in range (1,n+1):
    if i % 5 != 0:
        print(i , "No")
    else :
        print(i, "Yes")