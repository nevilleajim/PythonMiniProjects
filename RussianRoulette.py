import random

print("Russian Roulette.")
print('''Rules:
      1. Enter the number of plaeyers
      2. Roll the dice
      3. if you roll 6, its GAME OVER''')

players = int(input("Enter the number of players: "))

i = 0
while i != 6:
      for j in range(players):
            print("Player ", j+1, " turn.")
            inp = input("Press ENTER KEY to roll the dice")
            i = random.randint(1, 6)

            if i == 6:
                  print("Player ", j + 1, " rolled 6. GAME OVER.")
                  break
            else: 
                  print("Player ", j + 1, " rolled", i, ". GAME CONTINUES.")