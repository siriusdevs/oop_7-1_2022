import buildWorker

while True:

    click = input(' Choose town for work - click 1 \n \
see towns - click 2 \n \
create new town - click 3 \n \
exit - q \n')
    match click:

        case '1':
            print('{0:-^100}'.format('towns'))
            towns = buildWorker.Town.maps()
            for town, num in zip(towns, range(len(towns))):
                print(*town, '-', num)

            town = int(input('Please, choose a town: '))
            town = buildWorker.Town.maps()[town][0]
            while True:
                choice = input(('Do you want to see map (1) or inform about building(2), add a building (3) or destroy a building (4)?\n\
Go back(q)\n'))
                match choice:
                    case '2':
                        try:
                            x_coord = int(input('Enter building\' x coordinate on the map: '))
                            y_coord = int(input('Enter building\' y coordinate on the map: '))
                        except:
                            print('Enter correct data!')
                            continue
                        information = buildWorker.Town.see_buildings('{0}.json'.format(town), str(y_coord) + str(x_coord))
                        if isinstance(information, dict):
                            for hi in information:
                                print('{} - {}'.format(hi, information[hi]))
                        else:
                            print(information)
                    case '1':
                        for elem in buildWorker.Town.see_map('{0}.json'.format(town)):
                            for place in elem:
                                print(str(place).ljust(6), end=' ')
                            print()
                    case '3':
                        name = input('Enter building name: ')
                        try:
                            height = float(input('Enter building hight: '))
                            width = float(input('Enter building width: '))
                            floors = int(input('Enter building floors: '))
                            coord_x = int(input('Enter building coordinate x: '))
                            coord_y = int(input('Enter building coordinate y: '))
                        except Exception:
                            print('Enter correct data!')
                            continue
                        building = buildWorker.Building(name, height, width, floors, coord_x, coord_y)
                        buildWorker.Town.add_building('{0}.json'.format(town), building)

                    case '4':
                        try:
                            x_coord = int(input('Enter building\' x coordinate on the map: '))
                            y_coord = int(input('Enter building\' y coordinate on the map: '))
                        except:
                            print('Enter correct data!')
                        try:
                            buildWorker.Town.destroy_building('{0}.json'.format(town), str(y_coord) + str(x_coord))
                        except Exception:
                            print('No such a building')
                            continue

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
            try:
                length = int(input('Enter lenght of the matrix: '))
                width = int(input('Enter width of the matrix: '))
            except Exception:
                print('Enter correct data')
                continue
            map = buildWorker.Map(length, width)
            name = input('Enter new town\'s name: ')
            buildWorker.Town.create_town(map, name)

        case 'q':
            break

        case _:
            print('Unknown command')
