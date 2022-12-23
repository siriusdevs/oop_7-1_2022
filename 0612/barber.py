"""File with barbershop OLDBOY."""
from multiprocessing import Process, Queue, Event, Lock
from time import sleep
from random import randint

TIMEOUT = 5
WORK_INTERVAL = (1, 3)
SIZE_QUEUE = 2
ENTER_TIME_INTERVAL = (3, 6)


class Guest:
    """This is class guest in OLDBOY"""

    def __init__(self, name: str) -> None:
        """Initalization method.

        Args:
            name (str): quest's name.
        """
        self.name = name


class Barber:
    """This is class of barber in OLDBOY ."""

    def __init__(self) -> None:
        """Initialize the barber."""
        self.__guest_visited = Event()

    def meet(self, guest: Guest):
        """Meet the guest from the queue.

        Args:
            guest(Guest): the name of the quest
        """
        print('Барбер пригласил {0}'.format(guest.name))
        self.__guest_visited.clear()
        self.trim(guest)
        print('{0} подстрижен и доволен'.format(guest.name))

    def call(self):
        """Call the barber if the quest comes."""
        self.__guest_visited.set()

    def sleep(self):
        """Make the barber sleep until the quest comes.

        Returns:
            bool: if the quest comes or the timeout works
        """
        print('Барбер жёстко спит')
        res = self.__guest_visited.wait(timeout=TIMEOUT)
        return res

    def trim(self, guest: Guest):
        """Spend time on trimming hair to the quest.

        Args:
            guest(Guest): the name of the quest
        """
        sleep(randint(*WORK_INTERVAL))
        print('Барбер работает над {0}'.format(guest.name))


class OldBoy:
    """This is class of a barbershop."""

    def __init__(self, q_size: int) -> None:
        """Initialize the barbershop.

        Args:
            q_size(int): size of the queue in the barbershop
        """
        self.__worker = Barber()
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """The barbershop opens."""
        print('OLDBOY открылся очередь {0}'.format(self.q_size))
        self.__process.start()

    def close(self):
        """The barbershop closes."""
        print('OLDBOY закрылся')

    def work(self):
        """Work when the quest comes."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result = self.__worker.sleep()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                guest = self.__queue.get()
                self.__worker.meet(guest)

    def enter(self, guest: Guest):
        """Put the guest into the queue.

        Args:
            guest(Guest): the name of the guest.
        """
        with self.mutex:
            print('{0} вошел в OLDBOY'.format(guest.name))
            if self.__queue.full():
                print('{0} увидел что народу слишком много и ушёл'.format(guest.name))
            else:
                print('{0} увидел, что очередь небольшая и стал ждать'.format(guest.name))
                self.__queue.put(guest)
                self.__worker.call()


GUEST_NAMES = [
    'Leonardo',
    'Tom',
    'Gustav',
    'Alex',
    'Tomas',
]

if __name__ == '__main__':

    OldBoy = OldBoy(SIZE_QUEUE)
    guests = [Guest(str(name)) for name in GUEST_NAMES]
    OldBoy.open()
    for guest in guests:
        OldBoy.enter(guest)
        sleep(randint(*ENTER_TIME_INTERVAL))
