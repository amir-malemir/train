n, t = map(int, input().split())
spend_time = list(map(int, input().split()))
read_book = 0
next_number = 0
time_for_read= 0
for i in range(n):
    time_for_read += spend_time[i]


    while time_for_read > t:
        time_for_read -= spend_time[next_number]
        next_number += 1

    read_book = max(read_book, i - next_number + 1)
print(read_book)