n, s = map(int, input().split())
dragon_lists = []
for i in range(n):
    dragon_attack, dragon_bonus = map(int, input().split())
    dragon_lists.append((dragon_attack, dragon_bonus))

for dragon in dragon_lists:
    attk = dragon[0]
    bonus = dragon[1]
    print('*' * 10)
    print(attk)
    print(bonus)
    print('-' * 10)

    if s > attk:
        s = s + bonus
        print('yes')
    else:
        print('lose')
# 
