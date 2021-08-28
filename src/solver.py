import time
import sys
from itertools import combinations
import copy

class FillaPix:
  def __init__(self,xsize,ysize,table):
    self.xsize = xsize
    self.ysize = ysize
    self.table = table
    self.number_completed = {}
    self.boxes = []
    self.numbers = {}
    self.numbers_todo = []
    self.numbers_todo_main = []

  def make_boxes(self):
    # alku = time.time()
    lista = []
    for i in range(self.xsize):
      lista2 = []
      for j in range(self.ysize):
        lista2.append(Box(i,j))
      lista.append(lista2)
    # loppu = time.time()
    # print(f"latikoiden tekemiseen kului aikaa {loppu-alku}")
    self.boxes = lista

  def make_numbers(self):
    # alku = time.time()
    all_numbers = {}
    for num in range(0,10):
      all_numbers[num] = []
      self.number_completed[num] = []
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
          for box in boxes:
            box.add_number_around(new_number)
    # loppu = time.time()
    # print(f"numeroiden tekemiseen kului aikaa {loppu-alku}")
    
    self.numbers = all_numbers
    # return all_numbers

  def fill_table(self,table):
    for x in range(len(table)):
      for y in range(len(table[x])):
        self.boxes[x][y].value = table[x][y]

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
    # for i in range(1,9):
    #   self.numbers_todo.extend(self.numbers[i])
    self.numbers_todo_main.extend(self.numbers[1])
    self.numbers_todo_main.extend(self.numbers[8])
    self.numbers_todo_main.extend(self.numbers[2])
    self.numbers_todo_main.extend(self.numbers[3])
    self.numbers_todo_main.extend(self.numbers[4])
    self.numbers_todo_main.extend(self.numbers[5])
    self.numbers_todo_main.extend(self.numbers[6])
    self.numbers_todo_main.extend(self.numbers[7])
    
    self.numbers_todo = self.numbers_todo_main
    self.numbers_todo_main = sorted(self.numbers_todo_main, key=lambda x: x.x)



  def solve_step_2(self):
    # alku = time.time()
    self.numbers_todo = self.numbers_todo_main
    # for i in range(1,9):
    #   self.numbers_todo.extend(self.numbers[i])
    # self.numbers_todo = sorted(self.numbers_todo, key=lambda x: x.x)
    # print(self.numbers_todo)

    togo = True
    round = 1
    while togo is True:

      numbers_todo_round2 = self.numbers_todo.copy()
      togo = False
      remove_todo2 = []
      # print(f"kierros {round} numeroita {len(self.numbers_todo)}")
      # print(len(self.numbers_todo))
      for i in range(0,len(self.numbers_todo)):
        num = self.numbers_todo[i]
        boxes = num.number_boxes
        sum_black = 0
        sum_white = 0
        for box in boxes:
          if box.value == 1:
            sum_black += 1
          elif box.value == 0:
            sum_white += 1
        # print(f"numero {num.n} mustia {sum_black} valkosia {sum_white} paikka x {num.x} ja y {num.y}  ")

        if sum_black == num.n: # mustia oikea maara
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value is None:
              box.value = 0
              togo = True
          remove_todo2.append(i)
          

        elif sum_white == (len(boxes)-int(num.n)+sum_black): # valkoisia oikea maara
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value is None:
              box.value = 1
              togo = True
          remove_todo2.append(i)
          

        elif num.n == (len(boxes)-sum_white):
          # print(sum_black,sum_white,num.n,num.x,num.y)
          for box in boxes:
            if box.value is None:
              box.value = 1
              togo = True
          remove_todo2.append(i)
          
      # print(len(self.numbers_todo))
      for i in range(0,len(remove_todo2)):
        numbers_todo_round2.pop(remove_todo2[i]-i)
      self.numbers_todo = numbers_todo_round2.copy()
      round += 1

    # loppu = time.time()
    # print(f"vaihe 2 kului aikaa {loppu-alku}")



  def table_ready(self):
    for i in range(len(self.boxes)):
      for j in range(len(self.boxes[i])):
        if self.boxes[i][j].value == None:
          # print('ratkaisu kesken')
          return False
    print('ratkaisu valmis')
    return True
     

  def check_table(self):
    errors = []
    for i in self.boxes:
      for j in i:
        test = self.check_box(j)
        if test is not True:
          errors.append(test)
          return False
    if len(errors) == 0:
      # print('Kaikki kunnossa')
      return True
    else:
      # print('Taulussa ongelma')
      # for error in errors:
        # print(f"numero {error.n} paikassa {error.x} x ja {error.y} y")
      return False

  def check_box(self,box):
    numbers_around = box.numbers_around
    result = True
    problem_numbers = []
    for number in numbers_around:
      black = 0
      white = 0
      for num_box in number.number_boxes:
        if num_box.value == 1:
          black += 1
        elif num_box.value == 0:
          white += 1
      if black > number.n:
        result =  False
        problem_numbers.append(number)
        return False
      elif white > (len(number.number_boxes)-black):
        result =  False
        problem_numbers.append(number)
        return False
    if result is True:
      return True
    else:
      # print('laatikko ei oikein')
      if len(problem_numbers) == 0:
        return True
      else:
        return problem_numbers

  def make_snapshot(self):
    snapshot = []
    for i in range(len(self.boxes)):
      line = []
      for j in range(len(self.boxes[i])):
        line.append(self.boxes[i][j].value)
      snapshot.append(line)
    return snapshot

  def solve_step_3(self,snap,k,muokatut):
    # alku1 = time.time()
    self.fill_table(snap)
    # self.numbers_todo = todo
    self.solve_step_2()
    if self.check_table() is False:
      # print(f"ei onnistunut. numero {muokatut[-1]} aiheutti ongelman")
      muokatut = muokatut[:-1]
      # self.fill_table(snap)
      return False
    if self.table_ready() is True:
      print('VALMIS')
      print('VALMIS')
      print('VALMIS')
      print('------------------------------------------------------------')
      print('------------------------------------------------------------')
      print('------------------------------------------------------------')
      self.print_table()
      self.step3_loppu = time.time()
      print(f"kolmos vaihe kesti {self.step3_loppu-self.step3_alku}")
      exit()
      return self.table
    else:
      if len(self.numbers_todo) != 0:
        num_to_try = self.numbers_todo[0]
        # self.numbers_todo.pop(0)
        # print('UUSI')
        uudet_snap = []
        uudet_muokatut = []
        none_laatikot = []
        mustat = 0
        for i in range(0,len(num_to_try.number_boxes)):
          if num_to_try.number_boxes[i].value == None:
            none_laatikot.append(i)
          elif num_to_try.number_boxes[i].value == 1:
            mustat += 1
        possible_fills = list(combinations(none_laatikot,(num_to_try.n-mustat)))
        for fill in possible_fills:
          for fill_box in fill:
            num_to_try.number_boxes[fill_box].value = 1
          kunnossa = True
          for boox in fill:
            if self.check_box(num_to_try.number_boxes[boox]) is not True:
              # print('tarkistu tulos False')
              kunnossa = False
              break
          if kunnossa is True:
            new_snap = self.make_snapshot()
            uudet_snap.append(new_snap)
            uudet_muokatut.append((num_to_try.x,num_to_try.y))

            # print(num_to_try.x,num_to_try.y)
          for fill_box in fill:
            num_to_try.number_boxes[fill_box].value = None
        if len(uudet_snap) > 0:
          # print(f"Muokatut numerot {muokatut} kierros {k} numeroita vielä {len(self.numbers_todo)}")
          for uu in range(len(uudet_snap)):
            muokatut_laatikot = muokatut.copy()
            aa = list(uudet_muokatut[uu])
            aa.append(uu+1)
            aa.append(len(uudet_snap))
            # todo2 = copy.copy(self.numbers_todo)
            muokatut_laatikot.append(tuple(aa))
            
            self.solve_step_3(uudet_snap[uu],k+1,muokatut_laatikot)
        else:
          # print('ei uusia muokattavia')
          return False
      else:
        print('!!! todo lista tyhjä !!!')
        return False
    
  def main(self):
    self.make_boxes()
    self.make_numbers()
    # peli4.print_table()
    self.solve_step_1()
    print('vaihe 1')
    self.print_table()
    self.solve_step_2()
    print('vaihe 2')
    self.print_table()
    self.check_table()
    self.step3_alku = time.time()
    self.solve_step_3(self.make_snapshot(),0,[()])
    
