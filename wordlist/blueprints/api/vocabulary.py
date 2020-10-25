from flask import Blueprint, request, abort
from wordlist.words.vocabulary import generate_vocabulary


def add_rules(blueprint: Blueprint):
    blueprint.add_url_rule(rule='/vocabulary', view_func=generate, methods=['POST'])


def generate():
    form: dict = request.get_json()
    validate_request(form)
    texts = form.get('textos')
    result_filter = form.get('filtrar', [])
    vocabulary = generate_vocabulary(texts=texts, result_filter=result_filter)
    return vocabulary


def validate_request(form):

    if form is None:
        abort(400, "Você deve enviar um json válido")

    details = []
    textos = form.get('textos', None)

    if textos is None:
        details.append(
            {'target': 'textos', "message": "o campo textos é obrigatório"}
        )

    filtrar = form.get('filtrar', [])

    if not isinstance(filtrar, list):
        details.append(
            {'target': 'filtrar', "message": "O filtro deve ser uma lista de strings"}
        )
    elif not all(isinstance(item, str) for item in filtrar):
        details.append(
            {'target': 'filtrar',
             "message": "O filtro deve ser uma lista de filtros válidos: textos, listaDePalavras, "
                        "listaDeDuasPalavras, vetorDePalavras, vetorDeDuasPalavras"}
        )

    if not details:
        return form

    abort(400, description=details)




