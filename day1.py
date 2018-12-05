import time
import random
then = time.time() #Time before the operations start
inputfile = open('input.txt', 'r')
freq = 0
freq1 = 0
number = {0}
inters = 0
found = 0
numbers = [int(line) for line in inputfile.readlines()]

while (found == 0):
  inters += 1
  for num in numbers:
    freq = freq + num
    if freq in number:
      found = 1
      print(freq); break
    else:
      number.add(freq)
now = time.time() #Time after it finished
print("It took: ", now-then, " seconds")
print(inters)
