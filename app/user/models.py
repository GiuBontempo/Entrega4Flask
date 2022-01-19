from app.extensions import db
from app.models import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    cpf = db.Column(db.String(15), nullable = False)
    nome = db.Column(db.String(70))
    email = db.Column(db.String(70), unique = True, index = True)
    endereco = db.Column(db.String(70))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(10))

    carrinho = db.relationship("carrinho", back_populates="user", uselist=False)