# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/32436244#overview
# https://pythonhow.com/coding/d13c2/

def calc_age(year_of_birth, current_year=2023):
    # subtract year_of_birth from current year to get age
    return current_year - year_of_birth

year = int(input("What is the year of your birth: "))

print(calc_age(year))