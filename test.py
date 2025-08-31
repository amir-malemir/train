n, t = map(int, input().split())
spend_time = list(map(int, input().split()))
read_book = 0
counter = 0
left = 0

for i in range(n-1):
    sum_books = 0
    time_for_read = 0
    counter = 0
    print(' first for !!!!!!!!')
    for j in spend_time:
        # print(f'j--> {j}')

        time_for_read += j
        print(f'time for read--> {time_for_read}')
        if time_for_read <= t:
            sum_books += 1
            print(f'sumbook--> {sum_books}')
        else:
            time_for_read -= spend_time[0]
            left += 1
            break

    if sum_books > read_book:
        read_book = sum_books
print(f'last answer : {read_book}')