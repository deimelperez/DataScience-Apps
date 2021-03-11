import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import pickle


Setosa = Image.open('Setosa.jpg')
Versicolour = Image.open('Versicolor.jpg')
Virginica = Image.open('Virginica.jpg')

images = [Setosa, Versicolour, Virginica]


st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


clf = pickle.load(open('penguins_clf.pkl', 'rb'))

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

labels = ['Setosa', 'Versicolour', 'Virginica']

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(labels[int(prediction)])

st.subheader('Prediction Probability')
prediction_pro = pd.DataFrame(prediction_proba)
prediction_pro.columns = labels
st.write(prediction_pro)

st.subheader('Image: Iris ' + labels[int(prediction)])
st.image(images[int(prediction)], width=500)
