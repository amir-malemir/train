n = int(input())
month = input()
counter = 0
month.sort(reversed = True)

for i in range(12):
    counter = counter + 1
    sum_number = month[i+1] + month[i]
    if sum_number == 0:
        print(no)
    elif sum_number > n:
        print(counter)