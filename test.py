#  B. Sereja and Suffixes

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
list_of_questions = []
list_numbers = set()
results = [0] * n
counter = 0
index_number = 0
x = 0
while counter < m:
    l = int(input())
    list_of_questions.append(l)
    counter += 1

for i in range(n-1, -1):
    list_numbers.add(numbers[i])
    counter = len(list_numbers)
    results[i] = counter
print(list_numbers)

for l in list_of_questions:
    print(results[l - 1])


# for j in range(index_number, n):
#     list_of_numbers = []
#     if x < m:
#         index_number = list_of_questions[x] - 1
#         x += 1
#     list_of_numbers.append(numbers[j])
# output_numbers = set(list_of_numbers)   
# print(len(output_numbers))