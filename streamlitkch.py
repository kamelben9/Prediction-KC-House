
import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import numpy as np

# Charger le modèle depuis le fichier
with open("pkl_kch_filename", 'rb') as file:
    pickle_model_lr = pickle.load(file)


st.title(" Estimez votre maison")
img = Image.open("house.png")
st.image(img, width=100) 


st.subheader(" Veuillez renseigner les champs ci-dessous")

bedroom = st.selectbox("Nombre de chambres", (1, 2, 3, 4))

bathroom = st.number_input("Nombre de salles de bain", min_value=0.)

sqft_liv = st.number_input("Surface totale du bien (en square feet)", 0, 10000)

sqft_lot = st.number_input("Surface totale du terrain (en square feet)", 0, 10000)

view = st.number_input("Aspect du bien", 0, 4)

sqft_above = st.number_input("Surface de la maison (en square feet)", 0, 10000)

sqft_base = st.number_input("Surface de la cave (en square feet)", 0, 10000)

floors = st.number_input("Nombre d'étages", min_value=0.)

waterfront = st.radio("Vue sur mer", ("Oui", "Non"))
if waterfront == "Oui":
    waterfront = 1
elif waterfront == "Non":
    waterfront = 0


condition = st.slider("Condition du bien (Sur une échelle de 1 a 10)", 0, 10)

grade = st.slider("Grade du bien (Sur une échelle de 1 a 10)", 0, 10)

yr_built = st.number_input("Année de construction")

yr_renovated = st.number_input("Année de rénovation")

zipcode = st.text_input("Code postal")

sqft_liv15 = st.slider("Moyenne de la surface des biens des 15 plus proches voisins (en square feet)", 0, 10000)

sqft_lot15 = st.slider("Moyenne de la surface des terrains des 15 plus proches voisins (en square feet)", 0, 10000)

year = st.number_input("Année de vente du bien")

liste =[int(bedroom), bathroom, int(sqft_liv), int(sqft_lot), floors,waterfront,int(view),int(condition), int(grade), int(sqft_above),int(sqft_base), int(yr_built), int(yr_renovated), zipcode, int(sqft_liv15), int(sqft_lot15), int(year)]

liste_col = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'sqft_living15', 'sqft_lot15', 'year']

if st.button("Démarrez l'estimation"):
    df = pd.DataFrame(np.array(liste).reshape(1, -1),columns = liste_col)
    st.write(liste)
    st.write(pickle_model_lr.predict(df))
    price = int(pickle_model_lr.predict(df))
    st.success("{}$".format(price))