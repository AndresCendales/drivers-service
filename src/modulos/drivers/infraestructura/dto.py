"""DTOs para la capa de infrastructura del dominio de drivers

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de drivers

"""
from __future__ import annotations
from typing import List
from config.db import db
# from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
driver_ruta = db.Table('drivers_rutas', Base.metadata,
                         db.Column('driver_id', db.String(36), db.ForeignKey('drivers.id')),
                         db.Column('ruta_id', db.String(36), db.ForeignKey('rutas.id'))
                         )


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    nombre = db.Column(db.String(200), nullable=False)
    rutas =  db.relationship('Ruta')

class Ruta(db.Model):
    __tablename__ = "rutas"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False, primary_key=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, primary_key=True)
    zona = db.Column(db.String(10), nullable=False)
    hora_salida = db.Column(db.DateTime, nullable=False)
    tiempo_estimado = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.String(36), db.ForeignKey('drivers.id'))

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
# reservas_itinerarios = db.Table(
#     "reservas_itinerarios",
#     db.Model.metadata,
#     db.Column("reserva_id", db.String(40), db.ForeignKey("reservas.id")),
#     db.Column("odo_orden", db.Integer),
#     db.Column("segmento_orden", db.Integer),
#     db.Column("leg_orden", db.Integer),
#     db.Column("fecha_salida", db.DateTime),
#     db.Column("fecha_llegada", db.DateTime),
#     db.Column("origen_codigo", db.String(10)),
#     db.Column("destino_codigo", db.String(10)),
#     db.ForeignKeyConstraint(
#         ["odo_orden", "segmento_orden", "leg_orden", "fecha_salida", "fecha_llegada", "origen_codigo", "destino_codigo"],
#         ["itinerarios.odo_orden", "itinerarios.segmento_orden", "itinerarios.leg_orden", "itinerarios.fecha_salida", "itinerarios.fecha_llegada", "itinerarios.origen_codigo", "itinerarios.destino_codigo"]
#     )
# )
#
# class Reserva(db.Model):
#     __tablename__ = "reservas"
#     id = db.Column(db.String(40), primary_key=True)
#     fecha_creacion = db.Column(db.DateTime, nullable=False)
#     fecha_actualizacion = db.Column(db.DateTime, nullable=False)
#     itinerarios = db.relationship('Itinerario', secondary=reservas_itinerarios, backref='reservas')
#
# class Itinerario(db.Model):
#     __tablename__ = "itinerarios"
#     odo_orden = db.Column(db.Integer, primary_key=True, nullable=False)
#     segmento_orden = db.Column(db.Integer, primary_key=True, nullable=False)
#     leg_orden = db.Column(db.Integer, primary_key=True, nullable=False)
#     fecha_salida = db.Column(db.DateTime, nullable=False, primary_key=True)
#     fecha_llegada = db.Column(db.DateTime, nullable=False, primary_key=True)
#     origen_codigo = db.Column(db.String(10), nullable=False, primary_key=True)
#     destino_codigo= db.Column(db.String(10), nullable=False, primary_key=True)










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
