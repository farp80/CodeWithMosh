def greet(first_name, last_name):
    print(f"Hello, it is me {first_name} {last_name}!")
    print("The one you are looking for")


greet("Fidel", last_name="Rosell")  # keyboard argument
# parameters are part of the signature of the method while argument is the real value of that parameter.

# Type of functions
# 1. Perform a Task  --> It returns None
# 2. Return a value  -->


def increment(number, by=1):  # optional parameters go after the required parameters
    return number + by


print(increment(2))
print(increment(2, 5))

# *arg, wait, what
# [] => List
# () => Tuples -> we cannot add items to tuples.


def multiple(*numbers):  # list packing
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiple(2, 3, 4, 5))

# **arg --> name parameters --> it will create a dictionary


def save_user(**user):
    print(user["name"])


save_user(id=1, name="fidel", age=22)

# F9 add breakpoint
# F5 run it | Shift + F5 stop it
# Shift + F11 --> Step out of the function.

# Shortcuts:


def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if(input % 3 == 0):
        return "Fizz"
    if(input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz(2))
