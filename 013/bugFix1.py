
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/32453766#overview
# solution: https://pythonhow.com/coding/d13b1/
# orig def
# def calcualte_time(g=9.80665, h):
#     t = (2 * h / g ) ** 0.5
#     return t

# non-default parameter cannot follow a default parameter
def calcualte_time(h, g=9.80665):
    t = (2 * h / g ) ** 0.5
    return t


time = calcualte_time(100)
print(time)
