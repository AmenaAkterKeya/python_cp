# problem : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/D
s = input()  
p = input()  

print(len(s), len(p))

print(s + p)

temp = s[0]
s = p[0] + s[1:]  
p = temp + p[1:] 


print(s, p)
