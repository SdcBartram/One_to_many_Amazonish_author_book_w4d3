from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author_repo.delete_all()
book_repo.delete_all()

author1 = Author("Steven King")
author_repo.save(author1)
author2 = Author("Jane Austen")
author_repo.save(author2)

# author_repo.select_all()

book1 = Book("IT", "horror", author1)
book_repo.save(book1)
book2 = Book("Emma", "horror", author2)
book_repo.save(book2)

# book_repo.delete(1)

# book2.genre = "Romance"
# book_repo.update(book2)

# author1.name = "Bob"
# author_repo.update(author1)

# authors = author_repo.select_all()
# for author in authors:
#     print(author.name)