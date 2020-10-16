shopping_list = ["milk", "bacon", "eggs"]
for item in shopping_list:
  print(item.upper())

print("End of the list")

for number in range(1, 11):
  print(number)

counter = 0
while(counter < 10):
  print("I'll stop soon")
  counter += 1

print("the loops over")

today = "Saturday"
weather = "rainy"

if today == "Saturday" and weather == "rainy":
  print("Let's have a long-lie!")

if 5 != 10:
  print("maths is working")

if today is "Saturday":
  print("hello!")

breakfast = ["eggs", "bacon"]

if breakfast is ["eggs", "bacon"]:
  print("hello!") 
  # doesn't work because not strictly the same

if "eggs" in breakfast:
  print("yay, omelette!")

string = "somestring"
if "some" in string:
  print("there is some in string")


numbers = range(1, 11)
evens_squared = []
for number in numbers:
  if number % 2 == 0:
    evens_squared.append(number ** 2)

print(evens_squared)

evens_squared = [number ** 2 for number in numbers if number % 2 == 0]
print(evens_squared)


