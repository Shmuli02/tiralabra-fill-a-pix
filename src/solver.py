from os import listdir, read
from os.path import isfile, join
from fillapix import FillaPix
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
            print(file_url)
            file = open(file_url,"r")
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
            print(game_x,game_y)
            game = FillaPix(game_x,game_y,game_data)
            game.main()
        except:
            print('Väärä syöte')
