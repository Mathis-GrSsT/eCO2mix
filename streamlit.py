import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import altair as alt
import plotly.express as px
from PIL import Image   
import base64

df = pd.read_csv ("eco2mix-national-tr.csv", sep=';')

#Changement format de date 
df['Date'] = pd.to_datetime(df['Date'])

#Fitre date première semaine
start_date = '2021-12-01'
end_date = '2021-12-07'
semaine1 = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df_semaine1 = df.loc[semaine1]

#Fitre date première semaine
start_date = '2021-12-01'
end_date = '2021-12-07'
semaine1 = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df_semaine1_prod = df.loc[semaine1]

#Fitre date jour N°2
start_date = '2021-12-02'
jour_2 = (df['Date'] == start_date)
df_jour_2 = df.loc[jour_2]

#Fitre date jour N°2
start_date = '2021-12-02'
jour_2 = (df['Date'] == start_date)
df_jour_2_prod = df.loc[jour_2]

st.set_page_config(layout="wide")

def main():
    
    pages = {
        'Accueil' : accueil,
        'Consommation': page1,
        'Production': page2,
        'Mix énergétique': page3, 
        'Rejet CO2':page4}

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Accueil'
        })

    with st.sidebar:
        page = st.selectbox("", tuple(pages.keys()))

    pages[page]()

def accueil():
    image1 = Image.open('Image1.png')
    st.image(image1)

    st.markdown('##')
    st.markdown("<h1 style='text-align: center; color: black;'>Étude jeu de données : éCO2mix </h1>", unsafe_allow_html=True)
    st.markdown('##')

    st.markdown("<h5 style='text-align: center; color: black;'>Langage principal : Python  </h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: black;'>Librairies : Pandas, Numpy, Plotly Express  </h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: black;'>Outils : Google Collaboratory, VS CodeStreamlit </h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: black;'>Application : Streamlit </h6>", unsafe_allow_html=True)


def page1():
    
    st.markdown("<h1 style='text-align: center; color: black;'>1.Consommation</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Vue générale</h4>", unsafe_allow_html=True)
    
    fig1 = px.area(df, 
              x="Date - Heure", 
              y="Consommation (MW)", 
              title='Consommation(MW) en décembre 2021', 
              color_discrete_sequence=px.colors.qualitative.Set1
              )
    fig1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    st.plotly_chart (fig1,use_container_width=True)

    st.markdown("<h4 style='text-align: center; color: black;'>Focus semaine N°1</h4>", unsafe_allow_html=True)

    #Vue semaine 1
    fig2 = px.area(df_semaine1, 
              x="Date - Heure", 
              y="Consommation (MW)", 
              title='Consommation(MW) en décembre 2021 - semaine 1', 
              color_discrete_sequence=px.colors.qualitative.Vivid)
    fig2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart (fig2,use_container_width=True)

    st.markdown("<h4 style='text-align: center; color: black;'>Focus jour N°2</h4>", unsafe_allow_html=True)
    
    # Graphe consommation (MW) en fonction du temps 
    #Vue jour 2
    fig3 = px.area(df_jour_2, 
              x="Date - Heure", 
              y="Consommation (MW)", 
              title='Consommation(MW) en décembre 2021 - jour 2', 
              color_discrete_sequence=px.colors.qualitative.Set3_r)
              
    fig3.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    st.plotly_chart (fig3,use_container_width=True)

    st.markdown('##')

