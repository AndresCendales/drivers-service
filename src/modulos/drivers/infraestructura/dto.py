"""DTOs para la capa de infrastructura del dominio de drivers

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de drivers

"""

from config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Ruta(db.Model):
    __tablename__ = "rutas"
    id = db.Column(db.String(40), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False, primary_key=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, primary_key=True)
    zona = db.Column(db.String(10), nullable=False)
    hora_salida = db.Column(db.DateTime, nullable=False)
    tiempo_estimado = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.String(40), db.ForeignKey('drivers.id'))


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.String(40), primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    rutas = db.relationship('Ruta', back_populates='drivers')


class EventosAsignacion(db.Model):
    __tablename__ = "eventos_asignacion"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
