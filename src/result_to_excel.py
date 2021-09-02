import xlwings as xw

class FillaPixExcel:
    def __init__(self,file_name,game_data):
        self.abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        # self.abc = [chr(i) for i in range(65,91)] + [(chr(j)+chr(i)) for j in range(65,91) for i in range(65,91)]
        self.file_name = file_name
        self.game_data = game_data
  
    def to_excel(self):
        wb = xw.Book('macro.xlsm')
        sheet = wb.sheets['uu']
        for i in range(0,len(self.game_data)):
            for j in range(0,len(self.game_data[0])):
                u = str(self.abc[i]+str(j+1))
                if self.game_data[j][i] == 1:
                    sheet.range(u).value = self.game_data[j][i]
        wb.save(self.file_name + '.xlsm')
