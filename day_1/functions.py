def say_hello():
  return "Hello world!"

print(say_hello())

def set_alarm(day):
  if day == "Saturday" or day == "Sunday":
    return None
  else:
    return "07:00"

print(set_alarm(day="Saturday"))

def add(a, b = 5):
  return a + b

print(add(2))

