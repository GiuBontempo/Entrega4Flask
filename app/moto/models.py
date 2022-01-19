from app.extensions import db
from flask import Blueprint


moto_api = Blueprint("moto_api", __name__)

class Moto(db.Model):

    __tablename__ = "moto"

    id = db.Column(db.Integer, primary_key = True, nullable = False, unique = True)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)
    modelo = db.Column(db.String(15))
    cor = db.Column(db.String(15))
    preco = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    linha = db.Column(db.String(15))

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho_de_compras.id"))
    carrinho = db.relationship("carrinho_de_compras", back_populates="motos")

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