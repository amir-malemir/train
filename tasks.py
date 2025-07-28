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
