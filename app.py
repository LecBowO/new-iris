import streamlit as st
import pickle
import sklearn

st.title("IRIS FLOWER PRIDICTOR")
st.image("images/main-iris.png", width=280)

target = ['setosa', 'versicolor', 'virginica']

model = pickle.load(open('model.pkl', 'rb'))

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    sepal_length = st.number_input("Enter Sepal Length")
with col2:
    sepal_width = st.number_input("Enter Sepal Width")
with col3:
    petal_length = st.number_input("Enter Petal Length")
with col4:
    petal_width = st.number_input("Enter Petal Width")

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction == 0:
        prediction = "Sentosa"
        st.image("images/sentosa.png")
    elif prediction == 1:
        prediction = "Versicolor"
        st.image("images/versicolor.png", width=225)
    else:
        prediction = 'Virginica'
        st.image("images/virginica.png", width=225)

    st.subheader(prediction)