# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/32560228#overview
# in the problem, they are importing the entier module but not directly referencing the function.

import bf1_functions

# nr_of_periods = count("Trees are good. Grass is green.")  # The error
nr_of_periods = bf1_functions.count("Trees are good. Grass is green.")  # The Fix.
print(nr_of_periods)