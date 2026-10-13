from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Personne(Base):
    __tablename__ = "personnes"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"Personne(id={self.id}, " f"nom='{self.nom}', " f"prenom='{self.prenom}', " f"email='{self.email}')"
