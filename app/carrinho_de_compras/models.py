from app.extensions import db
from flask import Blueprint


carrinho_de_compras_api = Blueprint("carrinho_de_compras_api", __name__)

class CarrinhoDeCompras(db.Model):
    __tablename__ = "carrinho_de_compras"
    
    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)
    quantidade_de_itens = db.Column(db.Integer)
    valor = db.Column(db.String(15), nullable=False)
    valor_pos_desconto = db.Column(db.String(15))
    data_de_adicao_ultimo_item = db.Column(db.Time)
    quantidade_maxima = db.Column(db.SmallInteger)


    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("user", back_populates="carrinho_de_compras")
    carros = db.relationship("carro", back_populates="carrinho_de_compras")
    motos = db.relationship("moto", back_populates="carrinho_de_compras")
    cupom = db.relationship("cupom", back_populates="carrinho_de_compras", uselist=False)

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