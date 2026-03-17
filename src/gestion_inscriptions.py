import re
from typing import Optional, List, Dict

class GestionInscriptions:
    """Système d'inscription des étudiants."""

    def __init__(self):
        self.etudiants: List[Dict] = []  # Liste des étudiants inscrits

    def ajouter_etudiant(self, nom: str, email: str, age: int, numero_etudiant: str) -> Dict:
        """
        Ajoute un étudiant après validation.
        Retourne le dictionnaire de l'étudiant en cas de succès.
        Lève une exception ValueError si les données sont invalides.
        """
        # Validation du nom
        if not nom or not isinstance(nom, str) or len(nom.strip()) == 0:
            raise ValueError("Le nom ne peut pas être vide")

        # Validation de l'email (simple)
        pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern_email, email):
            raise ValueError("Email invalide")

        # Validation de l'âge
        if not isinstance(age, int) or age < 18:
            raise ValueError("L'âge doit être un entier supérieur ou égal à 18")

        # Validation du numéro d'étudiant
        if not numero_etudiant or not isinstance(numero_etudiant, str) or len(numero_etudiant.strip()) == 0:
            raise ValueError("Le numéro d'étudiant ne peut pas être vide")

        # Vérifier l'unicité du numéro d'étudiant
        for e in self.etudiants:
            if e['numero_etudiant'] == numero_etudiant:
                raise ValueError("Ce numéro d'étudiant existe déjà")

        # Vérifier l'unicité de l'email
        for e in self.etudiants:
            if e['email'] == email:
                raise ValueError("Cet email est déjà utilisé")

        etudiant = {
            'nom': nom.strip(),
            'email': email,
            'age': age,
            'numero_etudiant': numero_etudiant.strip()
        }
        self.etudiants.append(etudiant)
        return etudiant

    def trouver_par_email(self, email: str) -> Optional[Dict]:
        """Recherche un étudiant par email. Retourne None si non trouvé."""
        for e in self.etudiants:
            if e['email'] == email:
                return e
        return None

    def trouver_par_numero(self, numero_etudiant: str) -> Optional[Dict]:
        """Recherche un étudiant par numéro d'étudiant."""
        for e in self.etudiants:
            if e['numero_etudiant'] == numero_etudiant:
                return e
        return None

    def compter(self) -> int:
        """Retourne le nombre d'étudiants inscrits."""
        return len(self.etudiants)

    def obtenir_tous(self) -> List[Dict]:
        """Retourne la liste de tous les étudiants."""
        return self.etudiants.copy()