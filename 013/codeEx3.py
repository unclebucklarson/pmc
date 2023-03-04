# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/32436244#overview
# https://pythonhow.com/coding/d13c3/

def calc_age(year_of_birth, current_year=2023):
    # subtract year_of_birth from current year to get age
    return current_year - year_of_birth


year = int(input("What is the year of your birth: "))
age = calc_age(year)

if age > 120:
    print(f"Wow you have lived a long time! {age} years congrats!")
else:
    print(f"You are {age} years old.")