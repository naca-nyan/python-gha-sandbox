import tkinter
import numpy as np

class App(tkinter.Tk):
  def __init__(self):
    super().__init__()
    self.title("Hello, world!")

if __name__ == "__main__":
    App().mainloop()
