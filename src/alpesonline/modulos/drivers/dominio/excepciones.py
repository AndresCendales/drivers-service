""" Excepciones del dominio de drivers

En este archivo usted encontrará los Excepciones relacionadas
al dominio de drivers

"""

from alpesonline.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioDriversExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de drivers'):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
