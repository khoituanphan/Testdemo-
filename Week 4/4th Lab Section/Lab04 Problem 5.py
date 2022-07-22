
h = float(input("Enter your height in metres: "))
w = float(input("Enter your weight in kg: "))


def calculate_bmi(weight, height):
    return weight / (height ** 2)


bmi = calculate_bmi(w, h)

print("Patient's BMI is: %.2f" % bmi)