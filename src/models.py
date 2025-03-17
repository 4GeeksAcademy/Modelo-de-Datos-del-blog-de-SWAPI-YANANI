from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er


DB = SQLAlchemy()

# TABLA DEL USUARIO


class User(DB):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[int] = mapped_column(
        String(40), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(20), nullable=False)
    lastname: Mapped[str] = mapped_column(String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,

        }

    favorites = relationship('Favorite', backref='user', lazy=True)


# TABLA DE PERSONAGES----------------------------------------------------
class characters(DB):
    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(20), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(20), nullable=False)
    height: Mapped[str] = mapped_column(String(20), nullable=False)
    url: Mapped[str] = mapped_column(String(200), nullable=False)

    favorites = relationship('Favorite', backref='characters', lazy=True)

 # TABLA DE PLANETAS------------------------------------------------------


class Planets(DB):
    __tablename__ = 'planets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    climate: Mapped[str] = mapped_column(String(20), nullable=False)
    rotation_time: Mapped[str] = mapped_column(String(20), nullable=False)
    diameter: Mapped[str] = mapped_column(String(20), nullable=False)
    gravity: Mapped[str] = mapped_column(String(20), nullable=False)

    favorites = relationship('Favorite', backref='planets', lazy=True)


# TABLA DE VEHICULOS-----------------------------------------------------
class Vehicles(DB):
    __tablename__ = 'vehicles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    vehicle_tipe: Mapped[str] = mapped_column(String(20), nullable=False)
    length: Mapped[str] = mapped_column(String(20), nullable=False)
    value: Mapped[str] = mapped_column(String(20), nullable=False)
    fuel_capacity: Mapped[str] = mapped_column(String(20), nullable=False)
    url: Mapped[str] = mapped_column(String(200), nullable=False)

    favorites = relationship('Favorite', backref='vehicles', lazy=True)


# FAVORITOS-----------------------------------------------------
class Favorite(DB):
    __tablename__ = 'favorite'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(DB.ForeignKey('user.id'))
    characters_id: Mapped[int] = mapped_column(DB.ForeignKey('characters.id'))
    planet_id: Mapped[int] = mapped_column(DB.ForeignKey('planets.id'))
    vehicle_id: Mapped[int] = mapped_column(DB.ForeignKey('vehicles.id'))


render_er(DB, 'diagram.png')
