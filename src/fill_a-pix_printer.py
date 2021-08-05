from turtle import Turtle

class FillaPixPainter:
    def __init__(self,size,table):
        self.t = Turtle()
        self.side = 10
        self.t.width(1)
        self.numSquares = size
        self.table = table
        

    def drawSquare(self,color):
        self.t.color(color)
        self.t.begin_fill()
        self.t.speed(0)
        for i in range(4):
            self.t.forward(self.side)
            self.t.right(90)
        self.t.end_fill()
        self.t.forward(self.side)

    def nextRow(self):
        self.t.penup()
        self.t.backward(self.numSquares*self.side)
        self.t.left(90)
        self.t.forward(self.side)
        self.t.right(90)
        self.t.pendown()

    def drawRow(self,colors,numbers):
        for j in range(len(colors)):
            for k in range(numbers[j]):
                self.drawSquare(colors[j])
        self.nextRow()

    
    def draw(self):
        all_numbers = [1 for i in range(self.numSquares)]
        all_colors = self.table
        all_colors.reverse()
        for i in range(len(all_colors)):
            for j in range(len(all_colors[i])):
                if all_colors[i][j]==0:
                    all_colors[i][j]="gray"
                else:
                    all_colors[i][j]="black"
                    
        for i in range(len(all_numbers)):
            self.drawRow(all_colors[i],all_numbers)

if __name__ == "__main__":
    a = FillaPixPainter(15,[
      [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
      [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
      [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
      [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
      [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
      [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]])
    a.draw()
