import streamlit as st # type: ignore
import os
import pandas as pd # type: ignore
from indicator_data import indicator_details
from categories_data import categories

# Define la ruta base de los archivos multimedia
base_path = r"C:\Users\Fatim\Downloads\SEMUJERES\DESARROLLO\streamlitsemujeresapp\material"

# Función para cargar los estilos CSS personalizados
def load_gender_indicators_styles():
    st.markdown("""
    <style>
    #gender-indicators { padding: 20px; background-color: #ffffff; }
    #gender-indicators h2 { text-align: center; font-size: 4em; color: #4B0082; margin-bottom: 20px; }
    .category { margin: 20px; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
    .category img { width: 150px; }
    </style>
    """, unsafe_allow_html=True)

# Función para mostrar la tabla de detalles del indicador
def show_indicator_table(data):
    st.markdown("""
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
    }
    .custom-table th, .custom-table td {
        border: 1px solid #0078a8;
        padding: 8px;
        text-align: left;
    }
    .custom-table th {
        background-color: #0078a8;
        color: white;
    }
    .custom-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    </style>
    """, unsafe_allow_html=True)

    table_html = "<table class='custom-table'><tr><th>Ficha Técnica</th><th>Metadatos</th></tr>"
    for key, value in data.items():
        table_html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

def show_indicator_details(indicator_key):
    details = indicator_details.get(indicator_key)
    if details:
        st.subheader(indicator_key)
        show_indicator_table(details)

        # Construir la ruta del archivo
        file_path = os.path.join(base_path, details['file'])
        
        # Verificar si el archivo existe
        if os.path.exists(file_path):
            # Botón de descarga para el archivo XLSX
            with open(file_path, "rb") as f:
                st.download_button(
                    label="Descargar archivo XLSX",
                    data=f,
                    file_name=f"{indicator_key}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.error("El archivo no se encontró.")

        if st.button("Regresar"):
            del st.session_state.selected_indicator
    else:
        st.error("Error al cargar los detalles del indicador")
        if st.button("Regresar"):
            del st.session_state.selected_indicator


def show_gender_indicators():
    load_gender_indicators_styles()
    st.markdown('<div id="gender-indicators">', unsafe_allow_html=True)
    st.markdown('<h2>Sistema de Indicadores de Género</h2>', unsafe_allow_html=True)
    st.markdown('<p>Selecciona la categoría de indicadores de tu interés</p>', unsafe_allow_html=True)

    selected_category = st.sidebar.selectbox("Selecciona una categoría", [category['title'] for category in categories])

    if 'selected_indicator' in st.session_state:
        show_indicator_details(st.session_state.selected_indicator)
    else:
        for category in categories:
            if category['title'] == selected_category:
                st.markdown(f"<h3 style='text-align: center;'>{category['title']}</h3>", unsafe_allow_html=True)
                st.image(category['background'], width=900)
                st.image(category['image'], width=120)
                cols = st.columns(2)
                for index, detail in enumerate(category['details']):
                    with cols[index % 2]:
                        if st.button(f"{detail['title']}", key=f"{detail['title']}-{category['id']}-{index}"):
                            st.session_state.selected_indicator = detail['title']
                            break

    st.markdown('</div>', unsafe_allow_html=True)

show_gender_indicators()