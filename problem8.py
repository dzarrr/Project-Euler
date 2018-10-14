## Dzar Bela Hanifa
## Project Euler no 8
## Written in Python 2.7

from collections import deque

file  = open("problem8data.txt", "r")

current_batch = []
counter = 0
q = deque()
max_result = -1

for line in file :
  for character in line.rstrip("\n\r") :
    counter += 1
    result = 1
    q.append(int(character))
    if counter >= 13 :
      for element in q :
        result = result * element
      if result > max_result :
        max_result = result
      q.popleft()

print max_result

