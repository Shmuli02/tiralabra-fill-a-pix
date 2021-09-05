import xlwings as xw
import os

class FillaPixExcel:
    def __init__(self,file_name,game_data):
        self.abc = [chr(i) for i in range(65,91)] + [(chr(j)+chr(i)) for j in range(65,91) for i in range(65,91)]
        self.file_name = os.path.splitext(file_name)[0]
        self.game_data = game_data
  
    def to_excel(self):
        wb = xw.Book('macro.xlsm')
        sheet = wb.sheets['uu']
        for i in range(0,len(self.game_data)):
            for j in range(0,len(self.game_data[i])):
                u = str(self.abc[j]+str(i+1))
                if self.game_data[i][j] == 1:
                    sheet.range(u).value = self.game_data[i][j]
        wb.save(self.file_name +'-result'+ '.xlsm')
