"""
Lesson 2.4 - Interface Segregation Principle (ISP)

Step 1: Read the BadMediaItem hierarchy below. Notice every subclass has
        to implement ALL of get_page_count / get_runtime_minutes / play,
        even when it makes no sense for that type.
Step 2: Run it and observe what happens when calling code (naively,
        assuming any MediaItem supports anything) calls the wrong method
        on the wrong type.
Step 3: Refactor into small, focused interfaces (Readable, Playable) and
        have Book/DVD implement ONLY the ones that genuinely apply to them,
        using Python's multiple inheritance.
"""

from abc import ABC, abstractmethod


class BadMediaItem(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def get_page_count(self):
        ...

    @abstractmethod
    def get_runtime_minutes(self):
        ...

    @abstractmethod
    def play(self):
        ...


class BadBook(BadMediaItem):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages

    def get_page_count(self):
        return self.pages

    def get_runtime_minutes(self):
        raise NotImplementedError("Books don't have a runtime")

    def play(self):
        raise NotImplementedError("Books can't be played")


class BadDVD(BadMediaItem):
    def __init__(self, title, runtime_minutes):
        super().__init__(title)
        self.runtime_minutes = runtime_minutes

    def get_page_count(self):
        raise NotImplementedError("DVDs don't have pages")

    def get_runtime_minutes(self):
        return self.runtime_minutes

    def play(self):
        print(f"Playing {self.title}")

class Readable(ABC):
    @abstractmethod
    def get_page_count(self):
        ...


class Playable(ABC):
    @abstractmethod
    def get_runtime_minutes(self):
        ...

    @abstractmethod
    def play(self):
        ...

class MediaItem():
    def __init__(self, title):
        self.title = title
        
        
class DVD(MediaItem, Playable):
    def __init__(self, title, runtime_minutes):
        super().__init__(title)
        self.runtime_minutes = runtime_minutes

    def get_runtime_minutes(self):
        return self.runtime_minutes

    def play(self):
        print(f"Playing {self.title}")

class Book(MediaItem, Readable):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages

    def get_page_count(self):
        return self.pages

def print_page_count(item:Readable):
    print(f"Page count : {item.get_page_count()}")

def play_item(item: Playable):
    item.play()
# ============================================================
# TODO: Refactor.
#
# 1. Define two small interfaces: Readable (get_page_count) and
#    Playable (play, get_runtime_minutes).
# 2. Define a lean MediaItem base with just what's ALWAYS true for
#    every media item (e.g. title).
# 3. Book(MediaItem, Readable) -- implements only get_page_count.
#    DVD(MediaItem, Playable) -- implements only play/get_runtime_minutes.
#    Neither implements a method that doesn't apply to it. No
#    NotImplementedError stubs anywhere.
# 4. Write two small functions: print_page_count(item: Readable) and
#    play_item(item: Playable) -- each should only ever be called with
#    an object that actually supports that capability.
# ============================================================


if __name__ == "__main__":
    book = Book("book1", 100)
    dvd = DVD("movie1", 180)
    print_page_count(book)
    play_item(dvd)
    play_item(book)
    # TODO: create a Book and a DVD using your refactored classes
    # TODO: call print_page_count on the book, play_item on the dvd
    # TODO: (optional, to drive the point home) try calling play_item on
    #       the book -- it should fail at the type level / not even make
    #       sense to attempt, rather than raising NotImplementedError
    #       at runtime
    
    
