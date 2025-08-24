n = int(input())
worm_gr = input()
m = int(input())
which_worm = input()

low = 0
high = 0
while True:
    for i in range(m):
        if which_worm[[i]] <= low:
            print('low')
        elif which_worm > low:
            print('high')