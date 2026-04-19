# 🎯 Aircraft Analysis Dashboard using Postgres

[![Hugging Face Spaces](https://img.shields.io/badge/🤗-Live%20App-yellow)](https://huggingface.co/spaces/msshaqura/netflix_project)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Relational%20DB-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io)

🚀 Live Demo 👉 Try the app here:
[https://huggingface.co/spaces/msshaqura/aircraft_postgres_project]
# ✈️ Aircraft Data Analysis - PostgreSQL Version

## 📝 Contexte du Projet

Ce projet est une implémentation alternative d'une analyse de données d'aviation.  
Le projet original demandait l'utilisation de **Snowflake** (base de données cloud) et **Deepnote** (plateforme d'analyse collaborative).

**Pourquoi cette version PostgreSQL ?**

| Élément original | Alternative choisie | Justification |
|------------------|---------------------|---------------|
| Snowflake | PostgreSQL | Base de données relationnelle open-source, permettant de tester les concepts SQL sans dépendre d'un service cloud payant |
| Deepnote | Jupyter Notebook | Environnement de développement local, plus flexible et gratuit |

**Objectif :** Démontrer que les compétences SQL et l'analyse de données sont transférables entre différentes plateformes.

---

## 📊 Questions analysées

1. **✈️ Question 1 : Quel avion a volé le plus ?**  
   - Calcul du nombre de vols par avion à partir du tableau `individual_flights`

2. **🛬 Question 2 : Quel aéroport a transporté le plus de passagers ?**  
   - Calcul = nombre de vols × capacité de l'avion  
   - Double comptage : chaque vol compte pour l'aéroport de départ ET d'arrivée

3. **📈 Question 3 : Meilleure année pour le Revenue Passenger-Miles (RPM)**  
   - RPM_Total = RPM_Domestic + RPM_International  
   - Identification de l'année avec le RPM maximum par compagnie

4. **📊 Question 4 : Meilleure année pour la croissance (ASM)**  
   - Indicateur : AVG(ASM_Domestic) par compagnie et par année  
   - Plus la valeur est élevée, plus la compagnie a grandi

---

## 🏗️ Structure du Projet
aircraft-analysis-postgres/
- │
- ├── notebooks/
- │ └── aircraft_analysis.ipynb # Analyse exploratoire complète
- │
- ├── app/
- │ └── streamlit_app.py # Dashboard interactif
- │
- ├── data/
- │ ├── question1_avions.csv
- │ ├── question2_aeroports.csv  # Conformément aux instructions de l'énoncé, le nombre de passagers a été estimé à partir de la capacité des avions 
- | |                              multiplée par le nombre de vols par type d'appareils. 
- │ ├── question3_rpm_best_year.csv
- │ ├── question3_rpm_yearly.csv
- │ ├── question4_croissance_best_year.csv
- │ └── question4_croissance_yearly.csv
- │
- ├── src/
- │ ├── init.py
- │ └── database.py # Module de connexion PostgreSQL
- │
- ├── aircraft_db.sql # Script SQL original
- ├── requirements.txt
- ├── .env.example
- ├── .gitignore
- └── README.md


---

## 🚀 Installation et Exécution

### 1. Prérequis

- Python 3.9+
- PostgreSQL installé localement
- Jupyter Notebook

### 2. Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/aircraft-analysis-postgres.git
cd aircraft-analysis-postgres

# Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

3. Configuration de la base de données
# Créer la base de données PostgreSQL
psql -U postgres -c "CREATE DATABASE aircraft_db;"

# Importer les données
psql -U postgres -d aircraft_db -f aircraft_db.sql

4. Configuration des variables d'environnement
cp .env.example .env
# Modifier .env avec vos identifiants PostgreSQL

5. Exécuter l'analyse
# Lancer le Notebook
jupyter notebook notebooks/aircraft_analysis.ipynb

# Lancer le dashboard
streamlit run app/streamlit_app.py
📊 Résultats des Analyses
Question	Résultat
Q1 - Avion	Goose (g72) avec 1,008 vols (44.4% du total)
Q2 - Aéroport	Amazon Mothership (AMP) avec 2,423,400 passagers
Q3 - Meilleure année RPM	AA: 2015, FA: 2016, GA: 2016
Q4 - Meilleure année Croissance	AA: 2002, FA: 2016, GA: 2016
🔄 Liens avec les autres versions
Ce projet existe en deux versions pour démontrer l'adaptabilité des compétences SQL et d'analyse :

| Version           | Base de données       | Environnement         | Lien                                                  |
|-------------------|-----------------------|-----------------------|-------------------------------------------------------|
| PostgreSQL        | PostgreSQL (local)    | Jupyter Notebook      | https://github.com/msshaqura/projet_aircraft_postgres |
|-------------------|-----------------------|-----------------------|-------------------------------------------------------|	
| BigQuery          | BigQuery (cloud)      | Streamlit direct      |https://github.com/msshaqura/projet_aircraft_bigquery  |


Les deux versions utilisent exactement les mêmes requêtes SQL et produisent les mêmes résultats, prouvant que :

SQL est un langage standard et portable

Les compétences d'analyse sont indépendantes de la plateforme

L'approche peut être adaptée selon les besoins (local / cloud)

🛠️ Technologies Utilisées
Technologie	Usage
Python 3.9+	Langage principal
PostgreSQL	Base de données relationnelle
Jupyter Notebook	Analyse exploratoire (EDA)
Streamlit	Dashboard interactif
Plotly	Visualisations interactives
Pandas	Manipulation des données
👨‍💻 Auteur
Mohammed SHAQURA
Data Analyst | Projet d'analyse de données aircraft

