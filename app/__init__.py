from flask import Flask
from app.extensions import db, migrate
from app.config import Config
from app.carrinho_de_compras.models import *
from app.carro.models import *
from app.cupom.models import *
from app.moto.models import *
from app.user.models import *



def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(carrinho_de_compras_api)
    app.register_blueprint(carro_api)
    app.register_blueprint(cupom_api)
    app.register_blueprint(moto_api)
    app.register_blueprint(user_api)

    return app

