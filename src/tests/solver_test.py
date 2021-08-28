import unittest
from fillapix import FillaPix

class TestFillapix(unittest.TestCase):
  def setUp(self):
    self.peli = FillaPix(15,15,
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

    self.peli2 = FillaPix(20,20,['4;;;6;;;;6;;;4;;4;;;1;;;3;',
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
  def test_make_boxes(self):
    self.peli.make_boxes()
    self.assertEqual(len(self.peli.boxes),15)

  def test_make_numbers(self):
    self.peli.make_boxes()
    self.peli.make_numbers()
    numbers = []
    for i in range(0,10):
      numbers.append(len(self.peli.numbers[i]))
    self.assertEqual(numbers,[8,7,11,16,24,26,8,2,0,0])

  def test_solve_step_1(self):
    self.peli.make_boxes()
    self.peli.make_numbers()
    self.peli.solve_step_1()
    result = []
    for i in self.peli.boxes:
      row = []
      for j in i:
        row.append(j.value)
      result.append(row)
    self.assertEqual(result,[
      [0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None],
      [0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, 0, 0, 0, None, None, None, None],
      [None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None],
      [None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None],
      [None, None, None, None, None, 0, 0, 0, 0, None, None, None, None, None, None],
      [None, None, None, None, None, 0, 0, 0, 0, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0],
      [None, None, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0],
      [None, None, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0],
      [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, 0, 0, 0, None, None, None, None, None],
      [None, None, None, None, None, None, None, 0, 0, 0, None, None, None, None, None]])

  def test_solve_step_2(self):
    self.peli.make_boxes()
    self.peli.make_numbers()
    self.peli.solve_step_1()
    self.peli.solve_step_2()
    result = []
    for i in self.peli.boxes:
      row = []
      for j in i:
        row.append(j.value)
      result.append(row)
    self.assertEqual(result,[
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
  
  def test_solve_step_3(self):
    self.peli2.main()
    result = self.peli2.result
    self.assertEqual(result,[
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
      