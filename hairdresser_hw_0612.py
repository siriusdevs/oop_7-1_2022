from multiprocessing import Process, Queue, Event, Lock
from time import sleep
from random import randint


class Client:
    def __init__(self, name) -> None:
        self.name = name


class Hairdresser:
    TIMEOUT = 10
    WORK_INTERVAL = (2, 5)

    def __init__(self) -> None:
        self.__client_came = Event()

    def work(self):
        print('Hairdresser is ready to work')
        result = self.__client_came.wait(timeout=Hairdresser.TIMEOUT)
        return result

    def call(self):
        self.__client_came.set()

    def shave(self, client):
        sleep(randint(*Hairdresser.WORK_INTERVAL))
        print(f'Hairdresser is cutting {client.name}\'s hair')

    def greet(self, client: Client):
        print(f'Hairdresser greets {client.name}')
        self.__client_came.clear()
        self.shave(client)
        print(f'Client {client.name} is done')


class Salon:

    def __init__(self, q_size: int) -> None:
        self.__worker = Hairdresser()
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        print(f'Salon opens (queue size = {self.q_size})')
        self.__process.start()

    def close(self):
        print('Salon closes')

    def work(self):
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                work_result = self.__worker.work()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client):
        print(f'Client {client.name} has entered the salon')
        with self.mutex:
            if self.__queue.full():
                print(f'Client {client.name} sees full queue and leaves')
            else:
                print(f'Client {client.name} waiting at the reception')
                self.__queue.put(client)
                self.__worker.call()


SIZE_QUEUE = 3
ENTER_TIME_INTERVAL = (1, 3)

if __name__ == '__main__':

    salon = Salon(SIZE_QUEUE)
    clients = [Client(i) for i in range(10)]
    salon.open()
    for client in clients:
        salon.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
