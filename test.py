n, l = map(int, input().split())
fanos_l = list(map(int, input().split()))
output = 0
fanos_l.sort()

for i in range(n):
    num1 = fanos_l[i+1]
    num2 = fanos_l[i]
    print(f'num1 --> {num1}')
    print(f'num2 --> {num2}')
    calcu = num1 - num2 
    if calcu > output:
        output = calcu
        print(f'output --> {output/2}')