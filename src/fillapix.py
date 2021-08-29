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
    self.result = []

  def make_boxes(self): #Luodaan jokaiselle ruudulle Box luokka
    lista = []
    for i in range(self.xsize):
      lista2 = []
      for j in range(self.ysize):
        lista2.append(Box(i,j))
      lista.append(lista2)
    self.boxes = lista

  def make_numbers(self): # Luodaan jokaiselle numerolla Number luokka
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
                boxes.append(self.boxes[0][0])
                boxes.append(self.boxes[1][0])
                boxes.append(self.boxes[0][1])
                boxes.append(self.boxes[1][1])
              elif y == self.ysize-1: # oik yla kulma
                boxes.append(self.boxes[0][self.ysize-1])
                boxes.append(self.boxes[1][self.ysize-1])
                boxes.append(self.boxes[0][self.ysize-2])
                boxes.append(self.boxes[1][self.ysize-2])
              else: # yla reuna
                for i in range(y-1,y+2):
                  boxes.append(self.boxes[x][i])
                  boxes.append(self.boxes[x+1][i])
            elif x == self.xsize-1: # ala sivu
              if y == 0: # van ala kulma
                boxes.append(self.boxes[self.xsize-1][0])
                boxes.append(self.boxes[self.xsize-2][0])
                boxes.append(self.boxes[self.xsize-1][1])
                boxes.append(self.boxes[self.xsize-2][1])
              elif y == self.ysize-1: # oik ala kulma
                boxes.append(self.boxes[self.xsize-1][self.ysize-1])
                boxes.append(self.boxes[self.xsize-1][self.ysize-2])
                boxes.append(self.boxes[self.xsize-2][self.ysize-1])
                boxes.append(self.boxes[self.xsize-2][self.ysize-2])
              else: # ala reuna
                for i in range(y-1,y+2):
                  boxes.append(self.boxes[x-1][i])
                  boxes.append(self.boxes[x][i])
            elif y == 0: # vas reuna
              for i in range(x-1,x+2):
                boxes.append(self.boxes[i][y])
                boxes.append(self.boxes[i][y+1])
            elif y == self.ysize-1: # oik reuna
              for i in range(x-1,x+2):
                boxes.append(self.boxes[i][y-1])
                boxes.append(self.boxes[i][y])
          else: # keskella
            for e in range((x-1),x+2):
              for r in range((y-1),y+2):
                boxes.append(self.boxes[e][r])
          new_number = Number(x,y,a,boxes) # uusi numero
          all_numbers[int(a)].append(new_number) # uusi numero numerot listaan
          self.boxes[x][y].set_number(new_number) # merkataan numero oikeaan Box objektiin
          for box in boxes:
            box.add_number_around(new_number)
    
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
    self.numbers_todo = self.numbers_todo_main

    togo = True
    round = 1
    while togo is True:

      numbers_todo_round2 = self.numbers_todo.copy()
      togo = False
      remove_todo2 = []
      # print(f"kierros {round} numeroita {len(self.numbers_todo)}")
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
        if sum_black == num.n: # mustia oikea maara
          for box in boxes:
            if box.value is None:
              box.value = 0
              togo = True
          remove_todo2.append(i)
          

        elif sum_white == (len(boxes)-int(num.n)+sum_black): # valkoisia oikea maara
          for box in boxes:
            if box.value is None:
              box.value = 1
              togo = True
          remove_todo2.append(i)
          

        elif num.n == (len(boxes)-sum_white):
          for box in boxes:
            if box.value is None:
              box.value = 1
              togo = True
          remove_todo2.append(i)
          
      for i in range(0,len(remove_todo2)):
        numbers_todo_round2.pop(remove_todo2[i]-i)
      self.numbers_todo = numbers_todo_round2.copy()
      round += 1

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
    if self.result != []:
      return
    self.fill_table(snap)
    # self.numbers_todo = todo
    self.solve_step_2()
    if self.check_table() is False:
      # print(f"ei onnistunut. numero {muokatut[-1]} aiheutti ongelman")
      muokatut = muokatut[:-1]
      return False
    if self.table_ready() is True:
      print('vaihe 3')
      print('VALMIS')
      self.print_table()
      
      self.result = self.make_snapshot()
      return self.table
    else:
      if len(self.numbers_todo) != 0:
        num_to_try = self.numbers_todo[0]
        uudet_snap = []
        uudet_muokatut = []
        none_laatikot = []
        mustat = 0
        for i in range(0,len(num_to_try.number_boxes)):
          if num_to_try.number_boxes[i].value == None:
            none_laatikot.append(i)
          elif num_to_try.number_boxes[i].value == 1:
            mustat += 1
        possible_fills = list(combinations(none_laatikot,(num_to_try.n-mustat))) #millä tavoilla numero voidaan täyttää
        for fill in possible_fills:
          for fill_box in fill:
            num_to_try.number_boxes[fill_box].value = 1
          kunnossa = True
          for boox in fill:
            if self.check_box(num_to_try.number_boxes[boox]) is not True:
              kunnossa = False
              break
          if kunnossa is True:
            new_snap = self.make_snapshot()
            uudet_snap.append(new_snap)
            uudet_muokatut.append((num_to_try.x,num_to_try.y))

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
    alku = time.time()
    self.make_boxes()
    self.make_numbers()
    # peli4.print_table()
    self.solve_step_1()
    print('vaihe 1')
    self.print_table()
    self.solve_step_2()
    print('vaihe 2')
    self.print_table()
    if self.table_ready() is True:
      loppu = time.time()
      print(f"Yhteensä ratkaisu kesti {loppu-alku}")
    else:
      step3_alku = time.time()
      self.solve_step_3(self.make_snapshot(),0,[()])
      step3_loppu = time.time()
      print(f"kolmos vaihe kesti {step3_loppu-step3_alku}")
      loppu = time.time()
      print(f"Yhteensä ratkaisu kesti {loppu-alku}")
    
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