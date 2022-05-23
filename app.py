import databutton as db
import streamlit as st
from model import predict

@db.streamlit('/gen', cpu=2, memory='2056Mi')
def gen():
    st.title('text-generator ✌️✍️')

    text = st.text_area(label='write your text here', value='i found this app and it\'s just so...')
    if st.button('Generate the rest of the text'):
        generated = predict(text)
        st.markdown(generated[0]['generated_text'])
