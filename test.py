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

def get_number(msg: str):
    number = ""
    
    while not number.isdigit():
        number = input(msg)
    
    return int(number)

def get_bmi(height ,weight):
    return 10_000 * (weight / height / height ) 



number1 = get_number(msg = 'height? ')
number2 = get_number(msg = 'weight? ')
print(number1, number2)

bmi = get_bmi(number1, number2)
bmi = "{:.2f}".format(bmi)
print(bmi)