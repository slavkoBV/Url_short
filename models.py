import string
from random import choices

from .config import NUMBER_OF_CHARACTERS

from .app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_url = db.Column(db.String(512))
    short_url = db.Column(db.String(NUMBER_OF_CHARACTERS), unique=True)
    counter = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.get_short_url()

    def get_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=NUMBER_OF_CHARACTERS))

        url = self.query.filter_by(short_url=short_url).first()

        if url:
            return self.get_short_url()
        return short_url
