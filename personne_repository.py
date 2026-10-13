from models import Personne


class PersonneRepository:

    def __init__(self, session):
        self.session = session

    def creer(self, nom, prenom, email):
        p = Personne(nom=nom, prenom=prenom, email=email)

        self.session.add(p)
        self.session.commit()

        return p

    def rechercher_par_id(self, personne_id):
        return self.session.get(Personne, personne_id)

    def lister(self):
        return self.session.query(Personne).all()
