from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/docs"
API_URL = '../static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    base_url=SWAGGER_URL,
    api_url= API_URL,
    config= dict(app_name="Lista de palavras ")
)
