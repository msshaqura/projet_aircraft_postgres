"""
Application Streamlit pour visualiser les résultats de l'analyse
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Configuration de la page
st.set_page_config(
    page_title="Aircraft Data Analysis",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Couleurs neutres (fonctionnent en clair et sombre)
PRIMARY_BLUE = '#2C7DA0'
SECONDARY_BLUE = '#61A5C2'
ACCENT_BLUE = '#89C2D9'
DARK_GRAY = '#2C3E50'
MEDIUM_GRAY = '#5D6D7E'
LIGHT_GRAY = "#858A90"
WHITE = '#FFFFFF'

# CSS adaptable
st.markdown("""
    <style>
    .main-header {
        color: #2C7DA0;
        text-align: center;
        padding: 1rem;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .sub-header {
        color: #5D6D7E;
        text-align: center;
        padding: 0.5rem;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# SVG de l'avion (simple et universel)
aircraft_svg = """
<svg width="80" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M21 16L14 12L21 8V16Z" fill="#2C7DA0" stroke="#2C7DA0" stroke-width="1"/>
    <path d="M14 12L3 9L2 12L3 15L14 12Z" fill="#61A5C2" stroke="#61A5C2" stroke-width="1"/>
    <path d="M14 12L17 19L14 18L12 14L14 12Z" fill="#89C2D9" stroke="#89C2D9" stroke-width="1"/>
    <circle cx="16" cy="8" r="1" fill="#FFFFFF"/>
</svg>
"""

# Titre principal
st.markdown('<div class="main-header">✈️ Aircraft Data Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Analyse des vols, aéroports, RPM et croissance des compagnies aériennes</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    # Logo SVG
    st.markdown(aircraft_svg, unsafe_allow_html=True)
    st.markdown("### Aviation Analytics")
    st.markdown("---")
    st.markdown("## 🎯 Navigation")
    
    page = st.radio(
        "Choisissez une analyse:",
        ["✈️ Avions", "🛬 Aéroports", "📈 RPM", "📊 Croissance (ASM)"]
    )
    
    st.markdown("---")
    
    # Section présenté par
    st.markdown("### 👨‍💻 Présenté par")
    st.markdown("Mohammed SHAQURA")
    st.markdown("Data Analyst | Snowflake projet")
    st.markdown("---")
    
    st.markdown("### 🎯 Objectifs du projet")
    with st.expander("📋 Détail des analyses"):
        st.markdown("""
        **1. ✈️ Avions**
        - Classement des avions par nombre de vols
        
        **2. 🛬 Aéroports**
        - Classement par nombre de passagers
        - Double comptage (départ + arrivée)
        
        **3. 📈 RPM**
        - Meilleure année par compagnie
        - Évolution du RPM total
        
        **4. 📊 Croissance (ASM)**
        - Meilleure année par compagnie
        - Évolution de AVG(ASM)
        """)
    
    st.markdown("---")
    st.markdown("### 📊 Technologies")
    st.markdown("""
    | Technologie | Usage |
    |-------------|-------|
    | Python | Logique métier |
    | PostgreSQL | Base de données |
    | Streamlit | Dashboard |
    | Plotly | Visualisation |
    | Pandas | Manipulation |
    """)

# Chargement des données
@st.cache_data
def load_data(file_name):
    """Charge les données depuis le dossier results"""
    file_path = os.path.join('..', 'results', file_name)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return None

# Page: Avions
if page == "✈️ Avions":
    st.markdown("## ✈️ Question 1: Quel avion a volé le plus ?")
    st.markdown("*Classement des avions par nombre de vols effectués*")
    
    df_avions = load_data('question1_avions.csv')
    
    if df_avions is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.dataframe(
                df_avions.style.background_gradient(cmap='Blues', subset=['nombre_vols']),
                use_container_width=True
            )
        
        with col2:
            fig = px.bar(
                df_avions,
                x='nombre_vols',
                y='avion',
                orientation='h',
                title='Nombre de vols par avion',
                labels={'nombre_vols': 'Nombre de vols', 'nom_avion': 'Avion'},
                color='nombre_vols',
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=400,
                template='plotly_white',
                font=dict(color=DARK_GRAY),
                title_font_color=PRIMARY_BLUE
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 📊 Résumé")
        gagnant = df_avions.iloc[0]
        total = df_avions['nombre_vols'].sum()
        st.success(f"🏆 **Avion gagnant:** {gagnant['avion']} avec {gagnant['nombre_vols']:,} vols ({gagnant['nombre_vols']/total*100:.1f}% du total)")
    else:
        st.error("Fichier question1_avions.csv non trouvé")

# Page: Aéroports
elif page == "🛬 Aéroports":
    st.markdown("## 🛬 Question 2: Quel aéroport a transporté le plus de passagers ?")
    st.markdown("*Chaque vol compte pour l'aéroport de départ ET l'aéroport d'arrivée*")
    
    df_aeroports = load_data('question2_aeroports.csv')
    
    if df_aeroports is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.dataframe(
                df_aeroports.style.background_gradient(cmap='Blues', subset=['passagers']),
                use_container_width=True
            )
        
        with col2:
            fig = px.bar(
                df_aeroports,
                x='passagers',
                y='aeroport',
                orientation='h',
                title='Passagers transportés par aéroport',
                labels={'passagers': 'Nombre de passagers', 'aeroport': 'Aéroport'},
                color='passagers',
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=400,
                template='plotly_white',
                font=dict(color=DARK_GRAY),
                title_font_color=PRIMARY_BLUE
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 📊 Résumé")
        gagnant = df_aeroports.iloc[0]
        st.success(f"🏆 **Aéroport gagnant:** {gagnant['nom_aeroport']} avec {gagnant['passagers']:,} passagers")
        st.info("📌 Chaque vol compte pour l'aéroport de départ ET l'aéroport d'arrivée (double comptage)")
    else:
        st.error("Fichier question2_aeroports.csv non trouvé")

# Page: RPM
elif page == "📈 RPM":
    st.markdown("## 📈 Question 3: Meilleure année pour le Revenue Passenger-Miles (RPM)")
    st.markdown("*RPM = RPM_Domestic + RPM_International*")
    
    df_rpm_best = load_data('question3_rpm_best_year.csv')
    df_rpm_yearly = load_data('question3_rpm_yearly.csv')
    
    if df_rpm_best is not None and df_rpm_yearly is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### Meilleure année par compagnie")
            st.dataframe(
                df_rpm_best.style.background_gradient(cmap='Blues', subset=['rpm_total']),
                use_container_width=True
            )
        
        with col2:
            fig = px.line(
                df_rpm_yearly,
                x='Annee',
                y='rpm_total',
                color='compagnie',
                title='Évolution du RPM Total par compagnie',
                labels={'Annee': 'Année', 'rpm_total': 'RPM Total', 'compagnie': 'Compagnie'},
                markers=True,
                color_discrete_sequence=[PRIMARY_BLUE, SECONDARY_BLUE, ACCENT_BLUE]
            )
            fig.update_layout(
                template='plotly_white',
                font=dict(color=DARK_GRAY),
                title_font_color=PRIMARY_BLUE
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 📊 Résumé")
        for _, row in df_rpm_best.iterrows():
            st.success(f"🏆 **{row['compagnie']}:** Meilleure année {int(row['meilleure_annee'])} avec RPM_Total = {row['rpm_total']:,.0f}")
    else:
        st.error("Fichiers question3_rpm_*.csv non trouvés")

# Page: Croissance ASM
elif page == "📊 Croissance (ASM)":
    st.markdown("## 📊 Question 4: Meilleure année pour la croissance (Available Seat Miles)")
    st.markdown("*Indicateur: AVG(ASM_Domestic) par compagnie et par année*")
    
    df_asm_best = load_data('question4_croissance_best_year.csv')
    df_asm_yearly = load_data('question4_croissance_yearly.csv')
    
    if df_asm_best is not None and df_asm_yearly is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### Meilleure année par compagnie")
            st.dataframe(
                df_asm_best.style.background_gradient(cmap='Blues', subset=['avg_asm']),
                use_container_width=True
            )
        
        with col2:
            fig = px.line(
                df_asm_yearly,
                x='Annee',
                y='avg_asm',
                color='compagnie',
                title='Évolution de AVG(ASM) par compagnie',
                labels={'Annee': 'Année', 'avg_asm': 'AVG(ASM_Domestic)', 'compagnie': 'Compagnie'},
                markers=True,
                color_discrete_sequence=[PRIMARY_BLUE, SECONDARY_BLUE, ACCENT_BLUE]
            )
            fig.update_layout(
                template='plotly_white',
                font=dict(color=DARK_GRAY),
                title_font_color=PRIMARY_BLUE
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 📊 Résumé")
        for _, row in df_asm_best.iterrows():
            st.success(f"🏆 **{row['compagnie']}:** Meilleure année {int(row['meilleure_annee'])} avec AVG_ASM = {row['avg_asm']:,.0f}")
    else:
        st.error("Fichiers question4_croissance_*.csv non trouvés")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>✈️ Aircraft Data Analysis Dashboard | Données PostgreSQL | Visualisation Streamlit & Plotly</p>", unsafe_allow_html=True)