from .health import router as health_router
from .person import router as person_router

def configure_routes(app):
    app.register_blueprint(health_router)
    app.register_blueprint(person_router)