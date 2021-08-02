import unittest
from solver import FillaPix

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
  
  def test_make_boxes(self):
    self.peli.make_boxes()
    self.assertEqual(len(self.peli.boxes),15)