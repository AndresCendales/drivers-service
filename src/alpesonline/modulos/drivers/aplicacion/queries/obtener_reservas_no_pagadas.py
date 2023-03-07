from alpesonline.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery


class ObtenerReservasNoPagadas(Query):
    ...

class ObtenerReservasNoPagadasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...