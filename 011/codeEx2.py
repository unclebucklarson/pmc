def get_max(value_list):
    # grades = [9.6, 9.2, 9.7]
    return max(value_list), min(value_list)


max, min = get_max([9.6, 9.2, 9.7])
print(f"Max: {max}, Min: {min}")