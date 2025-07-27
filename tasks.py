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