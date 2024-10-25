from time import sleep

def countDown(n):
      print(n)
      sleep(1) #ensures the function stops executing 1 second after the number is printed

      if n == 1:
            return
      else:
            countDown(n - 1)

n = int(input("Enter the Number to start countdown from: "))
countDown(n)
