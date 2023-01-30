from random import randint
from string import ascii_lowercase
from threading import Condition, Lock, Thread
from time import sleep


class Writer(Thread):

    WRITE_TIME = 1
    SLEEP_TIME = (1, 2)
    CAN_WRITE = 5

    def __init__(self, name: str, book: Lock):
        super().__init__()
        self.name = name

    def write(self):
        global notifier, book
        book.acquire()
        print(f"Writer {self.name} started rewriting")
        with open("book.txt", "w+") as note:
            note.write(f"By: {self.name}\n")
        note.close()
        for _ in range(self.CAN_WRITE):
            with open("book.txt", "a") as note:
                with notifier:
                    note.write(ascii_lowercase[randint(0, len(ascii_lowercase) - 1)])
                    notifier.notify_all()
            sleep(self.WRITE_TIME)
        note.close()
        book.release()
        print(f"Writer {self.name} going to rest")

    def run(self):
        while True:
            print(f"Writer {self.name} is resting")
            sleep(randint(*Writer.SLEEP_TIME))
            print(f"Writer {self.name} wanna work")
            self.write()


class Reader(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        global notifier
        while True:
            with notifier:
                notifier.wait()
                with open("book.txt", "r") as note:
                    print(f"Reader {self.name} reads \n{' '.join(note.readlines())}")


if __name__ == "__main__":
    NUM_WRITERS = 2
    book = Lock()
    notifier = Condition(Lock())
    WRITERS = [Writer(str(num), book) for num in range(NUM_WRITERS)]
    READERS = [Reader(str(num)) for num in range(NUM_WRITERS)]
    for num in enumerate(WRITERS):
        WRITERS[num[0]].start()
        READERS[num[0]].start()
        sleep(1)
