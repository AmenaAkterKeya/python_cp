# problem : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J
from collections import Counter
S = input().strip()
counter = Counter(S)

for char in sorted(counter):
    print(f"{char} : {counter[char]}")
