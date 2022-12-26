"""Main for readers and writers."""

from threading import Lock
from readers_and_writers import Book, Reader, Writer

if __name__ == '__main__':
    NUM_OF_READERS = 5
    TEXTS = ["Text1", "Text2", "Text3", "Text4"]

    book = Book(lock=Lock())
    queue = Lock()
    for reader in range(NUM_OF_READERS):
        Reader(str(reader), book).start()
    for num, text in enumerate(TEXTS):
        Writer(str(num), text, queue, book).start()
