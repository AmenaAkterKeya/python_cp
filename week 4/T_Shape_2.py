#problem :https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/T
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    # Print stars
    print('*' * (2 * i - 1))
