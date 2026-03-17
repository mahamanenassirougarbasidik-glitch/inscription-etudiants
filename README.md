# Inscription des étudiants

Application simple de gestion des inscriptions d'étudiants avec validation des données et tests automatisés.

[![Tests](https://github.com/mahamanenassirougarbasidik-glitch/inscription-etudiants/actions/workflows/ci.yml/badge.svg)](https://github.com/mahamanenassirougarbasidik-glitch/inscription-etudiants/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/mahamanenassirougarbasidik-glitch/inscription-etudiants/badge.svg)](https://coveralls.io/github/mahamanenassirougarbasidik-glitch/inscription-etudiants)

## Fonctionnalités
- Ajouter un étudiant (nom, email, âge, numéro étudiant)
- Validation : nom non vide, email valide, âge ≥ 18, numéro unique
- Recherche par email ou par numéro
- Lister tous les étudiants

## Installation
```bash
pip install -r requirements.txt