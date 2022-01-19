from .extensions import db

class BaseModel(db.Model):

    create_time = db.Column(db.string)
    update_time = db.Column(db.string)


    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()