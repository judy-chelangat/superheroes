from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    super_name=db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

# add any models you may need. 
   
    def __repr__(self):
        return f'<Hero {self.name} {self.super_name}>'
    
class HeroPowers(db.Model):
    __tablename='heropowers'
    id = db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String,nullable=False)
    hero_id=db.Column(db.Integer,db.ForeignKey('hero.id'))
    power_id=db.Column(db.Integer,db.ForeignKey('power.id'))
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

#defining the relationships
    hero=db.relationship('Hero',backref='hero_powers')
    power=db.relationship('Power',backref='hero_powers')


    def __repr__(self):
        return f'<Heropowers {self.strength} >'
    
class Power(db.Model):
    __tablename__='power'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

   
    def __repr__(self):
        return f'<power {self.name} {self.description}>'
    