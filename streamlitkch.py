
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


condition = st.slider("Condition du bien (Sur une échelle de 1 a 10)", 0, 5)

grade = st.slider("Grade du bien (Sur une échelle de 1 a 10)", 0, 10)

yr_built = st.number_input("Année de construction")

yr_renovated = st.number_input("Année de rénovation")

zipcode = st.selectbox("Code postal", ('98178', '98125', '98028', '98136', '98074', '98053', '98003',
       '98198', '98146', '98038', '98007', '98115', '98107', '98126',
       '98019', '98103', '98002', '98133', '98040', '98092', '98030',
       '98119', '98112', '98052', '98027', '98117', '98058', '98001',
       '98056', '98166', '98023', '98070', '98148', '98105', '98042',
       '98008', '98059', '98122', '98144', '98004', '98005', '98034',
       '98075', '98116', '98010', '98118', '98199', '98032', '98045',
       '98102', '98077', '98108', '98168', '98177', '98065', '98029',
       '98006', '98109', '98022', '98033', '98155', '98024', '98011',
       '98031', '98106', '98072', '98188', '98014', '98055', '98039'))

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
    st.write(pickle_model_lr.predict(df))
    price = int(pickle_model_lr.predict(df))
    st.success("{}$".format(price))