# decoupling functions
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598164#overview
# Functions should only do one thing... not multiple things

# def convert(feet_inches):
#     # does too much, functions should do one thing
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.254
#     return meters


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches # returns a tuple
    return {"feet": feet, "inches": inches} # return a dict with the values


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters



feet_inches = input("Enter height in feet and inches (ie 5 11): ")

# result = convert(feet_inches)
parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small")
    print(result)
else:
    print("Kid can use the slide")
    print(result)
