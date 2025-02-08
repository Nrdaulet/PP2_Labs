class task1:
  def getString(self):
    self.input_string = input()

  def printString(self):
    print(self.input_string.upper())

if __name__ == "__main__":
    res = task1()
    res.getString()
    res.printString()