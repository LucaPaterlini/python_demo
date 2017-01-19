from mongoengine import StringField, ReferenceField, Document, IntField
from author import Author


class Book(Document):
    title = StringField(required=True)
    author = ReferenceField(Author)
    abstract = StringField()
    year_of_publication = IntField()
