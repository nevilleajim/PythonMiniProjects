def calculate_factorial(n):
      if n == 0:
            return 1
      elif n < 0:
            return None
      else: 
            return n * calculate_factorial(n - 1)

# while (1):
# n = int(input("Enter the number to be calculate: "))
# print(f"The factorial of {n} is {calculate_factorial(n)}")