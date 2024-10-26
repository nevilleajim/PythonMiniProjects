#TRIANGLE TYPE IDENTIFIER
print("Enter the lengths of sides of a triangle: ")
side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):    #Triangle Inequality Theorem
      if side1 == side2 == side3:
            print("The triangle is an EQUILSTERAL TRIANGLE.")
      elif (side1 == side2) or (side2 == side3) or (side1 == side3):
            print("The triangle is an ISOCELES TRIANGLE.")
      else:
            print("The triangle is a SCALENE TRIANGLE.")
else:
      print("The Triangle is not valid.")