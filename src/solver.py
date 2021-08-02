import time

class FillaPix:
  def __init__(self,xsize,ysize,table):
    self.xsize = xsize
    self.ysize = ysize
    self.table = table
    self.number_completed = {}
    self.boxes = []
    self.numbers = {}
    self.numbers_todo = []

  def make_boxes(self):
    alku = time.time()
    lista = []
    for i in range(self.xsize):
      lista2 = []
      for j in range(self.ysize):
        lista2.append(Box(i,j))
      lista.append(lista2)
    loppu = time.time()
    print(f"latikoiden tekemiseen kului aikaa {loppu-alku}")
    # print(lista)
    self.boxes = lista
    # return lista

  def make_numbers(self):
    alku = time.time()
    all_numbers = {}
    for i in range(0,10):
      all_numbers[i] = []
      self.number_completed[i] = []
    for x in range(len(self.table)):
      y = 0
      for a in self.table[x]:
        if a == ';':
          y += 1
        else:
          boxes = []
          if x == 0 or y == 0 or x == (self.xsize-1) or y == (self.ysize-1): # reunassa
            if x == 0: # yla sivu
              if y == 0:# vas yla kulma
                # print(f"vas yla {x} {y} {a}")
                boxes.append(self.boxes[0][0])
                boxes.append(self.boxes[1][0])
                boxes.append(self.boxes[0][1])
                boxes.append(self.boxes[1][1])
              elif y == self.ysize-1: # oik yla kulma
                # print(f"oik yla {x} {y} {a}")
                boxes.append(self.boxes[0][self.ysize-1])
                boxes.append(self.boxes[1][self.ysize-1])
                boxes.append(self.boxes[0][self.ysize-2])
                boxes.append(self.boxes[1][self.ysize-2])
              else: # yla reuna
                # print(x,y,a)
                for i in range(y-1,y+2):
                  boxes.append(self.boxes[x][i])
                  boxes.append(self.boxes[x+1][i])
                  # print(x,i)
                  # print(x+1,i)
            elif x == self.xsize-1: # ala sivu
              if y == 0: # van ala kulma
                # print(f"vas ala {x} {y} {a}")
                boxes.append(self.boxes[self.xsize-1][0])
                boxes.append(self.boxes[self.xsize-2][0])
                boxes.append(self.boxes[self.xsize-1][1])
                boxes.append(self.boxes[self.xsize-2][1])
              elif y == self.ysize-1: # oik ala kulma
                # print(f"oik ala {x} {y} {a}")
                boxes.append(self.boxes[self.xsize-1][self.ysize-1])
                boxes.append(self.boxes[self.xsize-1][self.ysize-2])
                boxes.append(self.boxes[self.xsize-2][self.ysize-1])
                boxes.append(self.boxes[self.xsize-2][self.ysize-2])
              else: # ala reuna
                # print(x,y,a)
                for i in range(y-1,y+2):
                  boxes.append(self.boxes[x-1][i])
                  boxes.append(self.boxes[x][i])
                  # print(x-1,i)
                  # print(x,i)
            elif y == 0: # vas reuna
              # print(x,y,a)

              for i in range(x-1,x+2):
                boxes.append(self.boxes[i][y])
                boxes.append(self.boxes[i][y+1])
                # print(i,y)
                # print(i,y+1)
            elif y == self.ysize-1: # oik reuna
              # print(x,y,a)

              for i in range(x-1,x+2):
                boxes.append(self.boxes[i][y-1])
                boxes.append(self.boxes[i][y])
                # print(i,y-1)
                # print(i,y)
            # print(boxes)
          else: # keskella
            # print(f"alku {x} {a}")
            for e in range((x-1),x+2):
              for r in range((y-1),y+2):
                # print(e,r)
                boxes.append(self.boxes[e][r])
            # print(boxes)
          new_number = Number(x,y,a,boxes) # uusi numero
          all_numbers[int(a)].append(new_number) # uusi numero numerot listaan
          self.boxes[x][y].set_number(new_number) # merkataan numero oikeaan Box objektiin
    loppu = time.time()
    print(f"numeroiden tekemiseen kului aikaa {loppu-alku}")
    self.numbers = all_numbers
    # return all_numbers

  def print_table(self):
    out = []
    for i in self.boxes:
      row = []
      for j in i:
        row.append(j.value)
      out.append(row)
    for i in out:
      print(i)

  def solve_step_1(self):
    for num in self.numbers[0]:
      for box in num.number_boxes:
        box.value = 0
    for num in self.numbers[9]:
      for box in num.number_boxes:
        box.value = 1
    self.number_completed[0] = self.number_completed[0] + self.numbers[0]
    self.number_completed[9] = self.number_completed[9] + self.numbers[9]


  def solve_step_2(self):
    alku = time.time()
    for i in range(1,9):
      self.numbers_todo.extend(self.numbers[i])
    # print(self.numbers_todo)

    togo = True
    round = 1
    while togo is True:

      numbers_todo_round2 = self.numbers_todo.copy()
      togo = False
      print(f"kierros {round} numeroita {len(self.numbers_todo)}")
      # print(len(self.numbers_todo))
      for i in range(0,len(self.numbers_todo)):
        num = self.numbers_todo[i]
        boxes = num.number_boxes
        sum_black = 0
        sum_white = 0

        for box in boxes:
          if box.value == 1:
            sum_black += 1
          if box.value == 0:
            sum_white += 1
        # print(f"numero {num.n} mustia {sum_black} valkosia {sum_white} paikka x {num.x} ja y {num.y}  ")

        if sum_black == num.n: # mustia oikea maara
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value == None:
              box.value = 0
          numbers_todo_round2.remove(num)
          togo = True

        elif sum_white == (len(boxes)-int(num.n)+sum_black): # valkoisia oikea maara
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value == None:
              box.value = 1
          numbers_todo_round2.remove(num)
          togo = True

        elif num.n == (len(boxes)-sum_white):
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value == None:
              box.value = 1
          numbers_todo_round2.remove(num)
          togo = True
      # print(len(self.numbers_todo))
      self.numbers_todo = numbers_todo_round2.copy()
      round += 1

    loppu = time.time()
    print(f"vaihe 2 kului aikaa {loppu-alku}")






class Box(FillaPix):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.value = None
    self.number = None

  def set_number(self,number):
    self.number = number

class Number(FillaPix):
  def __init__(self,x,y,n,boxes):
    self.x = x
    self.y = y
    self.n = int(n)
    self.number_boxes = boxes




if __name__ == "__main__":
  peli = FillaPix(15,15,
['0;;;4;3;2;1;;;;;;3;;',
';;5;;;4;;;4;4;;;;;3',
';5;4;5;4;5;5;;5;3;;1;2;;3',
'4;;;;4;;;4;2;;1;;;;',
';;5;4;;2;2;;1;0;;;7;5;',
';;;5;;;0;;;;;4;5;;2',
'4;;;5;4;2;0;0;;;;5;6;;',
'5;;;6;5;;;;;;3;3;3;;3',
';;5;;5;3;;;;;;;3;;',
'5;;;6;5;;3;5;;6;;;0;;0',
';;5;;4;3;2;4;5;;4;;;1;',
';7;;;5;;;1;;5;5;5;;;',
';;6;4;4;4;3;1;2;4;;;6;4;',
';5;;6;;;;;;4;6;;;;',
';;;;;;3;2;0;;4;4;3;;2'])
  peli.make_boxes()
  peli.make_numbers()
  peli.print_table()
  peli.solve_step_1()
  print('vaihe 1')
  peli.print_table()
  peli.solve_step_2()
  print('vaihe 2')
  peli.print_table()


