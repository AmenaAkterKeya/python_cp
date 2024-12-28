# problem: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/I

s= input()
a = reversed(s)
if s == ''.join(a) :
    print("YES")
else:
    print("NO")