import buildWorker

while True:

    click = input(' Choose town for work - 1 \n \
see towns - click 2 \n \
create new town - click 3 \n \
exit - q \n')
    match click:

        case '1':
            print('{0:-^100}'.format('towns'))
            towns = buildWorker.Town.maps()
            for town in towns:
                print(*town)

            town = input('Please, choose a town: ')
            while True:
                choice = input(('Do you want to see map (sm), add a building (ab) or destroy a building (db)?\n \
                    Exit( q )'))
                match choice:
                    case 'sm':
                        for elem in buildWorker.Town.see_map('{0}.json'.format(town)):
                            for place in elem:
                                print(str(place).ljust(6), end=' ')
                            print()
                    case 'ab':
                        name = input('Enter building name: ')
                        height = float(input('Enter building hight: '))
                        width = float(input('Enter building width: '))
                        floors = int(input('Enter building floors: '))
                        coord_x = int(input('Enter building coordinate x: '))
                        coord_y = int(input('Enter building coordinate y: '))
                        building = buildWorker.Building(name, height, width, floors, coord_x, coord_y)
                        buildWorker.Town.add_building('{0}.json'.format(town), building)

                    case 'db':
                        name = input('Enter building\'s name for destroying: ')
                        buildWorker.Town.destroy_building('{0}.json'.format(town), name)

                    case 'q':
                        break

                    case _:
                        print('Unknown command')
        case '2':
            for town in buildWorker.Town.maps():
                print(*town, end=' ')
            print()
            print('-' * 50)

        case '3':
            length = int(input('Enter lenght of the matrix: '))
            width = int(input('Enter width of the matrix: '))
            map = buildWorker.Map(length, width)
            name = input('Enter new town\'s name: ')
            buildWorker.Town.create_town(map, name)

        case 'q':
            break

        case _:
            print('Unknown command')
