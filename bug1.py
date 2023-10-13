class Circle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        return f"""
        ({self.x}, {self.y})
        {self.size}
       , - ~ ~ ~ - ,
     ,'             ',
    ,		      ,
    ,                  ,
    ,		       ,
    ,                  ,
     ,                ,
      ',            ,'
        - , _ _ _ ,'
	      """
def main():
    c = Circle(1, 2, 3)
    print("This is a circle")
    print(f"({c.x}, {c.y})")
    print(c.size)
    print(c.draw())

if __name__ == "__main__":
    main()
