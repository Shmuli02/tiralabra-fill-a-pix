import time

class FillaPix:
  def __init__(self,xsize,ysize,table):
    self.xsize = xsize
    self.ysize = ysize
    self.table = table
    self.number_completed = {}
    self.boxes = self.make_boxes()
    self.numbers = self.make_numbers()
    
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
    return lista

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
    return all_numbers

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
    for i in range(1,10):
      self.numbers_todo.extend(self.numbers[i])
    # print(self.numbers_todo)
    
    togo = True
    while togo == True:
      numbers_todo_round2 = self.numbers_todo.copy()
      togo = False
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
            if box.number != None:
              if box.number.x == num.x and box.number.y == num.y: # oma numero lisataan tehtyjen listaan
                self.number_completed[box.value].append(box.number)
              else:
                if box.number in self.number_completed[box.value]:
                  pass
                else:
                  pass
                  # print(box.number.x,box.number.y,box.number.n) # numerot jotka box ymarilla
                  # self.numbers_todo.append(box.number) # lisataan todo jonoon
          numbers_todo_round2.remove(num)
          togo = True 

        elif sum_white == (len(boxes)-int(num.n)+sum_black): # valkoisia oikea maara
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value == None:
              box.value = 1
            if box.number != None: # numerot ympärillä
              if box.number.x == num.x and box.number.y == num.y: # oma numero lisataan tehtyjen listaan
                self.number_completed[box.value].append(box.number)
              else:
                if box.number in self.number_completed[box.value]:
                  pass
                else:
                  pass
                  # print(box.number.x,box.number.y,box.number.n) # numerot jotka box ymarilla
                  # self.numbers_todo.append(box.number) # lisataan todo jonoon
          numbers_todo_round2.remove(num)
          togo = True      

        elif num.n == (len(boxes)-sum_white):
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value == None:
              box.value = 1
            if box.number != None: # numerot ympärillä
              if box.number.x == num.x and box.number.y == num.y: # oma numero lisataan tehtyjen listaan
                self.number_completed[box.value].append(box.number)
              else:
                if box.number in self.number_completed[box.value]:
                  pass
                else:
                  pass
                  # print(box.number.x,box.number.y,box.number.n) # numerot jotka box ymarilla
                  # self.numbers_todo.append(box.number) # lisataan todo jonoon
          numbers_todo_round2.remove(num)
          togo = True 
      # print(len(self.numbers_todo))
      self.numbers_todo = numbers_todo_round2.copy()

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
peli.print_table()
peli.solve_step_1()
print('vaihe 1')
peli.print_table()
peli.solve_step_2()
print('vaihe 2')
peli.print_table()


