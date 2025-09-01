


n, t = map(int, input().split())
time_for_read_books = list(map(int, input().split()))
books_read = 0
start_index = 0
time_spent = 0

for i in range(n):
    time_spent += time_for_read_books[i]
    print(f' print i --> {i}')
    print(f' print time_spent--> {time_spent}')
    if time_spent > t:
        time_spent -= time_for_read_books[start_index]
        print(f' print time_spent after - --> {time_spent}')

        start_index += 1
        print(f' print start_index --> {start_index}')
    print(f' i, startindex {i,start_index}')
    result = i - start_index + 1
    print(f'res--> {result}')
    if result > books_read:
        books_read = result
    print(f'books_read--> {books_read}')
print(books_read)