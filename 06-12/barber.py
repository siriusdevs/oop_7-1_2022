"""File with barbershop OLDBOY."""
from multiprocessing import Process, Queue, Event, Lock
from time import sleep
from random import randint

TIMEOUT = 5
WORK_INTERVAL = (4, 5)
SIZE_QUEUE = 1
ENTER_TIME_INTERVAL = (1, 2)


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
        self.guest_visited = Event()

    def meet(self, guest: Guest):
        """Meet the guest from the queue.

        Args:
            guest(Guest): the name of the quest
        """
        print('Барбер пригласил {0}'.format(guest.name))
        self.guest_visited.clear()
        self.trim(guest)
        print('{0} подстрижен и доволен'.format(guest.name))

    def call(self):
        """Call the barber if the quest comes."""
        self.guest_visited.set()

    def sleep(self):
        """Make the barber sleep until the guest comes.

        Returns:
            bool: if the guest comes or the timeout works
        """
        print('Барбер жёстко спит')
        return self.guest_visited.wait(timeout=TIMEOUT)

    def trim(self, guest: Guest):
        """Spend time on trimming hair to the guest.

        Args:
            guest(Guest): the name of the guest
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
        self.worker = Barber()
        self.q_size = q_size
        self.queue = Queue(maxsize=q_size)
        self.process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """The barbershop opens."""
        print('OLDBOY открылся очередь {0}'.format(self.q_size))
        self.process.start()

    def close(self):
        """The barbershop closes."""
        print('OLDBOY закрылся')

    def work(self):
        """Work when the quest comes."""
        while True:
            self.mutex.acquire()
            if self.queue.empty():
                self.mutex.release()
                work_result = self.worker.sleep()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                guest = self.queue.get()
                self.worker.meet(guest)

    def enter(self, guest: Guest):
        """Put the guest into the queue.

        Args:
            guest(Guest): the name of the guest.
        """
        with self.mutex:
            print('{0} вошел в OLDBOY'.format(guest.name))
            if self.queue.full():
                print('{0} увидел что народу слишком много и решил ходить обросшим'.format(guest.name))
            else:
                print('{0} увидел, что очередь небольшая и стал ждать'.format(guest.name))
                self.queue.put(guest)
                self.worker.call()


GUEST_NAMES = [
    'Leonardo',
    'Tom',
    'Gustav',
    'Alex',
    'Tomas',
]

if __name__ == '__main__':

    oldBoy1 = OldBoy(SIZE_QUEUE)
    guests1 = [Guest(str(name)) for name in GUEST_NAMES]
    oldBoy1.open()
    for guest in guests1:
        oldBoy1.enter(guest)
        sleep(randint(*ENTER_TIME_INTERVAL))
