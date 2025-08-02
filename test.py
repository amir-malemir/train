n = int(input())
people = []
input = 0
output = 0

for i in range(n):
    inside, outside = map(int, input().split())
    people.append((inside, outside))
for peo in people:
    input = peo[0]
    output = peo[1]
    calc = input + peo[0] - peo[1]
print(people)
print(calc)