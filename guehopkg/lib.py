def bmi_calculator(height, weight):
    bmi = round(weight / (height)**2 * 100, 2)
    return bmi
