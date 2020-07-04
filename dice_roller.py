import random
def main():
  sum = 0
  dice_rolls = 2
  for i in range (0, dice_rolls):
    roll = random.randint(1,6)
    print(f'Die number {i+1} rolled a {roll}')
    sum += roll
  print(f'Sum of both die is {sum}')
if __name__== "__main__":
  main()