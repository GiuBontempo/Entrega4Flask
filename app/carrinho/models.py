from app.extensions import db
from flask import Blueprint


carrinho_api = Blueprint("carrinho_api", __name__)

class Carrinho:
    __tablename__ = "carrinho"
    
    id = db.Column(db.Integer, primary_key = True)
    create_time = db.Column(db.String)
    update_time = db.Column(db.String)
    quantidade_de_itens = db.Column(db.Integer)
    reais = db.Column(db.String)
    valor_pos_desconto = db.Column(db.String)
    data_de_adicao_ultimo_item = db.Column(db.String)
    quantidade_maxima = db.Column(db.Integer)


    user_id = db.Column(db.Integer, db.ForeignKey("user"))
    user = db.relationship("user", back_populates="carrinho")
    carros = db.relationship("carro", back_populates="carrinho")
    motos = db.relationship("moto", back_populates="carrinho")
    cupom = db.relationship("cupom", back_populates="carrinho", uselist=False)

    def json(self):
        return {
            "id": self.id,
            "quantidade_de_itens": self.quantidade_de_itens,
            "valor": self.valor,
            "valor_pos_desconto": self.valor_pos_desconto,
            "data_de_adicao_ultimo_item": self.data_de_adicao_ultimo_item,
            "quantidade_maxima": self.quantidade_maxima
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