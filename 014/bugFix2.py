# import bf2_functions.py  # Including the file extension is wrong
# Solution:: https://pythonhow.com/coding/d14b2/
# bugfix2.py
# import bf2_functions
#
#
# nr_of_periods = bf2_functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)

# bugex3.py
from bf2_functions import count

# nr_of_periods = bf2_functions.count("Trees are good. Grass is green.")  # Error here is referencing the module
nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)