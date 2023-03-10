def add(*args):
  total = 0
  for n in args:
    total += n
  return total

# print(add(1,2,3,1012,123,1234344,123))

def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)

class Car:
  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.color = kw.get("color")
    self.sears = kw.get("seats")

my_car = Car(model="gtr")
print(my_car.make)