n = int(input())
month = list(map(int , input().split()))
counter = 0
month.sort(reverse=True)

for i in range(11):
    counter = counter + 1
    sum_number = month[i+1] + month[i]
    print(sum_number)
    if sum_number >= n:
        print(counter)
    else:
        print('no')
        