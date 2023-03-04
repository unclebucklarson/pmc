def check_state(the_temp):
    # https://pythonhow.com/coding/d14c2/
    freezing = 0.0
    boiling = 100.0

    # expect temp in Celsius
    if the_temp >= boiling:
        return "Gas"
    elif the_temp <= freezing:
        return "Solid"
    else:
        return "Liquid"

# instructors solution
# https://pythonhow.com/coding/d14c1/
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
