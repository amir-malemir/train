# for fun :D

#  for puzzle task

n, m = map(int, input().split())
puzzle_input = list(map(int, input().split()))
puzzle_input.sort()
output = 0
counter_min = 0
for i in range(m-n+1):
    dif = puzzle_input[i+n-1] - puzzle_input[i]
    if counter_min == 0:
        output = dif
        counter_min += 1
    if dif <= output:
        output = dif
        
print(output)


# boy and girl in chatroom

n = set(input())
m = len(n)

if m % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')


# stone on the table

n = int(input())
m = input()
counter = 0
output = 0 

for i in range(n-1):
    if m[i] == m[i+1]:
        output = output + 1
        
print(output)

# dragon attack and bonus task

s, n = map(int, input().split())
dragon_lists = []

status = False

for i in range(n):
    dragon_attack, dragon_bonus = map(int, input().split())
    dragon_lists.append((dragon_attack, dragon_bonus))
dragon_lists.sort()
for dragon in dragon_lists:
    attk = dragon[0]
    bonus = dragon[1]
    if s > attk:
        s = s + bonus
        status = True
        
    else:
        status = False
        break

if status == True:
    print('YES')
else:
    print('NO')


# 208A - Dubstep task

n = input()

m = n.replace('WUB', ' ')

print(m)

# Vanya and Lanterns

n, l = map(int, input().split())
fanos_l = list(map(int, input().split()))
middle = 0

fanos_l.sort()

if n > 1:    
    for i in range(n-1):
        calcu = fanos_l[i+1] - fanos_l[i]
        if calcu > middle:
            middle = calcu
middle = middle/ 2
first_l = fanos_l[0] - 0
last_l = l - fanos_l[n-1]
output = max(first_l, last_l, middle)
print(output)

# Amusing Joke

mehman = input()
mizban = input()
string_convert = input()


mix_input = mehman + mizban
mix_input = "".join(sorted(mix_input))
diff_string = "".join(sorted(string_convert))
if mix_input == diff_string:
    print('YES')
else:
    print('NO')

    # Business trip 

n = int(input())
month = list(map(int , input().split()))
counter = 0
sum_number = 0
flag = False
month.sort(reverse=True)
if n == 0:
        flag = True
        print('0')
        
for i in range(12):
    counter += 1
    sum_number = sum_number + month[i]
    if sum_number >= n and n > 0:
        flag = True
        print(counter)
        break
if flag == False:
    print('-1')

# Tram

n = int(input())
people = []
in_people = 0
out_people = 0
calc = 0
max_num = 0

for i in range(n):
    outside, inside = map(int, input().split())
    people.append((outside, inside))
for peo in people:
    calc = calc + peo[1] - peo[0] 
    in_people = peo[1]
    out_people = peo[0]
    if calc > max_num:
        max_num = calc

print(max_num)

# Pangram 

import string
all_alphabet = string.ascii_lowercase
m = int(input())
n = list(input().lower())
if len(set(n)) >= 26:
    n.sort()
    input_user = set(n)
    output_char = "".join(sorted(input_user)).lower()
    if output_char in all_alphabet:
        print('YES')
    else:
        print('NO')
else:
    print('NO')


# Worms 474B

n = int(input())
worm_gr = list(map(int, input().split()))
m = int(input())
which_worm = list(map(int, input().split()))
sums = []
current_sum = 0
for i in worm_gr:
    current_sum += i
    sums.append(current_sum)
for worm_num in which_worm:
    low = 0
    high = n - 1
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sums[mid] >= worm_num:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer + 1)
 


# Books 279/B - n**2 time complexity
n, t = map(int, input().split())
time_for_read = list(map(int, input().split()))

read_book = 0
sum_books = 0
counter = 0

for i in range(n):
    time_spend = 0
    for j in range(i, n):
        time_spend += time_for_read[j]
        if time_spend > t:
            break
        sum_books = j - i + 1
        if sum_books > read_book:
            read_book = sum_books


print(read_book)


# Books 279/B - بهینه و مفید

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