def get_number(msg: str, min_num: int = 0, max_num: int = 300) -> int:
    number = ""
    
    while True:

        number = input(msg)
        if number.isdigit():
            number = int(number)
            if number >= min_num and number <= max_num:
                break
    return int(number)

def get_bmi(height ,weight):
    return 10_000 * (weight / height / height ) 

def bmi_ranges(bmi: int):
    bmi_number = bmi

    if bmi_number <= 18.5:
        print('underwight')
    elif bmi_number <= 24.9:
        print('healthy weight')
    elif bmi_number <= 29.9:
        print('overweight')
    else:    
        print('obase range')




number1 = get_number(msg = 'height? ', min_num = 70, max_num = 200)
number2 = get_number(msg = 'weight? ')
print(number1, number2)

bmi = get_bmi(number1, number2)
bmi = "{:.2f}".format(bmi)
print(bmi)
bmi_ranges(float(bmi))

# L = 0 
# read_ptr = L
# write_ptr = 1
# L = 1

# if L == 0:
#     print('Error - empty list')

#     while read_ptr != 0:
#         next_read_ptr = read_ptr + 1




# students = []
# while True:
#     name = input('name? ')
#     age = input('age? ')
#     while not age.isdigit():
#         age = input('age? ')
#     age = int(age)
#     students.append({'name': name, 'age': age})
#     resume = input('add? (n/y) ')
#     if resume.lower() == 'n':
#         break
# print('*' * 10)

# for stu in students:
#     print(stu['name'], stu['age'])

# print('*' * 10)


def is_car_available(year:int , *cars):
    available_cars = {
        2025: ['BMW', 'audi  '],
        2024: ['mercedes', 'BMW', 'jeep  ']
    }
    models = available_cars.get(year)
    print(models)
    models = [model.strip().lower() for model in models]
    print(models)
    
    if not models:
        print( 'sry, we dont have car for this year' )
        return
    for car in cars:
        if car.strip().lower() in models:
            print(f'{car.title()} is available')
        else:
            print(f'{car.title()} is not available')

is_car_available(2024,'BMW', 'volvo  ')