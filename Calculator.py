num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operators = ("+", "-", "*", "/")

operation = input("Enter the operation (+, -, *, /): ")
if operation in operators:
      if operation == "+":
            result = num1 + num2
            print("Result: ", result)
      if operation == "-":
            result = num1 - num2
            print("Result: ", result)
      if operation == "*":
            result = num1 * num2
            print("Result: ", result)
      if operation == "/":
            result = num1 / num2
            print("Result: ", result)

else:
      print("Invalid Operator!!")