from database import SessionLocal
from personne_repository import PersonneRepository

"""
session = SessionLocal()
try:
    personne = Personne(nom="DUPONT", prenom="Jean", email="jean.dupont@example.com")

    session.add(personne)
    session.commit()

    print("Personne créée")

finally:
    session.close()
"""

"""
personnes = session.query(Personne).all()

for p in personnes:
    print(p)

session.close()
"""

"""
personne = session.query(Personne).filter(Personne.id == 1).first()

personne.prenom = "Jacques"

session.commit()
"""

with SessionLocal() as session:
    repo = PersonneRepository(session)
    repo.creer("MARTIN", "Pierrot", "pierrot.martin@test.fr")
    for personne in repo.lister():
        print(personne)
