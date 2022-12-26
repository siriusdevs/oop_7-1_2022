"""Model philosophers."""

import datetime
from multiprocessing import Process, Lock, Event
from random import randint
from time import sleep


class Philosopher(Process):
    """Class philosopher."""

    EATING_TIME = (1, 3)
    FAMINE_TIME = (5, 6)
    THINKING_TIME = (1, 3)
    WAIT_TIME = 0.001
    CHECK_HUNGRY_TIME = 1

    def __init__(self, name: str, chopstick_left: Lock, chopstick_right: Lock):
        """Create a philosopher.

        Args:
            name: str - philosopher's name.
            chopstick_left: Lock - chopstick left.
            chopstick_right: Lock - chopstick right.
        """
        super().__init__(name=name)
        self.name = name
        self.chopstick_left = chopstick_left
        self.chopstick_right = chopstick_right
        self.patience = datetime.timedelta(seconds=randint(*Philosopher.FAMINE_TIME))
        self.hunger = Event()
        self.__last_eating = datetime.datetime.now()

    def eating(self):
        """Function which eating the philosopher."""
        self.hunger.clear()
        print("{0} начал есть".format(self.name))
        sleep(randint(*Philosopher.EATING_TIME))
        print("{0} поел и начал мыcлить".format(self.name))

    def check_hunger(self):
        """Сhecks how long the philosopher has not eaten the philosopher."""
        while True:
            if self.hunger.wait(1):
                time = datetime.datetime.now() - self.__last_eating
                if time > self.patience:
                    print("{0} голодает уже {1}".format(self.name, time))
            else:
                print("{0} перестал голодать".format(self.name))
                self.__last_eating = datetime.datetime.now()
            sleep(Philosopher.CHECK_HUNGRY_TIME)

    def run(self) -> None:
        """Run method of philosopher."""
        Process(target=self.check_hunger).start()
        while True:
            if self.chopstick_left.acquire(timeout=Philosopher.WAIT_TIME):
                if self.chopstick_right.acquire(timeout=Philosopher.WAIT_TIME):
                    self.eating()
                    self.chopstick_right.release()
                    self.chopstick_left.release()
                    self.hunger.set()
                    sleep(randint(*Philosopher.THINKING_TIME))
                    print("{0} перестал мыслить и хочет есть".format(self.name))
                else:
                    self.chopstick_left.release()
            # works without below code, but sometimes they starve a long
            #
            # elif self.chopstick_right.acquire(timeout=Philosopher.WAIT_TIME):
            #     if self.chopstick_left.acquire(timeout=Philosopher.WAIT_TIME):
            #         self.out()
            #     else:
            #         self.chopstick_right.release()
