def say_hello():
  return "Hello world!"

hi_function = say_hello

def function_caller(callback):
  print("Hello from the higher order function")
  return callback()

# print(function_caller(say_hello))

def make_pretty(callback):
  def wrapper():
    print("I am a decorated function!")
    callback()
  return wrapper

@make_pretty
def ordinary_function():
  print("I am ordinary :(")

print(ordinary_function())