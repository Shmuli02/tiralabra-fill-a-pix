from os import listdir, read
from os.path import isfile, join
from fillapix import FillaPix
mypath = 'games'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
while True:
  print('')
  for i in range(0,len(onlyfiles)):
    print(f"{i} {onlyfiles[i]}")
  open_file_n = input('Mikä peli valitaan? ')

  if open_file_n == 'exit':
    break
  else:
    game_x = int(input('Taulun korkeus (x) '))
    game_y = int(input('taulun leveys (y) '))
    file_url = mypath + '/' + onlyfiles[int(open_file_n)]
    print(file_url)
    file = open(file_url,"r")
    game_data = []
    for line in file:
      line = line.strip('\ufeff')
      line = line.strip('\n')
      game_data.append(line)
    # print(game_data)
    game = FillaPix(game_x,game_y,game_data)
    game.main()
