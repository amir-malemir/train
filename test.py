n = int(input())
worm_gr = list(map(int, input().split()))
m = int(input())
which_worm = list(map(int, input().split()))

for i in worm_gr:
    sum_list += i
print(sum_list)
low = 0
high = 0

# while True:
#     for i in range(m):
#         if which_worm[[i]] <= low:
#             print('low')
#         elif which_worm > low:
#             print('high')
#     break