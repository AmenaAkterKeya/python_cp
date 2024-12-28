# problem : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/F
n = int(input())
for _ in range(n):
    word = input()
    if len(word) < 10:
        print(word)
    else:
        a = word[0] + str(len(word) - 2) + word[-1]
        print(a)
