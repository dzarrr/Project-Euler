## Dzar Bela Hanifa
## Project Euler no 4
## Written in Python 2.7

min_range = input("min range : ")
max_range = input("max range : ")

def check_palindrome(str):
  i = 0
  palindrome = True
  while (i < len(str) // 2) and (palindrome):
    front_iterator = i
    back_iterator = len(str) - i - 1
    if (str[front_iterator] != str[back_iterator]) :
      palindrome = False
    i += 1

  return palindrome

for number_one in range (min_range, max_range) :
  for number_two in range (min_range, max_range) :
    result = number_one * number_two
    if check_palindrome(str(result)) :
      print (result)