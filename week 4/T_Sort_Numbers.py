# problem: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/T
def sorting(x,y,z):
    ar = [x, y, z]
    ar.sort()  
    return ar  
x , y ,z= map(int,input().split())
arr = [x,y,z]
result = sorting(x, y, z)
for num in result:
    print(num)
    
print()
for nums in arr:
    print(nums)