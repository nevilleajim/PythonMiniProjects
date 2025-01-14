def PatternGenerator(n):
      k = n-1           #stores number of spaces

      for i in range(1, n+1):
            for j in range(0, k):
                  print(" ", end=' ')
            
            k = k-1

            for j in range(0, i):
                  print("*  ", end=" ")
            print("\n")

PatternGenerator(5)