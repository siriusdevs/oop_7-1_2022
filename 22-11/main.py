"""Map building and using running programm."""
from os import system
from analyzing import Buildings


def printer(lis, rdata):
    """
    Printing all the data.

    Args:
        lis(list): instruction list
        rdata(list): data about map
    """
    system('clear')
    for i in lis:
        print(i)
    if rdata[1]:
        print(rdata[2])
        for string in rdata[1]:
            print(string)


def itog_to_data(itog, rdata):
    """
    Function tht transfers itog into rundata.

    Args:
        itog(tuple): result of program
        rdata(list): running function's data
    """
    if isinstance(itog[0], str):
        if itog[1]:
            rdata[5] = input(itog[0])
            itog = Buildings(rdata[0], (rdata[1], rdata[4], rdata[2]), rdata[3], rdata[5]).input_analys()
            if itog:
                if isinstance(itog[0], str):
                    print(itog[0])
                    input("Enter to continue")
                else:
                    rdata = [None] + list(itog) + [None]
        else:
            print(itog[0])
            input("Enter to continue")
    else:
        rdata = [None] + list(itog) + [None]
    return rdata


def inpmaker(inp):
    """
    Constructs input in one list.

    Args:
        inp(list): command type
    """
    if inp == ['G']:
        inp = ['G', input("map's name: "), input("width by x: "), input("width by y: ")]
    if inp == ['O']:
        inp = ["O", (input("map's name: "))]
    if inp == ['D']:
        inp = ['D', (input("map's name: "))]
    if inp == ['E']:
        ifdel = input("add or delete building?[A/D]")
        if ifdel == "A":
            inp = [
                'E',
                input("x coordinate: "),
                input("y coordinate: "),
                input("widh by x: "),
                input("width by y: "),
                input("height: "),
                input("building's name: ")
            ]
        elif ifdel == "D":
            inp = [
                'E',
                input("x coordinate: "),
                input("y coordinate: "),
                input("widh by x: "),
                input("width by y: "),
                '0',
                ''
            ]
    if inp == ['S']:
        inp = ['S']
    if inp == ['I']:
        inp = ['I', input("x coordinate: "), input("y coordinate: ")]
    return inp


def start(lis, rdata):
    """
    Function that runs the programm.

    Args:
        lis(list): programm instruction
        rdata(list): programm data
    """
    while rdata[0] != ['Q']:
        printer(lis, rdata)
        print('')
        inp = inpmaker([input()])
        if inp:
            rdata[0] = inp
            itog = Buildings(rdata[0], (rdata[1], rdata[4], rdata[2]), rdata[3]).input_analys()
        if itog:
            rdata = itog_to_data(itog, rdata)


if __name__ == "__main__":
    with open('instruction.txt', 'r') as i:
        lis = []
        for string in i.readlines():
            lis.append(string[:-1])
    rdata = [None, None, None, None, {}, None]
    start(lis, rdata)
