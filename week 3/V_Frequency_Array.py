# problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V
from collections import Counter
n, m = map(int, input().split())  
s = list(map(int, input().split()))  

counter = Counter(s)
for i in range(1, m + 1):
    print(counter[i] if i in counter else 0)