# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34597778#overview
# password checker
# Modified for codeex2

print("Welcome to the password checker.")
print("Your password must be 7 chars or longer, have a number, upper and lowercase and a symbol.")

password = input("Enter password: ")
result = {}

length = False
if len(password) >= 7:
    length = True
result["length"] = length

digit = False
for char in password:
    if char.isdigit():
        digit = True
        break  # found a digit, exit loop
result["digit"] = digit

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
        break  # found 1 upper case, exit
result["uppercase"] = uppercase

symbol = False
for char in password:
    if not char.isalnum():
        symbol = True
        break
result["symbol"] = symbol

# new python function 'all', receives an iterable, if all items are True, returns True, else false.
# Zero length iterable returns true...
print(f"result is: {result}")

if all(result.values()):  # length must be greater than zero and all values must be true for the iterable
    # for codex2
    if len(password) == 7:
        print("Password is OK, but not too strong.")
    else:
        print("Strong Password")
else:
    print("Weak password")
