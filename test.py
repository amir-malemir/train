# C. Qpwoeirut And The City
# n = int(input())
# m = int(input())
# i = 0

# while i < n:
#     print(m)

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