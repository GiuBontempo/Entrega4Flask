from app.extensions import db
from app.models import BaseModel


class Cupom(BaseModel):

    __tablename__ = "cupom"

    id = db.Column(db.Integer, primary_key = True)
    porcentagem_ou_real = db.Column(db.String)
    codigo = db.Column(db.String)
    valor = db.Column(db.Integer)
    data_de_validade = db.Column(db.String)
    valor_maximo = db.Column(db.Integer)

    carrinho = db.relationship("carrinho")