def page2():

    energies=['Fioul (MW)','Charbon (MW)','Gaz (MW)','Nucléaire (MW)','Eolien (MW)','Solaire (MW)','Hydraulique (MW)','Pompage (MW)','Bioénergies (MW)', 'Fioul - TAC (MW)' ,'Fioul - Cogénération (MW)' ,'Fioul - Autres (MW)' , 'Gaz - TAC (MW)', 'Gaz - Cogénération (MW)', 'Gaz - CCG (MW)', 'Gaz - Autres (MW)',"Hydraulique - Fil de l'eau + éclusée (MW)","Hydraulique - Lacs (MW)" ,"Hydraulique - STEP turbinage (MW)"	, "Bioénergies - Déchets (MW)",	"Bioénergies - Biomasse (MW)" ,	"Bioénergies - Biogaz (MW)"]
    df['Production (MW)'] = df[energies].sum(axis=1)

    st.markdown("<h1 style='text-align: center; color: black;'>2.Production</h1>", unsafe_allow_html=True)

    # Graphe production (MW) en fonction du temps 
    #Vue générale 
    fig4 = px.area(df, 
              x="Date - Heure", 
              y="Production (MW)", 
              title='Production(MW) en décembre 2021', 
               color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig4.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    st.plotly_chart (fig4,use_container_width=True)

    #Fitre date première semaine
    start_date = '2021-12-01'
    end_date = '2021-12-07'
    semaine1 = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df_semaine1_prod = df.loc[semaine1]   

    # Graphe production(MW) en fonction du temps 
    #Vue semaine 1
    fig5 = px.area(df_semaine1_prod, 
                x="Date - Heure", 
                y="Production (MW)", 
                title='Production(MW) en décembre 2021 - semaine 1', 
                color_discrete_sequence=px.colors.qualitative.Vivid)
    fig5.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    st.plotly_chart (fig5,use_container_width=True)

    #Fitre date jour N°2
    start_date = '2021-12-02'
    jour_2 = (df['Date'] == start_date)
    df_jour_2_prod = df.loc[jour_2]

    # Graphe production (MW) en fonction du temps 

    #Vue jour 2

    fig6 = px.area(df_jour_2_prod, 
                x="Date - Heure", 
                y="Production (MW)", 
                title='Production(MW) en décembre 2021 - jour 2', 
                color_discrete_sequence=px.colors.qualitative.Set3_r)
    fig6.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    st.plotly_chart (fig6,use_container_width=True)

def page3():

    df_somme_colonne = pd.DataFrame(df.sum(axis = 0, skipna = True))
    df_somme_colonne.reset_index()
    df_somme_colonne.drop(df_somme_colonne.index[range(7)], inplace=True)
    df_somme_colonne.drop(labels=["Ech. physiques (MW)","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Taux de CO2 (g/kWh)"], inplace=True)
    
    st.markdown("<h1 style='text-align: center; color: black;'>3.Mix énergétique</h1>", unsafe_allow_html=True)

    #Mix énergétique 
    fig7 = px.pie(df_somme_colonne, 
                values=0, 
                names=df_somme_colonne.index, 
                color_discrete_sequence=px.colors.qualitative.Pastel)
    fig7.update_layout(width=800,height=800,title = {'text': "Mix production d'énergies",
            'y':0.95, 
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top' 
            })
    st.plotly_chart (fig7,use_container_width=True)

    fossiles = df_somme_colonne[0][0] + df_somme_colonne[0][1] + df_somme_colonne[0][2] + df_somme_colonne[0][3] + df_somme_colonne[0][9] + df_somme_colonne[0][10] + df_somme_colonne[0][11] + df_somme_colonne[0][12] + df_somme_colonne[0][13] + df_somme_colonne[0][14] + df_somme_colonne[0][15] 
    renouvelables = df_somme_colonne[0][4] + df_somme_colonne[0][5] + df_somme_colonne[0][6] + df_somme_colonne[0][7] + df_somme_colonne[0][8] + df_somme_colonne[0][16] + df_somme_colonne[0][17] + df_somme_colonne[0][18] + df_somme_colonne[0][19] + df_somme_colonne[0][20] + df_somme_colonne[0][21]
    df_renouvelables_fossiles = pd.DataFrame({'renouvelables':[renouvelables], 'fossiles':[fossiles]})
    df_renouvelables_fossiles_tr = df_renouvelables_fossiles.transpose()
    df_renouvelables_fossiles_tr.reset_index(inplace=True)

    #Part énergies renouvelables et fossilles 

    fig8 = px.pie(df_renouvelables_fossiles_tr, 
                values=0,
                names='index', 
                color_discrete_sequence=px.colors.qualitative.Dark2_r)

    fig8.update_layout(width=600,height=600,title = {'text': "Production : mix énergétique",
            'y':0.95, 
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top' 
            })

    st.plotly_chart (fig8,use_container_width=True)

def page4():

    st.markdown("<h1 style='text-align: center; color: black;'>4.Rejet C02</h1>", unsafe_allow_html=True)

    fig9 = px.area(df, 
    x="Date - Heure", 
    y="Taux de CO2 (g/kWh)", 
    title='Rejet de CO2 par kWh produit', 
    color_discrete_sequence=px.colors.sequential.Inferno)

    fig9.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    st.plotly_chart (fig9,use_container_width=True)

if __name__ == "__main__":
    main()