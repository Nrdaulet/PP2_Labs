class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def show(self):
    print(self.x, self.y)

  def move(self, x, y):
    self.x = x
    self.y = y

  def dist(self, point2):
    return ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()

print(p1.dist(point2=p2))

p2.move(6, 7)
p2.show()
