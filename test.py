n = int(input())
people = []
in_people = 0
out_people = 0
max_num = 0

for i in range(n):
    outside, inside = map(int, input().split())
    people.append((outside, inside))
for peo in people:
    in_people = peo[1]
    out_people = peo[0]
    calc = max_num - peo[0] + peo[1]
    if calc > max_num:
        max_num = calc


print(max_num)
