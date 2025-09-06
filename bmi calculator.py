height=float(input("Enter your height in cm :"))
Weight=float(input("Enter your weight in kg :"))
height=height/100
BMI= Weight/(height**2)
print("your Body mass index is :",BMI)
if BMI>0:
    if BMI<=16:
        print("you are severally underweight")
    elif BMI<=18.5:
        print("you are underweight")
    elif BMI<=25:
        print("you are healthy")
    elif BMI<=30:
        print("you are overweight")
    else:
        print("you are severally overweight")
else:
    print("you have entered invalid detailes!")