peli2 = FillaPix(60,100,[';;;;0;;0;;;;;;4;;;;0;;;;;5;4;;0;;0;;;;;3;4;;;0;;0;;;;;5;;;;;;;6;;5;;;5;6;;;;;;5;;;;;;;0;;;0;;0;;;;;;;;;;;;5;;;;;;;;;;;;;;',
';0;;;;;;;;0;3;;;;4;;;;;4;;;;;;0;;;3;;;;;;3;;;;;;5;;5;;;8;8;;;6;;;;;;8;;7;;;8;;;3;;;3;;;;;;;;;3;;;5;;3;;;7;;;;9;;;9;;;2;;3;;3;;0',
';;;1;0;;0;;;;;;4;;5;;;;;;5;5;;;;;;3;;;5;;4;;;0;;2;;;7;;;;5;;5;;;;7;;7;7;;;8;8;;;7;6;;;5;4;;3;2;;0;;;2;3;;;6;;7;;;6;7;;8;8;;;8;8;;5;4;;4;5;4;3;',
';3;4;;;;;;2;;;;;5;;;;3;;6;;;;7;;;4;3;;;5;6;;;;;;;;;5;6;;;;6;;;4;6;6;;8;;;;;;;;;5;;3;;3;3;2;;;;0;;;2;2;;;;5;;5;;;;6;6;5;;5;6;;4;3;3;;4;4;;2',
';;;4;;4;4;;;3;0;;2;;4;;3;;6;;7;;7;;4;3;;2;;;;7;;;;;0;;2;;4;;;7;5;3;;;;6;6;;;5;;;;;;4;4;;3;;2;;;;0;;;0;;;0;;0;;;4;5;;5;;;;;;;;;4;3;;;3;3;;;',
';;;;4;;;;;;;;0;3;;3;;2;;7;9;8;;;4;;;4;5;6;7;;;0;;0;;1;;1;;;4;;;;;2;;;5;;;;;;3;3;;4;;2;;;0;;;0;;;;;;3;;;;;1;;;3;;4;;;2;;;3;3;3;2;;;2;2;;;',
'4;6;5;5;4;;3;;4;;0;;;;3;;;4;;5;;;;1;;3;;3;;;5;;;;;3;;;0;;;;;;1;;;;;2;;;3;3;3;3;;;3;2;;;;0;;;;;;;0;2;;4;3;;4;;;2;1;1;;;;;;3;;;;;;0;;;0;;0;',
'4;;;3;3;;;;;;1;;;;;;3;;4;5;;3;;;;4;5;;;3;;;0;;2;;4;;;;;;;3;;;;0;;;;;;;;2;;0;;;0;;;0;;;;;;;;;;;;5;;7;;;;0;;0;;;2;;2;;;2;;;;;;;;',
';;;3;;1;;2;;2;;0;;;;;;5;;;1;;;1;;4;;1;0;;;;;;;7;6;6;;6;;6;6;;;2;;;;;;0;;;0;;;0;;;;;;;;4;;4;;4;3;;2;;4;;;7;;;;;;0;;;4;;;5;;;;;;;;;;3',
';0;;;0;;;;;;;;;0;;;0;;;6;;;;;;;5;;;;0;;;;2;;;;7;7;;7;6;4;;;;;;0;;;0;;;;;;;;;;;;;5;;;5;;;2;;;;;4;;5;;;0;;;;4;;5;;;7;7;;6;;8;7;6;;',
';;;;;;0;;;0;;;;;;;;;5;;5;;;1;;;;5;;;;;0;;;;;3;;5;6;;4;;;;0;0;;;;2;;0;;0;;;;0;;;0;;;;6;;;4;2;;;0;;4;4;6;3;;;;;2;;;;5;6;;;;;;6;6;6;;;2',
';;;;;;;;;;;;0;;;;;;;6;;4;;;;;;;;3;;0;;;;;;;;;;;1;;;0;;;;4;;3;;3;;;;;0;;;;;;;3;;3;4;;;0;;;0;3;3;;;;0;;;;;3;;3;3;2;;;;;;;;;2;',
';0;0;;;0;;;;0;;;;;;0;2;;;;;;6;;;;2;;5;;3;;;0;;0;;;0;;0;;;;1;;;4;;5;;;4;;6;;;;;;;;;0;3;3;6;4;4;;;;;;;;;;3;;;;;0;;;;2;3;;;0;;;0;;;2;;',
';;;;;;;0;;;;;;0;;;;5;;;5;6;;;4;5;;;6;7;;;;;;;;;;;0;;;;;4;5;5;;;;;;6;;8;7;;6;;5;;;;;;;3;;;0;;0;;0;;;;;;;;;;0;;;0;;0;;;;;;;0;;;0',
';;;;;0;;;;;;0;;;;;5;;3;;;;;;4;4;3;3;;;;;;;;;;;;0;;;;4;;5;;;6;7;;6;;;6;;9;;8;8;;;;;7;;;;;;;;;;;;;6;3;3;0;;;;;;;;;;;;;0;;;;;0;',
';0;0;;;;;;;0;;;4;;5;;;;;;;;;;2;;3;;;5;6;;;4;;;2;;;2;4;4;5;;;;;5;5;;6;;;;;;;9;;;;8;9;8;8;7;8;;7;;;;;;;;3;;;;;;;0;;;;;;;0;;;;;;;;;',
';;;;;;0;;;;;4;;;;6;;3;;7;6;;;0;;0;;;1;;;;;4;;4;4;;;5;6;6;;;;7;7;;;;;;7;;;;6;;8;;;;8;8;;;8;9;8;8;7;;;6;;;;;3;;0;;;;;0;;0;;;;;;0;;;0;;;',
';0;;;0;;;;;;5;;;2;;;;;;;;;;;;;;;;0;;0;;;;4;;4;;;8;;;5;;6;;;3;3;;;5;6;;;;;;8;;;7;;7;;;8;8;;;8;9;9;8;8;;;;;;;;;;;;;;;;0;;;;;0;;;0',
';;;;;;1;;5;;;;1;;;4;;3;;9;8;;;6;;;;;;;;;;;0;;;;;5;5;6;6;;;;;6;;;;6;;;7;;;;6;;8;;;;7;;;7;;7;;;8;9;9;;7;;;;;;0;;;;;;0;;;;;;;;;;;',
';;;0;;0;;4;;;;1;;;5;;2;;;;7;;;6;;;6;;;6;;6;;;;3;;;;;;;4;;;5;;3;;3;;3;;;5;6;;;;;6;6;;;8;8;7;;7;;;;;8;9;;;8;;;0;;;;;0;;;;;;;;0;;;;;;',
';0;;;;;;5;;;2;;4;6;5;;;;;;;;;;;;;;;;;6;;;6;;5;;;;;;;;5;6;;;;6;;;;;;7;7;;;;;;4;;;6;;6;;;8;;;;8;9;9;;;;;;;;;;;;;;3;;;;;0;;;0;',
';;;;;;;;;3;;5;5;;5;3;;;8;;;;;;;;0;;;;;;;;6;;6;;6;5;;;;2;;;;4;;5;;3;;;;4;;6;;;;;;;;;;;;;6;6;;;8;;9;;8;;;;0;;;;;0;;;;5;3;;0;;;0;;',
';;0;;0;3;4;;;;5;;;;;;3;;;;;0;;0;;;;;0;;;;;;;;;;6;;;6;;;;;;;;6;;;;;6;;;6;;;8;7;;;;;;;;;;;;;;6;;;8;8;6;;;;;0;;;;;;;5;3;;0;;;;',
'0;;;;;;;;;5;;1;;4;;;;;;7;;;;;;;;;;;0;;0;;;;;2;;;;6;;6;;;2;;;;;4;5;;;3;;;;6;;;7;;9;8;;;6;;;;;;;;;;;;6;;2;0;;;;;5;3;;;;5;;;;;;0',
';;;0;;3;;5;5;;1;;;;;0;;;9;;;;3;;;3;;;;;;;;;;0;;0;;;2;;;;6;;;;2;;2;;5;;6;;;;;;;;;7;;;8;9;;9;8;;;6;;6;;;;;;4;;;;3;;;;;;5;;;5;;;0;;',
';;0;;;4;;;;1;;;6;;;;;;;;;;;;3;;;4;4;3;3;;;;;;;;0;;;0;;;;;6;;;;2;;;;3;;6;;;6;8;7;;;;;;8;;7;;;8;7;;8;;7;;;6;;;;;;;;;5;7;7;;;;;;;;',
'0;;;;;;6;;2;;;;6;;;;;;;;;0;;;0;;;2;;3;;;;4;3;4;;;3;2;;;;;;;;;6;;;;2;;;;5;;;7;;7;7;;;;;;8;;;;;;;5;7;;;7;;;3;;;;5;;;;9;9;;;;6;5;;;0',
';;;;;;5;;;;4;;;;3;0;;;9;;;;;;;;;0;;;0;;;;3;;;4;;4;;;;;0;;;2;;5;6;;;;;;;;4;;7;;;;;0;;;;7;;8;6;;;;;;;;6;;;;5;;;9;;9;;;9;6;;;;;;',
';;;0;;4;;;5;;;;;;;;;6;;;;;0;;0;;;;;;;;0;;0;;;;;4;;;4;;;;;0;;;;;6;6;5;;;;;;;;;6;;;;;;;;;;;;;;;7;7;;;4;;;9;;;;6;;8;;5;;;7;;;0',
';0;;;3;;;;;;;0;3;;3;;;;;7;;;3;;;;;;;0;;;;;;;;;;;;;4;4;;;;;;1;;;;;6;;5;;;;;;;6;;;7;;;;;8;;;;0;;;7;;;;;8;;6;5;;;5;7;;6;;5;;;;;',
'0;;;0;;;7;5;;;0;;;;;;;;9;;;;3;;3;;4;;;;;;;;;;0;;;;;1;;;;4;;4;4;;;;;2;;;6;;5;;;2;;;;7;;8;;6;;;7;;;;;;;;;;;;;;4;;;4;;4;;;;4;;;;',
';;;;;;;;;;;;6;;;0;;;9;7;;;;;;;;4;;3;;;4;;3;;;;0;;;;;0;;;;;4;;4;;;1;;;;;6;;5;;2;;;;;6;;8;9;;;;;;7;;7;7;5;;;;;;;4;4;;;;;;;;;7;6;',
';;;0;3;;;;1;;;;;;;;;;;7;;;;;;0;;;;;;;4;4;;;;;;2;;;0;;;;0;;;;4;5;4;;;1;;;;5;;6;;;;;;;;;;;;9;;9;;;9;;7;;;3;3;;;;;;;;;5;;;;7;;',
'0;;;;;3;;;;4;;;;;;;;;;;5;;;0;;;0;;;0;;1;;;3;;;4;4;;;;;;0;;;;;;;;4;;4;;;1;;;;5;6;;5;;;;;2;;;5;;;6;;;6;;;4;;;3;;2;;;;4;5;4;4;;;6;7;;',
';;;;;;;;;;2;;3;;3;0;;;8;9;7;;;;;3;;;;1;;;0;;;1;;;;;;4;;;;;;0;;;;1;;4;;5;;;;1;1;;;;;5;5;;;;;;;3;3;;;;;3;;;1;0;1;;;;4;;4;;;4;4;;;;8;6',
';0;;0;;4;;4;;;1;;;5;;;;;;9;;;3;;;3;;4;;4;;;3;;;;;0;;;;;4;;;4;;;2;;0;;0;;;;;5;;;;;2;;;;5;5;;;;5;;;;;;;;;3;;;3;;;;;4;;;;4;4;;;;7;8;',
';;;;;;5;;;1;;4;5;5;;2;0;;;;8;;;;;6;;;;;;3;;;;3;;2;;;0;;;;;;;;4;;3;2;;;0;;;;;;4;;;;3;;;;;;5;5;;3;;;3;3;;3;;3;;3;;4;;;;;4;;4;4;;;6;;;',
'0;;;;0;;;;1;;4;;;;4;;;;6;;;;;2;;;2;;;;;6;;;4;3;4;4;;;3;;;0;;;3;;;4;;4;;;2;;0;;;;;;4;3;;4;;;3;;;6;;;;;;3;;;;;;;;;;4;4;;4;;;;5;;6;;8;6',
';;;0;;;4;;;3;;;1;3;;;;;;8;9;;;;3;3;;;0;;2;;;;3;;;4;;3;;;;;3;2;;;2;;;;4;;4;;3;;;0;;;;;;7;;4;;;;;;4;;;3;3;;;;;;;;4;;4;;;3;;3;4;;;;7;8;',
'0;;;;0;2;4;;;;;0;;;6;5;;;;;;;6;;;;;;;;3;;2;;0;;;;;6;;5;;3;;4;;3;;;;2;;;4;4;;4;;;;;;4;;;5;;;3;;3;;4;;4;;;;;3;;3;4;;4;;;;2;;2;4;;6;6;;;;6',
';;;0;;;;5;;;1;;4;;7;;3;;;6;9;9;;;;3;;3;;2;;;;;;;;;2;;;;;;6;;4;3;;4;;3;;;3;;;4;;;;5;;4;;;;;3;;;;;;3;;5;;6;;;6;6;;;3;;2;;;;5;;5;;5;;;8;',
';0;;;;;;;;;3;;5;4;5;;;;;;;;8;;;;;;;;;2;3;;3;2;;;;;;1;;2;;;;;;5;4;3;4;4;;;;;;7;;5;;;;5;;;;;;6;;;2;;;;4;;;4;;3;;;;;6;;;5;;5;;;;8;8;',
';;;4;;3;4;;5;;;5;4;;3;;4;;1;;;9;;5;;;6;6;;;;;;;;;;;3;;;;;;;;;2;3;3;;;;4;;;6;;;;;;;5;;;9;;7;;;6;;;;3;;;3;6;7;;6;;;7;;6;;;5;6;;;;6;;8;;',
';;;;;3;;;;;5;3;;;;;;;;;;;9;;;;9;9;8;;;6;;;6;;;;;;;2;;3;2;;;;;4;;;;;;7;;5;;;;5;;;9;;9;;;;;;;5;6;;;;1;;;;5;4;;;;7;7;;;;;7;;8;;;;2',
'0;3;4;;;0;0;;3;;;;;3;3;;;;;;;;;;;;6;;6;;;7;;9;9;;7;;;5;;;;;4;;2;;;3;;;6;5;;4;;;;;7;;9;;;9;;;5;;;;;;;3;;;0;;;6;7;7;;;;;;7;;;8;8;8;7;;;;',
';;4;;2;;;;;;;;2;;;;;6;;1;;;8;9;;;;;;;;;;;;;6;7;8;;7;;;6;;;5;5;;;;7;;5;;;;;7;;7;;;;6;;;;;5;;;3;2;;;;;;;;;;;6;;;7;;9;;;7;;;;6;;;',
'0;;;5;;5;6;;;;3;;;;4;5;;;5;;;;;9;;;;;6;;;7;;;;;;;;7;6;;;7;7;;6;;;;5;4;;;;;6;;6;;;;;;;;;3;;;;4;;;;0;;;;0;;;3;;8;;8;;;;;;;;7;;;;0;',
';;;;;5;7;;6;;;;;;;;9;9;7;;;;5;;9;7;;;8;;;9;;7;;;;7;;;;;;;7;;7;7;;5;;;;;6;;5;;;;;5;;;;;;;;;1;;;;;;;;0;;;;;;;9;;;;;;;7;;7;;;3;;',
';;;;6;;6;7;;6;;;;8;9;;8;;;4;;;;;9;;;;;;;;9;;9;;;9;;7;;;6;;;;;7;;;;;6;;5;;;;;;;;9;;9;;9;;6;;;5;6;;;;;;;;;;;;5;;;7;;;8;8;;;;;4;;;',
'4;;5;;3;4;;;8;;5;;;8;;7;;;;;;;;5;;;7;;6;7;;;;;8;9;;;9;;;9;;9;8;6;;;;6;6;;5;;;;;;8;;9;;;;;;;;;4;;;9;;;5;;;;;;4;;;;7;9;;9;;7;;;;;7;7;;;6',
'6;;8;;;;4;5;;8;7;;;;;7;;;6;7;6;;;;7;9;;;;;;;;;;7;;;8;;;;9;;;6;;;;;5;;;;;7;;;;;;;;3;;;3;;;;;;;;;7;;6;6;;8;;;;;;;;6;6;;;6;7;;8;;6;;4',
';9;8;;;;;;;;;5;;;5;;7;;9;;;;;;;;9;7;;;;6;;;;;;;;9;;;;;4;3;3;3;;;5;;;6;;;5;;;3;;3;;3;;;;;;;;;;;;;;7;;9;;;7;;;;;;;;4;4;;6;;;9;;;',
';;9;8;7;;;;;;;;4;3;;;8;;7;;8;7;;;;7;9;;;;8;;;9;;7;;;6;6;5;;;2;;3;;;5;4;4;;;;;3;;;;;3;;;3;;;2;;0;;;0;;0;;;;;;;;9;9;8;;8;;5;;3;;;;;;5;;;;4',
';;;9;8;7;;;6;5;;3;;3;3;;5;6;;;8;;6;;;;8;9;8;;;9;9;;;;;5;;;3;;;;4;4;;3;;;;3;;;;;;;;3;3;;;;;;;;;;;;;;;0;;;2;;;8;9;9;8;;;;;;;;0;;;;;;5;',
';9;;;8;;;;7;;;3;;;;;;;3;;6;8;;;;;;;9;;7;;;5;;;3;;;3;;;4;;;4;;;3;;3;3;;;4;;4;;;;;2;;;;;6;;6;;;6;;;;;;0;;;;7;;6;;;;2;;;;;;;;;;;;',
';;8;;;3;;;;6;;;3;;;4;4;;;6;;;9;8;;;;;;;;;;;;;3;;;4;4;;;;;;1;;2;;4;;4;4;;;;2;;;;;;;7;;7;;;;;7;;7;;;;;;5;6;;;;;;;;;;6;;;;;5;;;;1',
';;;;;;;0;;3;6;7;;;;;;4;;;7;;;;9;;8;;9;;7;;;3;;;3;;;;;;;0;;;;;;;;;;;;1;;3;;;6;6;;;6;;;;;;;;;6;;;3;3;;;;;;;;;6;;;9;;9;;;9;;;6;;',
';9;;;;;;;0;;;;;6;;;5;;;5;;;8;9;;;9;;;;;;;;;;;;2;1;;;;;4;;;4;;;2;;;2;;;;;;7;;6;;;;;;6;6;;;;;;6;;;;;;;;;6;;;9;;;;;;;;;;;9;;',
';;9;;7;;;;;;;;;;6;;6;;;;;;;;;;;;;3;;;;0;;;;;;;;5;;;;4;;;;;;;;;;;;9;;;;;;6;;;8;9;;9;8;;;6;;6;;;6;;6;;;9;;;;;;;;;;;;;;;;6',
';6;;;;6;5;;;2;;0;;;;;6;;4;;;4;5;5;;;3;;;;;;0;;;0;;2;;;4;5;5;;;;;0;;;2;3;;;6;;;;;;4;;;5;6;;;;;;6;;;6;;;6;;;6;;6;;;;6;;6;;6;;6;;6;;;6;;;'])
peli2.print_table()
peli2.solve_step_1()
print('vaihe 1')
peli2.print_table()
peli2.solve_step_2()
print('vaihe 2')
peli2.print_table()
