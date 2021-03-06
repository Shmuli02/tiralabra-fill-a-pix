import time
from itertools import combinations

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
                        for x_koko in range((x-1),x+2):
                            for y_koko in range((y-1),y+2):
                                boxes.append(self.boxes[x_koko][y_koko])
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
                if self.boxes[i][j].value is None:
                    # print('ratkaisu kesken')
                    return False
        if len(self.numbers_todo) == 0:
            if self.table_ready2() is True:
                return True
        return False

    def table_ready2(self):
        self.numbers_todo = self.numbers_todo_main
        self.solve_step_2()
        if len(self.numbers_todo) == 0:
            print('Ratkaisu oikein')
            return True
        else:
            return False

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
        if len(self.numbers_todo) != 0:
            num_to_try = self.numbers_todo[0]
            uudet_snap = []
            uudet_muokatut = []
            none_laatikot = []
            mustat = 0
            for i in range(0,len(num_to_try.number_boxes)): #mill?? tavoilla numero voidaan t??ytt????
                if num_to_try.number_boxes[i].value is None:
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
                        kunnossa = False
                        break
                if kunnossa is True:
                    new_snap = self.make_snapshot()
                    uudet_snap.append(new_snap)
                    uudet_muokatut.append((num_to_try.x,num_to_try.y))

                for fill_box in fill:
                    num_to_try.number_boxes[fill_box].value = None
            if len(uudet_snap) > 0:
                # print(f"Muokatut numerot {muokatut} kierros {k} numeroita viel?? {len(self.numbers_todo)}")
                for uusi in range(len(uudet_snap)):
                    muokatut_laatikot = muokatut.copy()
                    uusi_lista = list(uudet_muokatut[uusi])
                    uusi_lista.append(uusi+1)
                    uusi_lista.append(len(uudet_snap))
                    # todo2 = copy.copy(self.numbers_todo)
                    muokatut_laatikot.append(tuple(uusi_lista))

                    self.solve_step_3(uudet_snap[uusi],k+1,muokatut_laatikot)
            else:
                # print('ei uusia muokattavia')
                return False
        else:
            print('!!! todo lista tyhj?? !!!')
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
        self.numbers_todo_main = self.numbers_todo
        print('vaihe 2')
        self.print_table()
        if self.table_ready() is True:
            loppu = time.time()
            print(f"Yhteens?? ratkaisu kesti {loppu-alku}")
            self.result = self.make_snapshot()
        else:
            step3_alku = time.time()
            self.solve_step_3(self.make_snapshot(),0,[()])
            step3_loppu = time.time()
            print(f"kolmos vaihe kesti {step3_loppu-step3_alku}")
            loppu = time.time()
            print(f"Yhteens?? ratkaisu kesti {loppu-alku}")
        return self.result

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
