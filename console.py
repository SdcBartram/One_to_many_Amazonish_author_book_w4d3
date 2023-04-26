from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author_repo.delete_all()
book_repo.delete_all()

author1 = Author("Stephen King")
author_repo.save(author1)
author2 = Author("Miguel de Cervantes")
author_repo.save(author2)

book1 = Book("IT", "horror", author1)
book_repo.save(book1)

book_repo.delete(4)

authors = author_repo.select_all()
for author in authors:
    print(author.name)