n, m = map(int, input().split())
numbers = list(map(int, input().split()))
counter = 0 
for i in range(m):
    l = int(input())
    index_number = l - 1
    list_of_numbers = []
    
    for j in range(index_number,n):
        list_of_numbers.append(numbers[j])

output_numbers = set(list_of_numbers)   
print(len(output_numbers))