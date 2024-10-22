height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

BMI = weight/(height/100) ** 2
print("The BMI is: ", BMI)

if BMI <= 18.5:
      print("Opps!! You are underweight.")
elif BMI <= 24.9:
      print("Awesome!! You are healthy")
elif BMI <= 29.9:
      print("Oh no!! You are overweight.")
else:
      print("You are obese.")