"""Map building and using running programm."""
from os import system
from analyzing import Buildings


def printer(lis):
    """Printing rhe instruction.

    Args:
        lis(list): instruction list
    """
    for i in lis:
        print(i)


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
                rdata = [None] + list(itog) + [None]
        else:
            print(itog[0])
            input("Enter to continue")
    else:
        rdata = [None] + list(itog) + [None]
    return rdata


def start():
    """Function that runs the programm."""
    with open('instruction.txt', 'r') as i:
        lis = []
        for string in i.readlines():
            lis.append(string[:-1])
    rdata = [None, None, None, None, {}, None]
    while rdata[0] != ['Q']:
        system('clear')
        printer(lis)
        if rdata[1]:
            print(rdata[2])
            for string in rdata[1]:
                print(string)
        rdata[0] = input().split()
        if rdata[0]:
            itog = Buildings(rdata[0], (rdata[1], rdata[4], rdata[2]), rdata[3]).input_analys()
        if itog:
            rdata = itog_to_data(itog, rdata)


if __name__ == "__main__":
    start()
