import streamlit as st # type: ignore

def load_styles():
    st.markdown("""
    <style>
    /* Aquí incluyes todos los estilos CSS personalizados */
    .footer {
        background-color: #b486d4;
        padding: 10px;
        color: white;
        text-align: center;
    }
    .footer2 {
        background-color: #ce0f0f8d;
        color: black;
        padding: 2px;
        text-align: center;
        font-size: 1.4em;
    }
    /* Agrega aquí el resto del CSS adaptado */
    </style>
    """, unsafe_allow_html=True)
