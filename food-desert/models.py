from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Coordinates(DB.Model):
    lat = DB.Column(DB.BigInteger, nullable=False)
    lon = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<Latitude {}>'.format(self.lat)
        return '<Longitude {}>'.format(self.lon)
