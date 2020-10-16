# numbers = range(1, 11)
# for number in numbers:
#   print(number)

def generate_evens(upper_bound):
  number = 0
  while number < upper_bound:
    if number % 2 == 0:
      yield number
    number += 1

for number in generate_evens(10):
  print(number)