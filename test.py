n, m = map(int, input().split())
numbers = list(map(int, input().split()))
counter = 0 

for i in range(n):
    l = int(input())
    counter += 1
    for j in range(l,n):
        print(numbers[j])
        