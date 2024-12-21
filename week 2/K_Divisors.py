# Problem Statement
# Question : Divisors (https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/K)

n = int(input())
for i in range(1,n+1):
    if n % i == 0:
        print(i)
    