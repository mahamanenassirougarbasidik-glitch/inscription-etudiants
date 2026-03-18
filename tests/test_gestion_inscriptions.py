import pytest
from src.gestion_inscriptions import GestionInscriptions

# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

@pytest.fixture
def systeme_vide():
    """Fixture fournissant un système d'inscription vide."""
    return GestionInscriptions()

@pytest.fixture
def systeme_avec_etudiants():
    """Fixture avec deux étudiants pré-ajoutés (indépendante)."""
    systeme = GestionInscriptions()
    systeme.ajouter_etudiant("Tahirou Tchindo Djibril", "tahirou.tchindo@etudiant.fr", 22, "ET001")
    systeme.ajouter_etudiant("Mahamane Aboubacar Sidik", "mahamane.aboubacar@etudiant.fr", 23, "ET002")
    return systeme

# ------------------------------------------------------------------
# Tests unitaires de base
# ------------------------------------------------------------------

def test_ajout_etudiant_valide(systeme_vide):
    etudiant = systeme_vide.ajouter_etudiant("Abdou Ali", "abdou.ali@etudiant.fr", 21, "2025001")
    assert systeme_vide.compter() == 1
    assert etudiant['nom'] == "Abdou Ali"
    assert etudiant['email'] == "abdou.ali@etudiant.fr"
    assert etudiant['age'] == 21
    assert etudiant['numero_etudiant'] == "2025001"

def test_trouver_par_email(systeme_avec_etudiants):
    trouve = systeme_avec_etudiants.trouver_par_email("mahamane.aboubacar@etudiant.fr")
    assert trouve is not None
    assert trouve['nom'] == "Mahamane Aboubacar Sidik"
    assert systeme_avec_etudiants.trouver_par_email("inconnu@etudiant.fr") is None

def test_trouver_par_numero(systeme_avec_etudiants):
    trouve = systeme_avec_etudiants.trouver_par_numero("ET001")
    assert trouve is not None
    assert trouve['nom'] == "Tahirou Tchindo Djibril"
    assert systeme_avec_etudiants.trouver_par_numero("X999") is None

def test_compter():
    """Test de la méthode compter avec un système vide et un système avec étudiants."""
    systeme_vide = GestionInscriptions()
    assert systeme_vide.compter() == 0

    systeme_peuple = GestionInscriptions()
    systeme_peuple.ajouter_etudiant("Seydou Hamza", "seydou.hamza@etudiant.fr", 24, "ET003")
    systeme_peuple.ajouter_etudiant("Hamidou Ramatou", "hamidou.ramatou@etudiant.fr", 22, "ET004")
    assert systeme_peuple.compter() == 2

def test_obtenir_tous_copie(systeme_avec_etudiants):
    tous = systeme_avec_etudiants.obtenir_tous()
    assert len(tous) == 2
    # La modification de la copie ne doit pas affecter l'original
    tous.pop()
    assert systeme_avec_etudiants.compter() == 2

# ------------------------------------------------------------------
# Tests des cas d'erreur (validation)
# ------------------------------------------------------------------

def test_ajout_email_duplique(systeme_avec_etudiants):
    with pytest.raises(ValueError, match="Cet email est déjà utilisé"):
        systeme_avec_etudiants.ajouter_etudiant("Paul", "tahirou.tchindo@etudiant.fr", 25, "ET005")

def test_ajout_numero_duplique(systeme_avec_etudiants):
    with pytest.raises(ValueError, match="Ce numéro d'étudiant existe déjà"):
        systeme_avec_etudiants.ajouter_etudiant("Paul", "paul@etudiant.fr", 25, "ET001")

# ------------------------------------------------------------------
# Paramétrisation pour tester plusieurs cas invalides
# ------------------------------------------------------------------

@pytest.mark.parametrize("nom,email,age,numero,message_erreur", [
    ("", "test@etudiant.fr", 20, "E003", "Le nom ne peut pas être vide"),
    ("   ", "test@etudiant.fr", 20, "E004", "Le nom ne peut pas être vide"),
    ("Jean", "email_invalide", 20, "E005", "Email invalide"),
    ("Jean", "test@etudiant.fr", 17, "E006", "L'âge doit être un entier supérieur ou égal à 18"),
    ("Jean", "test@etudiant.fr", 20, "", "Le numéro d'étudiant ne peut pas être vide"),
    ("Jean", "test@etudiant.fr", 20, "   ", "Le numéro d'étudiant ne peut pas être vide"),
])
def test_ajout_etudiant_invalide(nom, email, age, numero, message_erreur):
    systeme = GestionInscriptions()
    with pytest.raises(ValueError, match=message_erreur):
        systeme.ajouter_etudiant(nom, email, age, numero)

# Avant (test qui réussit)
def test_ajout_etudiant_valide(systeme_vide):
    etudiant = systeme_vide.ajouter_etudiant("Jean", "jean@test.fr", 20, "2025001")
    assert etudiant['age'] == 20   # OK
    
    def test_ajout_etudiant_valide(systeme_vide):
    etudiant = systeme_vide.ajouter_etudiant("Jean", "jean@test.fr", 20, "2025001")
    assert etudiant['age'] == 999   # Va échouer
# ------------------------------------------------------------------
# Paramétrisation pour tester plusieurs cas valides avec la liste complète
# ------------------------------------------------------------------

@pytest.mark.parametrize("nom,email,age,numero", [
    ("Tahirou Tchindo Djibril", "tahirou.tchindo@etudiant.fr", 22, "ET001"),
    ("Mahamane Aboubacar Sidik", "mahamane.aboubacar@etudiant.fr", 23, "ET002"),
    ("Abdou Ali", "abdou.ali@etudiant.fr", 21, "ET003"),
    ("Seydou Hamza", "seydou.hamza@etudiant.fr", 24, "ET004"),
    ("Hamidou Ramatou", "hamidou.ramatou@etudiant.fr", 22, "ET005"),
    ("Oumarou Abdourahmane", "oumarou.abdourahmane@etudiant.fr", 25, "ET006"),
    ("Yayé Djabiri", "yaye.djabiri@etudiant.fr", 23, "ET007"),
    ("Moussa Awal", "moussa.awal@etudiant.fr", 21, "ET008"),
    ("Oumarou Tanda", "oumarou.tanda@etudiant.fr", 24, "ET009"),
])
def test_ajout_multiple_etudiants_valides(nom, email, age, numero):
    systeme = GestionInscriptions()
    etudiant = systeme.ajouter_etudiant(nom, email, age, numero)
    assert etudiant['nom'] == nom
    assert etudiant['email'] == email
    assert etudiant['age'] == age
    assert etudiant['numero_etudiant'] == numero