# check if a 'password' is seven chars or greater.

passwd = input("Enter password: ")

if len(passwd) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")