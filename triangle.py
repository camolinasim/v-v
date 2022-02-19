# Validity of Triangle given sides

# Function definition to check validity
def is_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


# Function definition for type
def type_of_triangle(a, b, c):
    if a == b and b == c:
        print('Triangle is Equilateral.')
    elif a == b or b == c or a == c:
        print('Triangle is Isosceles.')
    elif a!=b and a!=c and b!=c:
        print('Triangle is Scalane')
    else:
        print("Not a Triangle")


def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
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


# Reading Three Sides
side_a = sanitised_input('Enter length of side a: ', int, 1, 200)
side_b = sanitised_input('Enter length of side b: ', int, 1, 200)
side_c = sanitised_input('Enter length of side c: ', int, 1, 200)

# Function call & making decision
if is_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
else:
    print('NotATriangle')
