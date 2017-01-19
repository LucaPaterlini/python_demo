# This program connects to local mongoengine_database, it inserts the authors and books data
# by accessing files (authors_data.in,authors_data.in) in the database

from mongoengine import connect
from datetime import datetime
from mongoengine_demo.library import *

db=connect("mongodblibrary")
AUTHORS_DATA = "authors_data.in"
BOOKS_DATA = "books_data.in"
def load_authors_data(file_name):
    # this functions opens the file named in file_name and inserts the payload
    # into the database
    fd = open(file_name, 'r')
    n = int(fd.readline())
    for i in xrange(n):
        tmp_name = fd.readline()[:-1]
        tmp_surname = fd.readline()[:-1]
        tmp_bio = fd.readline()[:-1]
        birh_date_vect = map(int, fd.readline().split())
        tmp_birth_date = datetime(*birh_date_vect) if birh_date_vect else None
        death_date_vect = map(int, fd.readline().split())
        tmp_death_date = datetime(*map(int, *death_date_vect)) if death_date_vect else None
        Author(name=tmp_name, surname=tmp_surname, short_bio=tmp_bio, birth_date=tmp_birth_date,
               death_date=tmp_death_date).save()
    fd.close()

def load_books_data(file_name):
    # this functions opens the file named in file_name and inserts the payload
    # into the database
    fd = open(file_name, 'r')
    n = int(fd.readline())
    for i in xrange(n):
        tmp_title = fd.readline()[:-1]
        tmp_author_name,tmp_author_surname=fd.readline()[:-1],fd.readline()[:-1]

        tmp_author = Author.objects.get(name=tmp_author_name)
        print tmp_author
        tmp_abstract = fd.readline()[:-1]
        tmp_year_of_publication = int(fd.readline()[:-1])
        Book(title=tmp_title, author=tmp_author,abstract=tmp_abstract,
             year_of_publication=tmp_year_of_publication).save()
    fd.close()

print "Authors count before the insertion", len(Author.objects)
# load_authors_data(AUTHORS_DATA)
print "Authors count after the insertion", len(Author.objects)
print "Books count before the insertion", len(Book.objects)
load_books_data(BOOKS_DATA)
print "Books count after the insertion", len(Book.objects)
