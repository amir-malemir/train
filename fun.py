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