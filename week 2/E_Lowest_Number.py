# Problem Statement
# Question : Lowest Number (https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E)
 
n = int(input())
ar = list(map(int, input().split()))

# mn = ar[0]
# position = 0

# for i in range(n):
#     if mn > ar[i]:
#         mn = ar[i]
#         position = i
mn = min(ar)
position = ar.index(mn)

print(mn, position+1)
