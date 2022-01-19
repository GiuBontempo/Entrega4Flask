from app.extensions import db
from flask import Blueprint


user_api = Blueprint("user_api", __name__)

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)
    cpf = db.Column(db.String(20), nullable = False, unique=True)
    nome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(70), unique = True)
    endereco = db.Column(db.String(70))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(10))

    carrinho = db.relationship("carrinho_de_compras", back_populates="user", uselist=False)
    cupons = db.relationship("cupom", back_populates="user")

    def json(self):
        return {
            "id": self.id,
            "cpf": self.cpf,
            "nome": self.nome,
            "email": self.email,
            "endereco": self.endereco,
            "numero": self.numero,
            "complemento": self.complemento
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