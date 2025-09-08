import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
st.header(":red[Email Spam Classifier] ")
email = st.text_input(":blue[EMAIL]", placeholder='enter your email')
st.button('predict')
if email:
    data = [email]
    vect = vectorizer.transform(data).toarray()
    pred = model.predict(vect)
    if pred == 0:
        st.write("not spam")
    else:
        st.write("spam")

footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    right: 0;
    width: 100%;
    background-color: transparent;
    color: #888;
    text-align: right;
    padding: 10px;
    font-size: 14px;
}
</style>
<div class="footer">
    <p>Made by Nitesh Badgujar ✍️</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

