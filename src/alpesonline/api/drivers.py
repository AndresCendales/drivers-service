from alpesonline.seedwork.presentacion import api
import json
from alpesonline.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, session
from flask import Response
from alpesonline.modulos.drivers.aplicacion.mapeadores import MapeadorRutaDTOJson
from alpesonline.seedwork.aplicacion.comandos import ejecutar_commando
from alpesonline.seedwork.aplicacion.queries import ejecutar_query
from alpesonline.modulos.drivers.aplicacion.comandos.crear_reserva import AsignarRuta
from alpesonline.modulos.drivers.aplicacion.queries.obtener_reserva import ObtenerRutaAsignada

bp = api.crear_blueprint('drivers', '/drivers')


@bp.route('/rutas', methods=('POST',))
def asignar_ruta_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y 
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        ruta_dict = request.json

        map_ruta = MapeadorRutaDTOJson()
        ruta_dto = map_ruta.externo_a_dto(ruta_dict)

        comando = AsignarRuta(ruta=ruta_dto)

        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/rutas/<id>', methods=('GET',))
def dar_reserva_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerRutaAsignada(id))
        map_reserva = MapeadorReservaDTOJson()

        return map_reserva.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
