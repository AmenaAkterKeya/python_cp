# Problem Statement
# Question : Positions in array (https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/D)

n = int(input())
ar = list(map(int, input().split()))
# A = []
# index = 0
# for i in range(n):
#     if ar[i] <= 10:
#         index = i
#         A.append(ar[i])
#         print(A[index])
for i in range(n):
    if ar[i] <= 10:
        print(f"A[{i}] = {ar[i]}")