# Problem Statement
# Question : Next Alphabet (https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/C)

alpha = (input())
if alpha == 'z':
    print('a')
else:
    n = ord(alpha)+1
    print(chr(n))
