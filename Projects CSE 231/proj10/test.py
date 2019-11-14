class Example(object):
  def __init__(self, v1 = 0, v2 = 0):
    self.v1 = v1
    self.v2 = v2
  def __add__(self, v1, v2):
    num = self.v1 + self.v2
    return num

def main():
  a = Example(20,30)
  print(a)
  b = Example(40,50)
  c=a+b
  print(c)
main()