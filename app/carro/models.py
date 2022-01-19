from app.extensions import db
from flask import Blueprint


carro_api = Blueprint("carro_api", __name__)

class Carro(db.Model):

    __tablename__ = "carro"

    id = db.Column(db.Integer, primary_key = True, unique=True)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)
    modelo = db.Column(db.String(20), nullable=False)
    cor = db.Column(db.String(15), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer)
    linha = db.Column(db.String(20))

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho_de_compras.id"))
    carrinho = db.relationship("carrinho_de_compras", back_populates="carros")

    def json(self):
        return{
            "id": self.id,
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "ano": self.ano,
            "linha": self.linha
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