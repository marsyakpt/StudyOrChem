import streamlit as st
def show_materi(topik):
            if topik=="Kimia Organik":
                    st.subheader("Materi Kimia Organik")
                    st.write("""
                    - Hidrokarbon
                    - Alkohol Fenol Eter
                    - Aldehid dan Keton
                    - Asam Kerboksilat
                    - Amina
                    """)
            else:
                        st.subheader("Materi Kimia Anorganik")
                        st.write("""
                        - Uji Nyala
                        - Uji Kualitatif
                        """)                        
