# C. Qpwoeirut And The City
# n = int(input())
# m = int(input())
# i = 0

# while i < n:
#     print(m)

# L = 0 
# read_ptr = L
# write_ptr = 1
# L = 1

# if L == 0:
#     print('Error - empty list')

#     while read_ptr != 0:
#         next_read_ptr = read_ptr + 1

def get_number(age, weight):
    age = ""
    weight = ""
    while not age.isdigit():
        age = input('age? ')
    age = int(age)
    while not weight.isdigit():
        weight = int(input('weight? '))
    weight = int(weight)
    
    return age, weight

bmi = get_number(50, 180)
print(bmi)