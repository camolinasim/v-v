# Validity of Triangle given sides
from itertools import cycle

# Function definition to check validity
def is_valid_date(month, day, year):
    if 1 <= month <= 12 and 1 <= day <= 31 and 1812 <= year <= 2022:
        return True
    else:
        return False


# Function definition for type
def next_day(month, day, year):
    #flags
    increase_month = False
    increase_year = False

    if(day==31):
        increase_month = True
    if(month==12 and increase_month):
        increase_year = True

    month_cycle = range(1,13)
    month_pool = cycle(month_cycle)

    day_cycle = range(1,32)
    day_pool = cycle(day_cycle)

    year_cycle = range(1812,2023)
    year_pool = cycle(year_cycle)

    for i in range(0, day+1):
        day=next(day_pool)
    #print(day)

    if(increase_month):
        for i in range(0, month + 1):
            month = next(month_pool)
        #print(day)

    if (increase_year):
        for i in range(0, year - 1810):
            year = next(year_pool)
        #print(year)
    print(month, day, year)



    # if condition:
    #     print('Triangle is Equilateral.')



def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Invalid Input Value: Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Invalid Input Value: Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Invalid Input Value: Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Invalid Input Value: Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Invalid Input Value: Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return ui


# Reading Three inputs
month = sanitised_input('Enter the month number: ', int, 1, 12)
day = sanitised_input('Enter the day number: ', int, 1, 31)
year = sanitised_input('Enter the year: ', int, 1812, 2022)

# Function call & making decision
if is_valid_date(month, day, year):
    next_day(month, day, year)
# else:
#     print('NotATriangle')
