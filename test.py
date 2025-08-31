n, t = map(int, input().split())
spend_time = list(map(int, input().split()))
read_book = 0
counter = 0
i = 0

for i in range(n-1):
    sum_books = 0
    time_for_read = 0
    
    print(' first for !!!!!!!!')
    for j in spend_time:
        time_for_read += j
        if time_for_read <= t:
            sum_books += 1
        else:
            break

    if sum_books > read_book:
        read_book = sum_books