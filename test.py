n = int(input())
month = list(map(int , input().split()))
counter = 0
sum_number = 0
month.sort(reverse=True)
for i in range(11):
    counter = counter + 1
    sum_number = sum_number + month[i]
    if sum_number >= n:
        print(counter)
        break
    elif n == 0:
        print(1)
        break
    elif i == 11 or counter == 0:
        print('-1')
        