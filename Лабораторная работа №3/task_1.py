class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author
    @property
    def name(self):
        return self.__name
    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self,pages):
        if isinstance(pages,int) and pages>0:
            self.__pages=pages

    def __str__(self):
        super().__str__()


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super.__init__(name,author)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self,duration):
        if isinstance(duration,float) and duration>0:
            self.__duration=duration

    def __str__(self):
        super().__str__()
