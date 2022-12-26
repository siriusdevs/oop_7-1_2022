from multiprocessing import Event, Lock, Process, Queue
from random import randint
from time import sleep

from faker import Faker


class Client:
    def __init__(self, name: str) -> None:
        self.name = name

        
class Barber:
    
    TIMEOUT = 5
    WORK_TIME = (2, 5)
    
    def __init__(self) -> None:
        self._came_of_client = Event()
    
    def client_wait(self) -> bool:
        print('Waiting for clients Z-Z-Z')
        return self._came_of_client.wait(timeout=Barber.TIMEOUT)
    
    def call(self) -> None:
        self._came_of_client.set()
 
    def cut(self, client: Client) -> None:
        print(f'Cutting {client.name}')
        self._came_of_client.clear()
        sleep(randint(*Barber.WORK_TIME))
        print(f'Cutted {client.name}')
 
    
class Barbershop:
    def __init__(self, size: int) -> None:
        self._queue = Queue(maxsize=size)
        self._worker = Barber()
        self._process = Process(target=self.work)
        self.mutex = Lock()

    def open(self) -> None:
        print('Barbershop is opened.')
        self._process.start()

    def close(self) -> None:
        print('Barbershop is closed.')

    def work(self) -> None:
        while True:
            self.mutex.acquire()
            if self._queue.empty():
                self.mutex.release()
                work_result = self._worker.client_wait()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self._queue.get()
                self._worker.cut(client)

    def enter(self, client: Client) -> None:
        with self.mutex:
            print(f'{client.name} has entered the barbershop')
            if self._queue.full():
                print(f'{client.name} sees full queue and leaves')
            else:
                print(f'{client.name} wants to do a haircut')
                self._queue.put(client)
                self._worker.call()


QUEUE_SIZE = 3
ENTER_INTERVAL = (1, 3)
CLIENTS = 5

if __name__ == '__main__':
    names = [Faker().name() for _ in range(CLIENTS)]
    clients = [Client(name) for name in names]
    barbershop = Barbershop(QUEUE_SIZE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*ENTER_INTERVAL))
