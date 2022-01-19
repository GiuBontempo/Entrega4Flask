from app.extensions import db
from flask import Blueprint


cupom_api = Blueprint("cupom_api", __name__)

class Cupom:

    __tablename__ = "cupom"

    id = db.Column(db.Integer, primary_key = True)
    create_time = db.Column(db.String)
    update_time = db.Column(db.String)
    porcentagem_ou_real = db.Column(db.String)
    codigo = db.Column(db.String)
    valor = db.Column(db.Integer)
    data_de_validade = db.Column(db.String)
    valor_maximo = db.Column(db.Integer)

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho"))
    carrinho = db.relationship("carrinho", back_populates="cupom")
    user_id = db.Column(db.Integer, db.ForeignKey("user"))
    user = db.relationship("user", back_populates="cupons")

    def json(self):
        return {
            "id": self.id,
            "porcentagem_ou_real": self.porcentagem_ou_real,
            "codigo": self.codigo,
            "valor": self.valor,
            "data_de_validade": self.data_de_validade,
            "valor_maximo": self.valor_maximo
        }

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
