from pydantic import BaseModel, validator
from pydantic.error_wrappers import ValidationError

class BookSchema():
    title: str
    isbn: str

class UserSchema(BookSchema):
    # use email type field depends on some library
    email: str
    #books: BookSchema


def main():
    livro1 = {'title': "PIKA", 'isbn': '2129384'}
    livro2 = {'title': "PIKA", 'isbn': 1223333}
    print(BookSchema(livro1))

main()