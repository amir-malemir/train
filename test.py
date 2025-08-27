n = int(input())
worm_gr = list(map(int, input().split()))
m = int(input())
which_worm = list(map(int, input().split()))
sums = []
current_sum = 0
for i in worm_gr:
    current_sum += i
    sums.append(current_sum)
for worm_num in which_worm:
    low = 0
    high = n - 1
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sums[mid] >= worm_num:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer + 1)

        