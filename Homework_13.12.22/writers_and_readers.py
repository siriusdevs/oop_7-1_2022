"""This file for Reader and Writer classes."""
from threading import Thread, Condition, Lock
from time import sleep
from random import choice


class Reader(Thread):
    """This class create Reader."""

    def __init__(self, name: str) -> None:
        """
        This function create reader.
        Args:
            name: str - name of reader and thread.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Function of work thread reader."""
        global cond
        while True:
            with cond:
                cond.wait()     # Ожидание действия
                print("Читатель {0}, читает {1}".format(self.name, text))


class Writer(Thread):
    """This class create Writer."""

    time_for_write = 2
    time_for_sleep = 1
    text = ["Привет", "Пока", "Здравствуйте"]

    def __init__(self, name: str) -> None:
        """
        Function create writer.
        Args:
            name: str - name of writer and thread.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Function of work thread writer."""
        global text
        while True:
            with lock:
                writing_text = choice(self.text)
                while writing_text != "":
                    ch = writing_text[0]
                    text += ch
                    writing_text = writing_text[1:]
                    print("Писатель {0} написал букву {1}".format(self.name, ch))
                    cond.acquire()      # Получили доступ
                    cond.notify_all()   # Сообщает всем читателям что можно читать
                    cond.release()      # Закрыли себе доступ
                    sleep(self.time_for_write)
                print("Писатель {0} написал строку {1}".format(self.name, writing_text))
                print("Писатель {0} пошёл отдыхать")
                writing_text = ""
                sleep(self.time_for_sleep)


if __name__ == "__main__":
    cond = Condition(lock=Lock())
    lock = Lock()
    text = ""
    for reader in range(5):
        Reader(f"reader_{reader}").start()
    for writer in range(2):
        Writer(f"writer_{writer}").start()
    sleep(0.1)
