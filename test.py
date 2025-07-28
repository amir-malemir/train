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
    
if status == 1:
    print('YES')
else:
    print('NO')
