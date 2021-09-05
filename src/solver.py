from os import listdir, read
from os.path import isfile, join
from fillapix import FillaPix
from fillapixprinter import FillaPixPainter
try:
    from result_to_excel import FillaPixExcel
except ModuleNotFoundError:
    pass


try:
    mypath = 'games'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
except FileNotFoundError:
    mypath = 'src/games'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
while True:
    print('')
    for i in range(0,len(onlyfiles)):
        print(f"{i} {onlyfiles[i]}")
    open_file_n = input('Mikä peli valitaan? ')

    if open_file_n == 'exit':
        break
    else:

        try:
            file_url = mypath + '/' + onlyfiles[int(open_file_n)]
            file = open(file_url, encoding='utf-8-sig')
            game_data = []
            for line in file:
                line = line.strip('\ufeff')
                line = line.strip('\n')
                game_data.append(line)
                summa = 0
            game_y = 1
            for box in game_data[0]:
                if box == ';':
                    game_y += 1
            game_x = len(game_data)
            game = FillaPix(game_x,game_y,game_data)
            result = game.main()
            printer_result_turtle = input('Tulostetaanko tulos (turtle) avulla? k/e: ')
            if printer_result_turtle == 'k':
                try:
                    printer = FillaPixPainter(game_x,result)
                    printer.draw()
                except:
                    print('Ongelma')
            printer_result_excel = input('Tulostetaanko tulos (excel) avulla? k/e: ')
            if printer_result_excel == 'k':
                try:
                    to_excel = FillaPixExcel(onlyfiles[int(open_file_n)],result)
                    to_excel.to_excel()
                except:
                    print('Ongelma')
        except:
            print('Väärä syöte')
        
