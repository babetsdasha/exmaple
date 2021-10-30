import re


class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_number_group(n):
    try:
        int(n)
    except ValueError:
        return "You entered incorrect data. Please try again."

    try:
        if int(n) <= 10:
            raise ToSmallNumberGroupError("We obtain error: Number of your group can't be less than 10")
    except ToSmallNumberGroupError as e:
        return e.data

    return f"Number of your group {n} is valid"


def solve_quadric_equation(a, b, c):
    try:
        float(a)
        float(b)
        float(c)
        x1 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    except ValueError:
        return "Could not convert string to float"
    except ZeroDivisionError:
        return "Zero Division Error"
    else:
        return f"The solution are x1={complex(x1)} and x2={complex(x2)}"


def day_of_week(day):
    try:
        int(day)
    except ValueError:
        return "You did not enter a number! Please try again."

    if int(day) > 7 or int(day) <= 0:
        return "There is no such day of the week! Please try again."

    dict_days = {1: "Monday", 2: "Tuesday", 3: "Wendsday", 4: "Thursday", 5: "Friday", 6: "Sanday", 7: "Saturday"}
    return dict_days[int(day)]


class MyError(Exception):
    pass


def check_positive(number):
    try:
        int(number)
    except ValueError:
        return "Error type: ValueError!"

    if float(number) >= 0:
        return f"You input positive number: {float(number)}"

    if float(number) < 0:
        return f"You input negative number: {float(number)}. Try again."


def divide(numerator, denominator):
    try:
        int(numerator)
        int(denominator)
        x = numerator / denominator
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except(TypeError, ValueError):
        return "Value Error! You did not enter a number!"
    else:
        return f"Result is {x}"


def check_odd_even(number):
    try:
        int(number)
        if number % 2:
            return "Entered number is odd"
        else:
            return "Entered number is even"
    except ValueError:
        return "You entered incorrect data. Please try again."


def valid_email(s):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if(re.search(pattern, s)):
        return "Email is valid"
    else:
        return "Email is not valid"
