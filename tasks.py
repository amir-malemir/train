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
        