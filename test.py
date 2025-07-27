n = int(input())
m = input()
counter = 0
output = 0 

for i in range(n-1):
    if m[i] == m[i+1]:
        output = output + 1
        
print(output)
