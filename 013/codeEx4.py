# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/32436244#overview
# https://pythonhow.com/coding/d13c4/ # doesn't follow keep it simple...

def split_names(string_of_names):
    """ Split a comma separated string of names into a list """
    return string_of_names.split(",")


names = input("Enter names separated by commas (no spaces): ")
separated_names = split_names(names)
print(len(separated_names))