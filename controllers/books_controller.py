from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

books_blueprint = Blueprint("books", __name__)

# to create a new entry
# GET '/books/new'


@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repo.select_all()
    return render_template("books/new.jinja", all_authors=authors)


@books_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    print(books)
    return render_template("books/index.jinja", all_books=books)

# create - POST '/books


@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_name = request.form['author_name']
    existing_author = request.form.get('existing_author')
    if existing_author:
        author_id = request.form['author_id']
        author = author_repo.select(author_id)
    else:
        author = author_repo.save(Author(author_name))

    book = Book(title, genre, author)
    book_repo.save(book)
    return redirect('/books')

# show - GET '/books/<id>'


@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repo.select(id)
    return render_template('books/show.jinja', book=book)

# edit - GET '/books/<id>/edit'


@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template('books/edit.jinja', book=book, all_authors=authors)

# update - POST '/books/<id>'


@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    book = book_repo.select(id)
    book.title = request.form['title']
    book.genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book.author = author
    book_repo.update(book)
    return redirect('/books')

# delete - POST '/books/<id>'


@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')
