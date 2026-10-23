import math

total = 0

n = int(input("Enter number: "))

for x in range(1, n+1):
    cube = math.pow (x,3)
    print(cube, end = ",")
    total = total + cube