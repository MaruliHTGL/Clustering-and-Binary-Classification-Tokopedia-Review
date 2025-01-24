import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# import ml package
import joblib
import os   

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Defining a function to clean up the text
def clean(Text):
    text = re.sub('[^a-zA-Z]', ' ', Text) #Replacing all non-alphabetic characters with a space
    text = text.lower() #converting to lowecase
    text = word_tokenize(text)
    text = [stemmer.stem(word) for word in text if not word in stopwords.words("indonesian")]
    text = ' '.join(text)
    return text
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def load_vectorization(vectorization_file):
    loaded_vectorization = joblib.load(open(os.path.join(vectorization_file), 'rb'))
    return loaded_vectorization

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'> Input the Review </h2>", unsafe_allow_html=True)
    review = st.text_area('Enter the Tokopedia Review:', 'The Tokopedia Review')

    with st.expander("Your Selected Options"):
        result = {
            'Review': review,
        }

    # dataframe
    df_4 = pd.DataFrame({'Review': [review]})

    # clean text
    df_4["clean_text"] = df_4["Review"].apply(clean)

    st.markdown("<h2 style = 'text-align: center;'> Your Review </h2>", unsafe_allow_html=True)

    vectorization = load_vectorization("vectorization.pkl")
    vectorization_array = vectorization.transform(df_4["clean_text"])

    st.write(review)

    # prediction section
    st.markdown("<h2 style = 'text-align: center;'> Analysis Result </h2>", unsafe_allow_html=True)

    model = load_model("model_svc.pkl")  
    prediction = model.predict(vectorization_array)

    if prediction == 'Negative':
        st.warning("Negative Review")
        st.write('Halo Toppers, terima kasih atas rating yang kamu berikan. Kami akan terus melakukan perkembangan pada aplikasi Tokopedia untuk terus memberikan keamanan dan kenyamanan Toppers dalam bertransaksi. Silahkan sampaikan kritik/saran atau kendala transaksi kamu dengan menghubungi Tokopedia Care melalui tkp.me/supportMainapps.')
    else:
        st.success('Positive Review')
        st.write('Hi Toppers, terima kasih untuk rating dan ulasan baiknya, ya! Kami akan terus meningkatkan performa aplikasi, fitur serta layanan agar bisa memberikan pengalaman bertransaksi terbaik bagi semua pengguna. Yuk tingkatkan terus transaksi kamu!')