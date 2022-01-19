from app.extensions import db
from flask import Blueprint


cupom_api = Blueprint("cupom_api", __name__)

class Cupom(db.Model):

    __tablename__ = "cupom"

    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)
    porcentagem = db.Column(db.Boolean) #Se for em porcentagem, True. Em valor real, False
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    valor = db.Column(db.Integer)
    valor_minimo = db.Column(db.Integer)
    valor_maximo = db.Column(db.Integer)

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho_de_compras.id"))
    carrinho = db.relationship("carrinho_de_compras", back_populates="cupom")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
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
