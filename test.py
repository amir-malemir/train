n, t = map(int, input().split())
spend_time = list(map(int, input().split()))
read_book = 0
counter = 0
i = 0

for i in range(n):
    sum_books = 0
    
    counter += 1
    print(' for clear !!!!!!!!')
    for j in spend_time:
        print(spend_time[counter])
        # print(f'counter {counter}')
        # print(f'j {j}')
        # sum_books += spend_time[counter-1]
        # print (f'in secound for : {sum_books}')