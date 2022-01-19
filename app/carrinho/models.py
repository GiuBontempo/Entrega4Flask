from app.extensions import db
from app.models import BaseModel

class Carrinho(BaseModel):
    __tablename__ = "carrinho"

    id = db.Column(db.Integer, primary_key = True)
    quantidade_de_itens = db.Column(db.Integer)
    valor = db.Column(db.String)
    valor_pos_desconto = db.Column(db.String)
    data_de_adicao_ultimo_item = db.Column(db.String)


    user_id = db.Column(db.Integer, db.ForeignKey("user"))
    user = db.relationship("user", back_populates="carrinho")
    carros = db.relationship("carro")
    motos = db.relationship("moto")