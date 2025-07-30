n, l = map(int, input().split())
fanos_l = list(map(int, input().split()))
middle = 0

fanos_l.sort()

if n > 1:    
    for i in range(n-1):
        calcu = fanos_l[i+1] - fanos_l[i]
        if calcu > middle:
            middle = calcu
middle = middle/ 2
first_l = fanos_l[0] - 0
last_l = l - fanos_l[n-1]
output = max(first_l, last_l, middle)
print(output)