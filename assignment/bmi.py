weight = int(input("weight="))
height = float(input("height="))
bmi = weight/float(height*height)
if bmi < 18.5:
    print("underweight")
elif  bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
   print("Overweight")
else:
   print("Obesity")