class Box(FillaPix):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.value = None
    self.number = None
    self.numbers_around = []

  def set_number(self,number):
    self.number = number
  
  def add_number_around(self,number):
    self.numbers_around.append(number)
  
class Number(FillaPix):
  def __init__(self,x,y,n,boxes):
    self.x = x
    self.y = y
    self.n = int(n)
    self.number_boxes = boxes




if __name__ == "__main__":
  # peli = FillaPix(15,15,['0;;;4;3;2;1;;;;;;3;;',
  # ';;5;;;4;;;4;4;;;;;3',
  # ';5;4;5;4;5;5;;5;3;;1;2;;3',
  # '4;;;;4;;;4;2;;1;;;;',
  # ';;5;4;;2;2;;1;0;;;7;5;',
  # ';;;5;;;0;;;;;4;5;;2',
  # '4;;;5;4;2;0;0;;;;5;6;;',
  # '5;;;6;5;;;;;;3;3;3;;3',
  # ';;5;;5;3;;;;;;;3;;',
  # '5;;;6;5;;3;5;;6;;;0;;0',
  # ';;5;;4;3;2;4;5;;4;;;1;',
  # ';7;;;5;;;1;;5;5;5;;;',
  # ';;6;4;4;4;3;1;2;4;;;6;4;',
  # ';5;;6;;;;;;4;6;;;;',
  # ';;;;;;3;2;0;;4;4;3;;2'])
  # peli.make_boxes()
  # peli.make_numbers()
  # peli.print_table()
  # peli.solve_step_1()
  # print('vaihe 1')
  # peli.print_table()
  # peli.solve_step_2()
  # print('vaihe 2')
  # peli.print_table()
  # peli.check_table()


  peli2 = FillaPix(50,80,[';;;;1;;2;;;;;;1;;4;;;;;4;;6;;4;;;4;5;;4;3;;;3;;2;;;1;;0;;3;;;;;;3;3;;;;;;3;;1;;;4;;;0;;;;3;;2;;;1;;;2;;;;',
';5;;5;;;;;2;;2;;;;;;;3;;;;;;;;;;;;;;;;;;;;;;;;3;;;3;2;;;;;;3;3;;;;3;;;;4;4;;;;3;;;;3;;3;;2;;;5;;;2',
';;4;;3;3;3;;;2;;3;;3;4;3;;3;;2;;3;;1;3;;4;;2;2;;3;;1;2;;3;;;2;;3;3;2;;;;3;;1;;3;;;0;3;;;3;;;3;3;;3;;;1;;;3;;;2;2;3;;4;;',
'3;;2;;3;4;;3;3;2;2;3;;2;2;;;;5;3;;;1;;;4;;;;;;;;;4;;3;4;3;;;;3;1;2;3;;;;;;1;;;;;;5;;;;3;;6;3;3;2;;3;;1;;;;;;5;2;;3',
'3;;;;3;;2;;2;;2;;3;;;;;;;4;3;;;3;;5;;2;;4;;;3;;;4;;3;;3;;3;;;;;3;;;4;3;;2;;;;;;3;2;;;;;;;;;5;2;;3;;;;;;4;;',
';5;;5;2;;1;3;;2;3;3;;;3;;;4;;;;0;;;5;;4;;;;;3;;;;3;3;2;;;;;;5;;3;;;;;;3;;;6;5;;;;;3;;;;;;;;5;;;;;2;;3;5;;;',
';;7;;;;;3;;2;;;;4;;;;4;6;;;;;5;;;;;6;5;6;;7;;3;;;;1;;;;;;;;;5;;;4;;;;;6;;4;4;;4;5;4;6;;5;;3;3;;4;3;;;2;;;7;5;',
';5;;5;2;;1;;1;3;;;8;6;;6;;;;4;6;;7;5;;3;;8;;;;;;;;1;;;;3;;7;;;;;7;;3;3;;7;7;5;;;7;;;;;;;;;;;;;3;;;2;2;;;5;;;',
';;;;;;2;;;;;;;;;;9;;;;;;9;;;;7;;;;;6;9;;;;6;;;;;9;7;;;8;;;;;;9;;;;6;9;7;;;8;9;;;;9;6;;;;5;;2;1;;;;;;3',
'3;;2;;3;;;;1;;;;9;8;;;9;;;;6;9;8;;;;;;9;;;;;;;;;8;;6;;;;;;9;;;;;6;;9;;;;;7;;;8;;;;6;9;;;;;8;;3;;3;3;;2;;3',
';5;;;;;;;3;4;;9;;;;;;8;;;;;;;;6;8;;7;;6;;7;8;8;;;8;;;;;9;;;;9;7;;;;9;8;;;;8;5;;;;9;;;;;8;;;9;9;7;;;2;3;;;;',
';5;;6;3;;1;;;;8;;6;;;4;;8;;;;7;6;;;;;;;;;;;8;9;9;;;;;9;9;;;;6;;;;;;;;;;5;;;;;5;;6;;;;;;9;;7;;;;2;3;6;;;2',
';;6;;;;;;;6;;6;;;4;;;;7;;;;;;1;;;;;;;;;6;6;;;;;6;9;;;;;;;8;6;;;;;;;;;;2;;;7;;;2;;;5;;5;;;2;;;4;;6;;',
';;;3;;3;;0;;4;;;;5;;5;;;;;;;;;;;;2;;;1;1;2;;;;2;;;;;;3;;;;;6;;;;7;6;;;;6;6;;;;5;5;;;4;;;3;;;;;;3;;3;;;2',
';4;;;;3;;;;;;;;;4;;;;6;;;3;3;0;1;2;;5;;2;;;;;;;1;2;;;;;;;1;0;;;;2;;;6;;4;6;;9;8;;;;;;5;;5;;;;;4;;3;3;;;;;',
';;5;;4;;;;3;;;;3;;2;;3;;3;3;;;;;3;;6;;;;3;;2;;3;1;;;;8;;;1;2;;;0;;;;;3;;3;;7;8;;6;;;;;4;;4;;;;;;3;3;;;4;;5;4;2',
';;;;;4;4;;;;5;;4;;;3;2;2;;;2;;;1;2;4;;;6;;2;1;;;3;;2;;;;3;1;;;2;;;;;0;;;;;;6;7;;;6;;4;;3;4;;;4;;5;;5;;4;4;;;;;',
'1;;2;3;;;;;2;4;;;;3;;2;;;;1;1;;;;;4;6;6;6;;;;;;;;1;3;3;3;;2;;;;;;;;;;;;;;6;;;;;5;5;;3;3;;;;6;;4;2;3;;;4;;2;;',
';;2;2;;3;4;;;;5;3;3;;;;;;;2;2;3;;;;2;;5;;2;2;;;2;;2;2;2;2;;;3;2;;1;;3;;;;;7;;7;5;;5;;;;5;;3;;;4;4;4;;;;;;4;;;2;2;;2',
';3;;1;2;2;;;3;;;1;;1;;;1;;0;;;4;3;2;;;;;;;;2;;4;;2;1;;;3;;;;;3;;;6;;;8;9;6;;;;;7;7;7;5;;5;;;;3;;2;;3;3;;;2;;1;;;3',
'4;;4;;2;1;;2;;;;;;;;;;4;;3;;3;;;1;;1;;;0;;;5;;5;;3;;2;;3;;;3;;3;4;;4;;;9;;6;;;;7;8;;;6;;5;;;1;;;;;;3;;1;2;;;;3',
'5;;3;1;;;;0;;1;3;;;2;;5;;;;3;;;;;;4;3;;;;1;3;;5;;4;2;;;;;3;;;;;3;4;2;3;5;;;;6;8;7;;6;;;6;9;;;;;;0;;0;;;1;;;1;3;;',
'5;;;;;;2;;;3;;4;;;5;7;;4;3;;3;;3;;3;;3;3;;;2;;5;;5;;3;2;;;;;3;;2;;2;2;2;;;;;;;;8;;;;;;9;8;5;3;;;;;;0;;;2;;;3;;3',
'4;5;;;0;;;1;;;4;;;;4;;3;;2;3;5;6;;;6;;6;5;4;;;2;;4;;3;;2;;;1;;1;2;;;;0;;1;;;6;6;7;;9;;;;;;8;7;;;;0;;1;;;;0;;2;;5;;3',
';;3;;;0;2;;;;;4;;;3;;;;;4;4;4;;3;;;3;4;4;4;;2;;3;4;2;;;;1;;;;;1;0;0;;2;;;5;;;;;;9;6;;;6;;;;5;3;;;;2;;;;;;5;5;;4',
';;3;2;;1;1;;;1;;;;1;2;3;;3;4;;6;;4;4;;6;;;4;;4;;3;2;;;;;1;;;1;;0;;;1;;3;;;;7;8;9;;;;;;6;7;;;4;;5;3;3;2;;;;;;;;;6;4',
';1;;2;;;;;;1;;3;;3;;;;;;;;4;2;2;;;5;4;;4;;4;;2;1;;;;;2;;;;;;1;;3;;3;;;;7;;;;9;6;;;7;;;;;4;4;;4;;3;;1;;1;;3;;4',
';;;2;1;;;2;;;;4;;3;4;4;;3;;;;;3;;;5;;3;2;;4;;4;;1;;;1;2;2;;;2;3;1;;1;2;;;;;;;7;9;;;;;;;;;;;;;;;;;;2;;;;2;;',
'2;;1;;;2;;1;;;;4;;;;5;;3;;3;3;;;4;4;;3;;;;;5;;4;;1;0;1;1;;;;;;3;;;3;;;;;1;;6;;;7;;6;;;;5;2;;;4;;5;;;2;;;;1;2;;2',
'3;;2;2;;;0;;;;3;;;2;5;;;;3;;;3;;;;3;;0;;;2;;6;;;;1;0;;;;;;;;;;;1;;2;2;;;;7;9;;;;7;;6;;;2;;;5;;;4;;2;;;;1;;',
';;;2;;1;;;5;;;;3;;;;5;;;3;;3;4;5;5;;4;;;3;;;;6;;3;;1;0;;3;;4;;2;;1;;;3;;2;;;;;;;;;;;;;;;;2;;4;4;3;;1;;0;;;;1',
'3;;2;;;;3;;;4;4;;5;4;;5;;;;3;3;3;;;;4;;;3;;;4;;4;;;3;;;;1;;;2;;;;;3;3;;;;;6;;;6;;;9;6;;6;6;;;;3;2;3;;;;;;0;;;1',
';;2;2;2;;;3;;5;;7;6;;4;;4;2;;;;;;3;;;6;;6;;6;;;;;;;;;;;3;;;;5;;;;6;5;;;7;;;6;6;;6;9;;;;6;;0;;;;;1;;1;;2;3;3;;2',
';2;;;;6;;;3;;4;;5;6;;;;1;0;1;3;3;;;;;;;;;3;3;3;;;5;;6;4;2;;;2;;;5;6;;;;6;;;;7;;;;;;6;;;4;5;3;2;;2;;;;0;;;5;;3;;1',
';;4;5;;4;2;;;4;;;5;;;;;2;3;2;3;3;3;;2;;;3;;;;;;;;6;;;5;;;;;5;;6;;5;;;;5;;6;;5;;5;;;;;;;;4;;3;3;4;;;;;4;5;5;4;;',
';;;;;;4;5;;;3;;;;2;;;;;;;;3;;3;;3;;;;;4;;5;;;6;;5;3;;;3;;6;;;;6;6;;;;;;;;5;6;;;;5;;;5;6;;;;7;7;;5;;;3;;;',
';7;;3;;3;4;;;;;3;;;;;;;6;;4;;;;3;;3;4;;4;;;5;;5;;5;;4;;0;;;;5;;;4;;6;;;;2;;;2;2;;4;4;;;5;;4;;;;4;5;;5;;;1;;2;;2',
';;6;;;3;;;;;;;;;;;8;;;;5;5;;;;4;;;6;;;3;;;;;;;;;;;;;6;;;;;;;;6;;5;;;;;;;5;6;;;;6;;;;;;;;;;;;;',
';6;;6;;;;6;;8;9;8;6;;;6;8;;;8;;;;;;;;4;;3;1;;;3;;;3;4;;;;;;4;;;4;;3;4;;;4;;;4;;6;5;;;;;3;;;;6;;;3;3;4;;;3;;;;3',
'2;;;;6;;4;;;;;;;;;6;7;;7;;8;6;;6;;;;;;;1;1;3;;3;;4;;;7;7;;5;;;6;;;;6;6;;;5;;;;;6;;;5;;;;;6;8;;;;;;;;;;7;;3',
'2;;4;6;;7;;;5;5;;;7;;;;;6;;5;;;;;;;2;;3;;0;1;2;3;;;;3;3;;;;3;3;3;;;2;2;;;;3;;3;1;;;;1;;;;2;;;;;8;;2;;;5;;;2;;;3',
';4;3;;6;;6;;4;;;6;;3;;;;;6;;6;;8;7;;;;;;;;0;2;2;;;;;;;5;;3;;;;6;;3;;6;;;;;;;;2;1;3;;3;;;3;;5;;6;;;;6;;2;;7;;',
';;4;;4;;;7;;;3;5;;;2;;3;4;;5;;7;7;;;;8;8;;5;;;;3;;3;;;3;3;;;;3;2;;5;;;;;;3;;3;;;;;;;;;2;;;;;6;;3;3;;;;1;;;;',
';4;;4;3;4;6;;6;;;;;3;;3;;;;5;;;5;;;7;8;9;8;7;;;4;5;;;5;6;;;;6;;;;6;;;;;7;;;5;;5;;8;;;;;;;;6;;;;6;;;;7;;;;7;5;3',
'2;;4;4;4;3;;;;6;;;2;;;3;;4;;;;;;5;5;6;;8;;6;4;;5;;;;;6;;;6;;;;;5;6;5;;7;;;4;;;;;7;;;6;;6;;;8;7;;6;;;;8;7;;;;;;',
';;3;4;;5;;;6;;6;3;;;3;;;4;;4;;;;4;;;4;;3;;;6;;;;;;;;;;;6;7;;;;;6;7;;;;;7;6;;;6;;8;;;;;;7;;;;6;6;;;6;;6;;;',
';3;;3;5;;6;;;6;;6;;;;;;;;;;;4;4;3;;2;;;;;;7;5;3;3;;4;2;;4;;;;;;5;;;6;8;;;;;;;;;4;;7;;5;;;;3;5;;;;;;;3;;4;4;3',
'2;;3;;4;6;;6;;;6;;6;;3;4;;5;4;5;;;5;4;4;;4;;;;6;6;7;;;;;;;6;;;3;;2;;;;;6;;;;3;;2;;3;;;8;;;5;8;;;;;3;;;;4;;;5;;;',
';;;3;;;;;;;;;;;;;4;;;;;4;;;;;;6;;;;5;;;2;;3;;4;;;;;;;;;;;;;6;;3;;2;;;;;;;;;;;;;;;;5;8;;6;;;;;',
';2;2;2;;2;3;;5;3;;;5;5;;2;;3;4;4;;4;4;;3;;5;6;5;;3;;3;2;;;;;;6;4;;;4;3;4;2;3;;;6;;;;;;4;2;;;5;5;4;;;2;4;2;;2;;4;;4;;2;3;3;3;'])
  # peli2.make_boxes()
  # peli2.make_numbers()
  # # peli2.print_table()
  # peli2.solve_step_1()
  # print('vaihe 1')
  # # peli2.print_table()
  # peli2.solve_step_2()
  # print('vaihe 2')
  # # peli2.print_table()
  # peli2.check_table()
  # alku = time.time()
  # peli2.solve_step_3(peli2.make_snapshot(),0,[()],peli2.numbers_todo)
  # loppu = time.time()
  # print(f"kolmos vaihe kesti {loppu-alku}")
  # # peli2.print_table()

  peli3 = FillaPix(20,20,[';;;;1;;2;;;;;;1;;4;;;;;2',
';5;;5;;;;;2;;2;;;;;;;3;;',
';;4;;3;3;3;;;2;;3;;3;4;3;;3;;1',
'3;;2;;3;4;;3;3;2;2;3;;2;2;;;;5;3',
'3;;;;3;;2;;2;;2;;3;;;;;;;4',
';5;;5;2;;1;3;;2;3;3;;;3;;;4;;',
';;7;;;;;3;;2;;;;4;;;;4;6;',
';5;;5;2;;1;;1;3;;;8;6;;6;;;;2',
';;;;;;2;;;;;;;;;;9;;;',
'3;;2;;3;;;;1;;;;9;8;;;9;;;',
';5;;;;;;;3;4;;9;;;;;;8;;',
';5;;6;3;;1;;;;8;;6;;;4;;8;;',
';;6;;;;;;;6;;6;;;4;;;;7;',
';;;3;;3;;0;;4;;;;5;;5;;;;',
';4;;;;3;;;;;;;;;4;;;;6;',
';;5;;4;;;;3;;;;3;;2;;3;;3;3',
';;;;;4;4;;;;5;;4;;;3;2;2;;',
'1;;2;3;;;;;2;4;;;;3;;2;;;;0',
';;2;2;;3;4;;;;5;3;3;;;;;;;1',
';2;;1;2;2;;;3;;;1;;1;;;1;;0;'])
  # peli3.make_boxes()
  # peli3.make_numbers()
  # # peli3.print_table()
  # peli3.solve_step_1()
  # print('vaihe 1')
  # # peli3.print_table()
  # peli3.solve_step_2()
  # print('vaihe 2')
  # # peli3.print_table()
  # peli3.check_table()
  # alku = time.time()
  # peli3.solve_step_3(peli3.make_snapshot(),0,[()],peli3.numbers_todo)
  # loppu = time.time()
  # print(f"kolmos vaihe kesti {loppu-alku}")
  # # peli3.print_table()

  peli4 = FillaPix(20,20,['4;;;6;;;;6;;;4;;4;;;1;;;3;',
';;9;;8;;9;8;;;;;;2;2;;6;;;3',
'6;;;;;7;7;;;2;;1;2;;2;4;6;8;;4',
'5;;;;3;;;;3;;;;0;;;;;;7;',
';;1;;;;;;;0;;;;;;;5;5;;4',
';;;;;0;;;1;;;;;;;4;;6;;4',
';0;;;;3;;;3;;2;;2;;1;3;4;;;',
';;;6;;;;;3;4;;;5;;;;6;;;',
'0;;;8;;;3;;4;;6;8;6;;;;;8;;3',
';;;;6;4;;2;3;;;;;7;6;;7;9;;',
';;;;;5;;;;5;;6;7;;;;5;7;;4',
';7;8;;8;;;;;;4;;;6;;;;6;;',
';;;7;;;7;;;5;;;;;;1;;;6;',
'5;;;;;;;;3;3;;6;;;5;;;;;',
';;7;;7;;;;5;;;;7;;3;;3;;;5',
';5;;7;;;;1;;1;;;7;;;;;;;',
';5;;;;4;5;;;;;;;;1;;2;5;;3',
';7;9;;8;;;1;;;;;7;;;6;;;5;',
';5;;7;;;;;;5;;;;;3;;;;;3',
';;;;6;5;;;4;5;5;;;3;;;;3;;'])
peli4.main()
  # peli4.make_boxes()
  # peli4.make_numbers()
  # # peli4.print_table()
  # peli4.solve_step_1()
  # print('vaihe 1')
  # peli4.print_table()
  # peli4.solve_step_2()
  # print('vaihe 2')
  # peli4.print_table()
  # peli4.check_table()
  # alku = time.time()
  # peli4.solve_step_3(peli4.make_snapshot(),0,[()])
  # loppu = time.time()
  # print(f"kolmos vaihe kesti {loppu-alku}")
  # peli4.print_table()