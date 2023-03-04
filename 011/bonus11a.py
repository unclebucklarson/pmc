
def get_average():
    with open("data.txt", "r") as file:
        data = file.readlines()[1:]  # ignore the title line, instructors solution

    # This was my solution...
    # running_total = 0
    # for index, value in enumerate(data):
    #     if index == 0:  # ignore the title line
    #         continue
    #     else:
    #         running_total += int(value)

    # instructors solution
    values = [float(i) for i in data]  # list comprehension brilliant

    average_local = sum(values) / len(values)  # sum function... Brilliant

    return average_local

average = get_average()

print(f"Average temp is {average}")