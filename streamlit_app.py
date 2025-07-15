import streamlit as st

st.title("Halo! Selamat datang di Game Kimia!")
st.title("Kamu mau ngapain dulu nih?")
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
