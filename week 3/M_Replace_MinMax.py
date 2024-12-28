# problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
n = int(input())
s = list(map(int, input().split())) 
mn = min(s)
mx = max(s)
mn_index = s.index(mn)
mx_index = s.index(mx)
s[mn_index], s[mx_index] = s[mx_index], s[mn_index]
print(*s)
