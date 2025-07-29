n, l = map(int, input().split())
fanos_l = list(map(int, input().split()))
output = 0
fanos_l.sort()

for i in range(n):
    num1 = fanos_l[i+1]
    num2 = fanos_l[i]
    calcu = num1 - num2 
    if calcu > output:
        output = calcu
print(output/2)  