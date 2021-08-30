from turtle import Turtle

class FillaPixPainter:
    def __init__(self,size,table):
        self.turtle = Turtle()
        self.side = 10
        self.turtle.width(1)
        self.numSquares = size
        self.table = table


    def drawSquare(self,color):
        self.turtle.color(color)
        self.turtle.begin_fill()
        self.turtle.speed(0)
        for _ in range(4):
            self.turtle.forward(self.side)
            self.turtle.right(90)
        self.turtle.end_fill()
        self.turtle.forward(self.side)

    def nextRow(self):
        self.turtle.penup()
        self.turtle.backward(self.numSquares*self.side)
        self.turtle.left(90)
        self.turtle.forward(self.side)
        self.turtle.right(90)
        self.turtle.pendown()

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
