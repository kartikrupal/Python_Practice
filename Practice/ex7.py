weight=int(input("enter weight in kg:"))
height=float(input("enter height in meter:"))
bmi=weight/height**2
print(f"The BMI is {bmi}")
if bmi>25:
    print("overweight")
elif bmi>16 and bmi<25:
    print("normal")
elif bmi<16:
    print("underweight")
else:
    print("invalid")
