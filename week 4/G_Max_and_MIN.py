# problem: https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/G
def sorting(x):
    mn = min(x)
    mx = max(x)
    return mn, mx
n = int(input())
x = list(map(int,input().split()))
print(*sorting(x))