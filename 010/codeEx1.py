
try:
    tValue = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    print(f"That is {(value / tValue) * 100}%")
    # All actions that depend on output/values need to be enclosed in the try except
except ValueError:
    print("You need to enter a number, Run the program again.")
except ZeroDivisionError:
    print("You cannot divide by zero, Run the program again.")




