#problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/J
n = int(input())
ar =  list(map(int,input().split()))
mn = min(ar)
cnt = 0
for i in range(n):
    if(ar[i]== mn):
        cnt+=1

if cnt % 2 != 0:
    print("Lucky")
else:
    print("Unlucky")