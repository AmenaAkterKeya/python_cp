# Problem Statement
# Question : Lucky Numbers (https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/I)

n = (input())
a  = int(n[0])
b  = int(n[1])
if a % b == 0 or b % a == 0:
    print("YES")
else:
    print("NO")