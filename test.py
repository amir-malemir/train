n = int(input())
month = list(map(int , input().split()))
counter = 0
sum_number = 0
month.sort(reverse=True)
print(month)

for i in range(11):
    counter = counter + 1
    sum_number = sum_number + month[i]
    print(sum_number)
    if sum_number >= n:
        print(counter)
        break
    else:
        print('no')
        