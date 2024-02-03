def bmi(weight, heigth):
    index = weight / (heigth * heigth)
    return index

p6 = bmi(79, 1.73)
print(p6 < 18.5)
