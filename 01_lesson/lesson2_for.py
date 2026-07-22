#lst = [ '🍇', '🍑', '🍐', '🍊', '🍌', '🍎']

#print(lst[0] + ", " + lst[-1])

def is_year_leap(year):
    return year % 4 == 0


year_to_check = 2025
is_leap = is_year_leap(year_to_check)

print(f'год {year_to_check}: {is_leap}')

#---------
import math
def square(side):
    area = side * side
    return math.ceil(area)


side_length = 3.7
area_result = square(side_length)

print(f'Площадь квадрата со стороной {side_length}: {area_result}')
