#problem :https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/W

n = int(input())
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)
for i in range(n, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)




   