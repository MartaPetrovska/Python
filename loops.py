# Nr.1 Task = Analyzing Numbers - Iterate through a list of 10 random numbers and determine whether each number is higher or lower than 5.

import random
random_numbers = []
for i in range(10):
  random_numbers.append(random.randrange(1,11))

print(random_numbers)

for i in random_numbers:
  if i > 5:
    print(f'{i} is higher than 5')
  elif i == 5:
    print(f'{i} is 5')
  else:
    print(f'{i} is lower than 5')
