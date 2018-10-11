## Dzar Bela Hanifa
## Project Euler no 8
## Written in Python 2.7

from collections import deque

file  = open("problem8data.txt", "r")

result = 1
counter = 0
q = deque()
for line in file :
  for character in line.rstrip("\n\r") :
    counter += 1
    if counter >= 13 :
      result /= q.popleft()
    result *= int(character)
    q.append(result)
    print result, int(character)

