from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.book import Book

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

tasks_blueprint = Blueprint("books", __name__)

@tasks_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("books/index.jinja", all_books = books)