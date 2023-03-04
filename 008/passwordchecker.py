# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34597778#overview
# password checker
print("Welcome to the password checker.")
print("Your password must be 8 chars or longer, have a number, upper and lowercase and a symbol.")
password = input("Enter password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for char in password:
    if char.isdigit():
        digit = True
        break  # found a digit, exit loop
result.append(digit)

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
        break  # found 1 upper case, exit
result.append(uppercase)

symbol = False
for char in password:
    if not char.isalnum():
        symbol = True
        break

result.append(symbol)

# new python function 'all', receives an iterable, if all items are True, returns True, else false.
# Zero length iterable returns true...
print(f"result is: {result}")

if all(result) and len(result) > 0:  # length must be greater than zero and all values must be true
    print("Strong Password")
else:
    print("Weak password")
