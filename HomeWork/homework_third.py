"""Home work philosopher's."""
from multiprocessing import Process, Lock
from random import randint
from faker import Faker
from time import sleep
TABLE = 2


class Table(Process):
    """Representation of table."""

    LONG_VISITORS_TIME = [1, 5]

    def __init__(self, name: str):
        """Initialization method.

        Args:
            name(str): table name.
        """
        super().__init__(name=name)
        self.name = name
        self.seats = randint(2, 5)

    def run(self):
        """Main table function that start him."""
        print("{0} - Накрыт для посетителей, всего {1} мест".format(self.name, self.seats))
        sleep(1)
        chopsticks = [Lock() for _ in range(self.seats)]
        for number_of_stick in range(self.seats):
            philosopher_name = "{2} Филосов {0} #{1}".format(Faker().name(), number_of_stick, self.name)
            print("{0} зашёл в бар и сел за {1}".format(philosopher_name, self.name))
            chopstick_left = chopsticks[number_of_stick - 1]
            chopstick_right = chopsticks[number_of_stick]
            Philosopher(philosopher_name, chopstick_left, chopstick_right).start()
            sleep(randint(*self.LONG_VISITORS_TIME))


class Philosopher(Process):
    """Representation of philosopher."""

    EATING_TIME = (2, 5)
    THINKING_TIME = (3, 7)
    TIMEOUT = 0.01
    LEFT_RIGHT = [0, 1]
    RIGHT_LEFT = [1, 0]

    def __init__(self, name: str, chopstick_left: Lock, chopstick_right: Lock):
        """Initialization method.

        Args:
            name(str): philosopher's name.
            chopstick_left(Lock): his left chopstick.
            chopstick_right(Lock): his right chopstick.
        """
        super().__init__(name=name)
        self.name = name
        self.chopstick_left = chopstick_left
        self.chopstick_right = chopstick_right

    def out(self):
        """Function which show us what philosopher doing."""
        print("{0}\033[32m начинает есть.\033[0m".format(self.name))
        sleep(randint(*Philosopher.EATING_TIME))
        print("{0}\033[33m заканчивает есть и начинает думать\033[0m".format(self.name))

    def run(self) -> None:
        """Main philosopher's function that start him."""
        while True:
            chopsticks = self.chopstick_right, self.chopstick_left
            for first_choice, second_choice in (Philosopher.LEFT_RIGHT, Philosopher.RIGHT_LEFT):
                if chopsticks[first_choice].acquire(timeout=Philosopher.TIMEOUT):
                    if chopsticks[second_choice].acquire(timeout=Philosopher.TIMEOUT):
                        self.out()
                        self.chopstick_right.release()
                        self.chopstick_left.release()
                        sleep(randint(*Philosopher.THINKING_TIME))
                        print("{0}\033[31m заканчивает думать и хочет поесть.\033[0m".format(self.name))
                    else:
                        chopsticks[first_choice].release()


if __name__ == '__main__':
    print("\033[92mБургер Кинг открыт, столы накрываются\033[0m")
    for number_of_table in range(TABLE):
        waiter_time = randint(3, 10)
        print("Официант накроет стол за {0}сек.".format(waiter_time))
        sleep(waiter_time)
        Table("Стол ${0}".format(number_of_table)).start()
