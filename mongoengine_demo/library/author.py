from mongoengine import Document, StringField, DateTimeField


class Author(Document):
    name = StringField(required=True)
    surname = StringField(required=True)
    short_bio = StringField()
    birth_date = DateTimeField()
    death_date = DateTimeField()

