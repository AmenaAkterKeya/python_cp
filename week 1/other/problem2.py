# Problem Statement
# You need to take two integer values as input and show the summation, subtraction, multiplication and division in the given format below.

# For example:
# Inputs are 5 and 2
# Then you’ll give output as:
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.50

a ,b  = map (int,input().split())
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')