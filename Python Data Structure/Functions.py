def func1():
  print("I am learning python")
  print("I am learning python")

func1()

def square(x):
  result = x ** 2
  return result

print(square)

def multiply(x=10, y=10):
  print(y)
  return x * y

print(multiply(y=12, x=14))

def digital(*args):
  print(type(args))

digital(1, 2, 3, 4, 5)
digital("Hello", "bye", "hi", "nope")
