#  B. Sereja and Suffixes

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
list_of_questions = []
counter = 0 
while counter < m:
    l = int(input())
    list_of_questions.append(l)
    counter += 1

for x in range(m):
    index_number = list_of_questions[x] - 1
    
    list_of_numbers = []
    
    for j in range(index_number,n):
        list_of_numbers.append(numbers[j])
    output_numbers = set(list_of_numbers)   
    print(len(output_numbers))