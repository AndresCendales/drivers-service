from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
# from modulos.drivers.dominio.entidades import Reserva, Aeropuerto
from modulos.drivers.dominio.objetos_valor import Ruta, Orden, Ubicacion, ZonaEnum
from .dto import RutaDTO, UbicacionDTO, OrdenDTO

from datetime import datetime


class MapeadorRutaDTOJson(AppMap):
    def _procesar_ruta(self, ruta: dict) -> RutaDTO:
        ordenes: list[OrdenDTO] = list()
        for orden in ruta.get('ordenes', list()):
            ordenes.append(
                OrdenDTO(
                    origen=self._procesar_ubicacion(orden.get('origen')),
                    destino=self._procesar_ubicacion(orden.get('destino')),
                    tipo=orden.get('tipo'),
                    parada=orden.get('parada')
                )
            )
        return RutaDTO(
            id=ruta.get('ruta_id'),
            ordenes=ordenes,
            zona=ruta.get('zona'),
            hora_salida=ruta.get('hora_salida'),
            tiempo_estimado=ruta.get('tiempo_estimado')
        )

    @staticmethod
    def _procesar_ubicacion(ubicacion: dict) -> UbicacionDTO:
        return UbicacionDTO(ubicacion.get('lat'), ubicacion.get('lon'))

    def externo_a_dto(self, externo: dict) -> RutaDTO:
        return self._procesar_ruta(externo)

    def dto_a_externo(self, dto: RutaDTO) -> dict:
        return dto.__dict__


class MapeadorRuta(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_ruta(self, ruta_dto: RutaDTO) -> Ruta:
        ordenes: list[Orden] = list()
        for orden in ruta_dto.ordenes:
            ordenes.append(
                Orden(
                    origen=Ubicacion(orden.origen.lat, orden.origen.lon),
                    destino=Ubicacion(orden.destino.lat, orden.destino.lon),
                    tipo=orden.tipo,
                    parada=orden.parada
                )
            )

        return Ruta(
            fecha_creacion=datetime.strptime(ruta_dto.fecha_creacion, self._FORMATO_FECHA)  ,
            fecha_actualizacion=datetime.strptime(ruta_dto.fecha_actualizacion,self._FORMATO_FECHA),
            ordenes=ordenes,
            zona=ZonaEnum(ruta_dto.zona),
            hora_salida=datetime.strptime(ruta_dto.hora_salida, self._FORMATO_FECHA),
            tiempo_estimado=ruta_dto.tiempo_estimado
        )

    def obtener_tipo(self) -> type:
        return Reserva.__class__

    def entidad_a_dto(self, entidad: Ruta) -> RutaDTO:

        ordenes: list[OrdenDTO] = list()
        for orden in entidad.ordenes:
            ordenes.append(
                OrdenDTO(
                    origen=UbicacionDTO(orden.origen.lat, orden.origen.lon),
                    destino=UbicacionDTO(orden.destino.lat, orden.destino.lon),
                    tipo=orden.tipo.__str__(),
                    parada=orden.parada
                )
            )

        return RutaDTO(
            fecha_creacion=entidad.fecha_creacion.strftime(self._FORMATO_FECHA),
            fecha_actualizacion=entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA),
            ordenes=ordenes,
            zona=entidad.zona.__str__(),
            hora_salida=entidad.hora_salida.strftime(self._FORMATO_FECHA),
            tiempo_estimado=entidad.tiempo_estimado
        )

    def dto_a_entidad(self, dto: RutaDTO) -> Ruta:
        return self._procesar_ruta(dto)
