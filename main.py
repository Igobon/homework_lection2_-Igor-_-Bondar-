from pydantic import BaseModel

class Bookmodel(BaseModel):
    title:str
    year: int
    autor:str


class Book:
    def __init__(self,title,year,autor):
        self.title=title
        self.year=year
        self.autor=autor

    def __str__(self):
        return Book(f'{self.title} by {self.autor} from {self.years}')

class Library:
    def __init__(self):
        self.books=[]

    def __iter__(self):
        return iter(self.books)
    def __generator_books(self,autor: str):
        for book in self.books:
            if book.autor == autor:
                yield book

    def log_add_book(func):
        def wrapper(*args,**kwargs):
            result=func(*args,**kwargs)
            print(f'function{__name__} result{result}')
        return wrapper
    @log_add_book
    def add_book(library,book):
        return #dobawit funkciju zadekorirowanuju


    def check_del_book(func):
        def wrapper(slef,book):
            if book in self.books:
                print('this book exist in library')
            return func(self,book)
            return wrapper()
    @check_del_book
    def dell_book(library,book):
        pass#podywytys'


    def save_file(self,file_name:str):
        with open(file_name,'w') as file:
            for book in self.books:
                file.write(f'{book.title} {book.autor} {book.year}')

    def load_book(self,file_name:str):
        with open(file_name, 'r') as file:
            for new_book in file.readlines():
                title, autor, year = new_book.strip().split(",")
                self.books.append(Bookmodel(title=title, autor=autor, year=int(year)))
class Magazin(Bookmodel):
    pass


