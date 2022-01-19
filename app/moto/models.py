from app.extensions import db
from flask import Blueprint


moto_api = Blueprint("moto_api", __name__)

class Moto:

    __tablename__ = "moto"

    id = db.Column(db.Integer, primary_key = True)
    create_time = db.Column(db.String)
    update_time = db.Column(db.String)
    modelo = db.Column(db.String)
    cor = db.Column(db.String)
    preco = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    linha = db.Column(db.String)

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho"))
    carrinho = db.relationship("carrinho", back_populates="motos")

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