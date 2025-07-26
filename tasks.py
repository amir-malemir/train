# for fun :D

#  for puzzle task

n, m = map(int, input().split())
puzzle_input = list(map(int, input().split()))
puzzle_input.sort()
output = 0

puzzle_num = [0] * m

for i in range(m-n+1):
    dif = puzzle_input[i+n-1] - puzzle_input[i]
    if dif <= output:
        output = dif
    elif output == 0:
        output = dif

print(output)