from app.extensions import db
from app.models import BaseModel


class Moto(BaseModel):

    __tablename__ = "moto"

    id = db.Column(db.Integer, primary_key = True)
    modelo = db.Column(db.String)
    cor = db.Column(db.String)
    preco = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    linha = db.Column(db.String)

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho"))