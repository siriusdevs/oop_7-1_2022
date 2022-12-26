"""Main for barber."""

from random import randint

from oop5.barber import Client, Barbershop
from time import sleep

SIZE_QUEUE = 2
ENTER_TIME_INTERVAL = (1, 3)

PEOPLE = [
    'Michelin',
    'Alex',
    'Max',
    'Kiril1',
    'Kiril2',
    'Kiril3',
    'Kiril4',
    'Kiril5',
    'Kiril6',
    'Kiril7',
    'Kiril8',
    'Kiril9',
    'Kiril10',
]

if __name__ == '__main__':
    clients = [Client(human) for human in PEOPLE]
    library = Barbershop(SIZE_QUEUE)
    library.open()
    for client in clients:
        library.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
