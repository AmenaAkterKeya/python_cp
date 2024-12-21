# Problem Statement
# Question : Searching (https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/B)

n = int(input())
ar = list(map(int, input().split()))
x = int(input())
found = False
for i in range(n):
    if ar[i] == x:
        print(i)
        found = True
        break

if found == False:
    print(-1)