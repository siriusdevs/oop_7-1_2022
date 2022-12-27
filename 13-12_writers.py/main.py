"""Конфликтные исатели по очереди пишут одну и ту же книгу для своих писателей."""
from time import sleep
from random import randint, choices
from threading import Thread, Condition, Lock
from string import ascii_letters


class Writer(Thread):
    """Класс писателя, пишущего книгу."""

    def __init__(self, name) -> None:
        """
        Инициализация писателя.

        Args:
            name(int): номер писателя
        """
        super().__init__()
        self.name = name

    def run(self):
        """Писатель пишет."""
        global book
        while True:
            booklock.acquire()
            book = []
            print("Writer {0} started writing the book".format(self.name))
            for _ in range(randint(1, 10)):
                letter = choices(ascii_letters)[0]
                print("Writer {0} added {1} into the book".format(self.name, letter))
                book.append(letter)
                with cond:
                    cond.notify_all()
                sleep(TIMEOUT)
            booklock.release()
            sleep(randint(5, 10))


class Reader(Thread):
    """Класс читателя, пишущего книгу."""

    def __init__(self, name):
        """
        Инициализация читателя.

        Args:
            name(int): номер читателя
        """
        super().__init__()
        self.name = name

    def run(self):
        """Читатель читает."""
        while True:
            with cond:
                cond.wait()
            print("Reader {0} read {1} in the book".format(self.name, book[-1]))


if __name__ == '__main__':
    TIMEOUT = 1
    booklock = Lock()
    book = []
    cond = Condition()
    for i in range(3):
        Reader(i).start()
    for i in range(3):
        Writer(i).start()
