n = int(input())
worm_gr = list(map(int, input().split()))
m = int(input())
which_worm = list(map(int, input().split()))
prefix_sums = []
current_sum = 0
for i in worm_gr:
    current_sum += i
    prefix_sums.append(current_sum)
print(prefix_sums)
low = 0
high = 0

# while True:
#     for i in range(m):
#         if which_worm[[i]] <= low:
#             print('low')
#         elif which_worm > low:
#             print('high')
#     break