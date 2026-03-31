"""
Application Streamlit pour visualiser les résultats de l'analyse
Version finale - Lit les données depuis le dossier data/
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuration de la page
st.set_page_config(
    page_title="Aircraft Data Analysis",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Couleurs
PRIMARY_BLUE = '#2C7DA0'
SECONDARY_BLUE = '#61A5C2'
ACCENT_BLUE = '#89C2D9'
DARK_GRAY = '#2C3E50'

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

aircraft_svg = """
<svg width="80" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M21 16L14 12L21 8V16Z" fill="#2C7DA0" stroke="#2C7DA0" stroke-width="1"/>
    <path d="M14 12L3 9L2 12L3 15L14 12Z" fill="#61A5C2" stroke="#61A5C2" stroke-width="1"/>
    <path d="M14 12L17 19L14 18L12 14L14 12Z" fill="#89C2D9" stroke="#89C2D9" stroke-width="1"/>
    <circle cx="16" cy="8" r="1" fill="#FFFFFF"/>
</svg>
"""

st.markdown('<div class="main-header">✈️ Aircraft Data Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Analyse des vols, aéroports, RPM et croissance des compagnies aériennes</div>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.markdown(aircraft_svg, unsafe_allow_html=True)
    st.markdown("### Aviation Analytics")
    st.markdown("---")
    st.markdown("## 🎯 Navigation")
    
    page = st.radio(
        "Choisissez une analyse:",
        ["✈️ Avions", "🛬 Aéroports", "📈 RPM", "📊 Croissance (ASM)"]
    )
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Présenté par")
    st.markdown("**Mohammed SHAQURA**")
    st.markdown("Data Analyst | Snowflake projet")
    st.markdown("---")
    
    st.markdown("### 🎯 Objectifs")
    with st.expander("📋 Détail des analyses"):
        st.markdown("""
        **1. ✈️ Avions** - Classement par nombre de vols
        **2. 🛬 Aéroports** - Classement par passagers (double comptage)
        **3. 📈 RPM** - Meilleure année par compagnie
        **4. 📊 Croissance** - Meilleure année AVG(ASM)
        """)

@st.cache_data
def load_data(file_name):
    """Charge les données depuis le dossier data/"""
    file_path = os.path.join('data', file_name)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return None

# Page: Avions
if page == "✈️ Avions":
    st.markdown("## ✈️ Question 1: Quel avion a volé le plus ?")
    df = load_data('question1_avions.csv')
    if df is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df)
        with col2:
            fig = px.bar(df, x='nombre_vols', y='avion', orientation='h', 
                         color='nombre_vols', color_continuous_scale='Blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig)
        total = df['nombre_vols'].sum()
        st.success(f"🏆 **Gagnant:** {df.iloc[0]['avion']} avec {df.iloc[0]['nombre_vols']:,} vols ({df.iloc[0]['nombre_vols']/total*100:.1f}%)")
    else:
        st.error("Fichier question1_avions.csv non trouvé")

# Page: Aéroports
elif page == "🛬 Aéroports":
    st.markdown("## 🛬 Question 2: Quel aéroport a transporté le plus de passagers ?")
    df = load_data('question2_aeroports.csv')
    if df is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df)
        with col2:
            fig = px.bar(df, x='passagers', y='aeroport', orientation='h',
                         color='passagers', color_continuous_scale='Blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig)
        st.success(f"🏆 **Gagnant:** {df.iloc[0]['aeroport']} avec {df.iloc[0]['passagers']:,} passagers")
    else:
        st.error("Fichier question2_aeroports.csv non trouvé")

# Page: RPM
elif page == "📈 RPM":
    st.markdown("## 📈 Question 3: Meilleure année pour le RPM")
    df_best = load_data('question3_rpm_best_year.csv')
    df_yearly = load_data('question3_rpm_yearly.csv')
    if df_best is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df_best)
        with col2:
            fig = px.line(df_yearly, x='Annee', y='rpm_total', color='compagnie', markers=True)
            fig.update_layout(height=400)
            st.plotly_chart(fig)
        for _, row in df_best.iterrows():
            st.success(f"🏆 **{row['compagnie']}:** {int(row['meilleure_annee'])} avec RPM = {row['rpm_total']:,.0f}")
    else:
        st.error("Fichiers question3_rpm_*.csv non trouvés")

# Page: Croissance ASM
elif page == "📊 Croissance (ASM)":
    st.markdown("## 📊 Question 4: Meilleure année pour la croissance")
    df_best = load_data('question4_croissance_best_year.csv')
    df_yearly = load_data('question4_croissance_yearly.csv')
    if df_best is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df_best)
        with col2:
            fig = px.line(df_yearly, x='Annee', y='avg_asm', color='compagnie', markers=True)
            fig.update_layout(height=400)
            st.plotly_chart(fig)
        for _, row in df_best.iterrows():
            st.success(f"🏆 **{row['compagnie']}:** {int(row['meilleure_annee'])} avec AVG_ASM = {row['avg_asm']:,.0f}")
    else:
        st.error("Fichiers question4_croissance_*.csv non trouvés")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>✈️ Aircraft Data Analysis Dashboard | Streamlit & Plotly</p>", unsafe_allow_html=True)