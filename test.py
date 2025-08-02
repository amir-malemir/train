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
