import numpy as np

def matrix_input():
      rows = int(input("Enter the number of rows: "))
      cols = int(input("Enter the number of columns: "))
      matrix = []
      print("Enter elements row wise: ")
      for i in range(rows):
            row = []
            for j in range(cols):
                  element = float(input(f"Enter element [{i + 1}][{j + 1}]: "))
                  row.append(element)
            matrix.append(row)
      return np.array(matrix)

def matrix_operations():
      print("MATRIX CALCULATIONS.")
      print("1. Addition")
      print("2. Substraction")
      print("3. Multiplication")
      print("4. Division")

      choice = int(input("Enter the operation number: "))
      matrix1 = matrix_input()
      matrix2 = matrix_input()

      if choice == 1:
            result = np.add(matrix1, matrix2)
      
      elif choice == 2:
            result = np.subtract(matrix1, matrix2)

      elif choice == 3:
            result = np.matmul(matrix1, matrix2)
      
      elif choice == 4:
            result = np.divide(matrix1, matrix2)
      
      else:
            print("Invalid choice")
      
      print("The result is: ")
      print(result)

matrix_operations()