import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_nacimiento = Column(String(250), nullable=False)
    

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre_personaje = Column(String(250), nullable=False)
    especie_personaje = Column(String(250), nullable=False)
    
    
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(250), nullable=False)
    habitabilidad = Column(String(250), nullable=False)
    habitantes = Column(String(250), nullable=False)


class PersonajesFavoritos(Base):
    __tablename__ = 'personajes_favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey ("usuario.id"))
    personaje_id = Column(Integer, ForeignKey ("personajes.id"))
    relacion_personaje = relationship ("Personajes")
    relacion_usuario = relationship ("Usuario")


class PlanetasFavoritos(Base):
    __tablename__ = 'planetas_favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey ("usuario.id"))
    planeta_id = Column(Integer, ForeignKey ("planetas.id"))
    relacion_planeta = relationship ("Planetas")
    relacion_usuario = relationship ("Usuario")
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')