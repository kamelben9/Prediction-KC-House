
import streamlit as st
from PIL import Image
import pickle

# Charger depuis le fichier
with open("pkl_kch_filename", 'rb') as file:
    pickle_model_lr = pickle.load(file)


st.title(" Estimez votre maison")
img = Image.open("house.png")
st.image(img, width=100) 


st.subheader(" Veuillez renseigner les champs ci-dessous")

bedroom = st.selectbox("Nombre de chambres", ("1", "2", "3", "4"))

bathroom = st.selectbox("Nombre de salles de bain", ("1", "2", "3", "4"))

sqft_liv = st.slider("Surface totale du bien (en square feet)", 0, 100000)

sqft_lot = st.slider("Surface totale du terrain (en square feet)", 0, 100000)

view = st.slider("Aspect du bien", 0, 4)

sqft_above = st.slider("Surface de la maison (en square feet)", 0, 100000)

sqft_base = st.slider("Surface de la cave (en square feet)", 0, 100000)

floor = st.selectbox("Nombre d'étages", ("1", "2", "3", "4"))

waterfront = st.radio("Vue sur mer", ("Oui", "Non"))

condition = st.slider("Condition du bien (Sur une échelle de 1 a 10)", 0, 10)

grade = st.slider("Grade du bien (Sur une échelle de 1 a 10)", 0, 10)

yr_built = st.number_input("Année de construction")

yr_renovated = st.number_input("Année de rénovation")

zipcode = st.number_input("Code postal")

lat = st.float_input("Latitude ou est situé le bien")

long = st.float_input("Longitude ou est situé le bien")

sqft_liv15 = st.slider("Moyenne de la surface des biens des 15 plus proches voisins (en square feet)", 0, 100000)

sqft_lot15 = st.slider("Moyenne de la surface des terrains des 15 plus proches voisins (en square feet)", 0, 100000)

year = st.number_input("Année de vente du bien")

if st.button("Démarrez l'estimation"):
    pickle_model_lr.predict