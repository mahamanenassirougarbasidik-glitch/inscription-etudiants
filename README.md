# Inscription des étudiants

Application simple de gestion des inscriptions d'étudiants avec validation des données et tests automatisés.

[![Build Status](https://travis-ci.com/votre-compte/inscription_etudiants.svg?branch=main)](https://travis-ci.com/votre-compte/inscription_etudiants)
[![Coverage Status](https://coveralls.io/repos/github/votre-compte/inscription_etudiants/badge.svg)](https://coveralls.io/github/votre-compte/inscription_etudiants)

## Fonctionnalités
- Ajouter un étudiant (nom, email, âge, numéro étudiant)
- Validation : nom non vide, email valide, âge ≥ 18, numéro unique
- Recherche par email ou par numéro
- Lister tous les étudiants

## Installation
```bash
pip install -r requirements.txt