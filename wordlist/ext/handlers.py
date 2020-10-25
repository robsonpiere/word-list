from flask import Flask


def handle_400(e):
    if type(e.description) is list:
        return {
                   'code': 400,
                   "message": "Não foi possível validar todos os campos.",
                   "details:": e.description
               }, 400
    return default_message(e, 400)


def handle_404(e):
    return default_message(e, 404)


def handle_405(e):
    return default_message(e, 405)


def handle_500(e):
    return {'code': 500, "message:": "Ocorreu um erro interno na aplicação."}, 500


def default_message(error, code: int):
    return {'code': code, "message:": error.description}, code


def init_app(app: Flask) -> None:
    """
    Adiciona handlers a aplicação
    """
    app.register_error_handler(400, handle_400)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    app.register_error_handler(500, handle_500)
