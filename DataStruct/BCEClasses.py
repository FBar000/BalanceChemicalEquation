# Holds a pair of numbers, representing the start and end of a substring
class Unit:

  def __init__(self, lo, hi):
    if lo <= hi:
      self.lo = lo
      self.hi = hi
    else:
      self.lo = -1
      self.hi = -1
      raise ValueError("lo must be less than or equal to hi")


  def __eq__(self, other):
    if (isinstance(other, Unit)):
      return self.lo == other.lo and self.hi == other.hi

  def __str__(self):
    return "(" + str(self.lo) + "," + str(self.hi) + ")"

  def size(self):
    return self.hi - self.lo

  def display(self):
  	print("(" + str(self.lo) + ", " + str(self.hi) + ")")


