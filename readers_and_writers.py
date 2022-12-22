from threading import Thread, Lock, Event
from time import sleep
from random import randint, choice

class Writer(Thread):

    def __init__(self, name: str, line: str, book_lock: Lock):
        """Method which initialize cllas Writer.
        
        Args:
            name - name of a writer.
            line - writer's line to write in the book.
            book_lock (Lock) - lock for no change book at the same time.
        """
        super().__init__()
        self.name = name
        self.line = line
        self.book_lock = book_lock

    def run(self):
        """Writers write in the book their lines and then go sleep."""
        global book, adding_letter
        LETTER_TIMEOUT = (1, 1)
        REST = (4, 5)

        while True:
            print(f'Writer {self.name} wants to write {self.line}')
            with self.book_lock:
                for letter in self.line:
                    book += letter 
                    print(f'{self.name} writes letter {letter}')
                    adding_letter.set()
                    adding_letter.clear()
                    sleep(randint(*LETTER_TIMEOUT))
                book = ''
            print(f'Writer {self.name} is sleeping')
            sleep(randint(*REST))

class Reader(Thread):

    def __init__(self, name: str):
        """Method which initialize cllas Reader.
        
        Args:
            name - name of a reader.
        """
        super().__init__()
        self.name = name

    def run(self):
        """Readers are reading a book in real time."""
        global adding_letter, book

        while True:
            adding_letter.wait()
            print(f'Reader {self.name} reads {book}')

if __name__ == '__main__':
    LINES = ['HELLO WORLD', 'ANYA IS COOL']
    BOOK_LOCK = Lock()
    adding_letter = Event()
    book = ''
    WRITERS = [Writer(number, choice(LINES), BOOK_LOCK) for number in range(3)]
    READERS = [Reader(number) for number in range(4)]

    for reader in READERS:
        reader.start()

    for writer in WRITERS:
        writer.start()

            

