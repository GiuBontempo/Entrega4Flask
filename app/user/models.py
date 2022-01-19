from app.extensions import db
from flask import Blueprint


user_api = Blueprint("user_api", __name__)

class User:

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    create_time = db.Column(db.String)
    update_time = db.Column(db.String)
    cpf = db.Column(db.String(15), nullable = False)
    nome = db.Column(db.String(70))
    email = db.Column(db.String(70), unique = True, index = True)
    endereco = db.Column(db.String(70))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(10))

    carrinho = db.relationship("carrinho", back_populates="user", uselist=False)
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