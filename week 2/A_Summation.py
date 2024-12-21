# Problem Statement
# Question : Summation (https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/A)

n = int(input())  # Get the number of elements
ar = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += ar[i]

print( abs(sum))
