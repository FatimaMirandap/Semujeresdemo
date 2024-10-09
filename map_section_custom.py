import streamlit as st# type: ignore
import os

# Función para cargar estilos CSS personalizados
def load_map_styles():
    st.markdown("""
    <style>
    .map-section { display: flex; flex-direction: column; height: 100vh; font-family: 'Roboto', sans-serif; font-size: 35px; font-style: normal; }
    .map-section h2 { text-align: center; font-size: 8em; color: #4B0082; margin-bottom: 20px; font-family: 'Roboto', sans-serif; }
    .map-section p { text-align: center; font-size: 5em; color: #b3b1b1; margin-bottom: 35px; font-family: 'Roboto', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Función para cargar el contenido del HTML y mostrarlo en Streamlit
def mostrar_html(archivo_html):
    try:
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido_html = f.read()
        st.components.v1.html(contenido_html, height=600, scrolling=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo HTML en la ruta especificada: {archivo_html}")

# Función principal que muestra la sección del mapa
def show_map_section():
    load_map_styles()
    st.title("Mapa Digital")
    st.write("Haz zoom de acuerdo al propósito de consulta.")

    base_path = r"C:\Users\Fatim\Downloads\SEMUJERES\DESARROLLO\streamlitsemujeresapp\material"

    def get_layer_label(layer):
        return {
            'feminicidios': 'Feminicidios 2015-2023',
            'mujeres': 'Mujeres que hablan lenguas indígenas',
            'violencia': 'Tasa de casos de violencia por año',
            'violencia_familiar': 'Tasa de violencia familiar por año',
            'menores': 'Tasa menores'
        }.get(layer, '')

    def get_sub_layers(layer):
        sub_layers_dict = {
            'mujeres': [
                ('total', 'Cantidad total de mujeres por municipio'),
                ('etnia', 'Cantidad de mujeres que hablan lenguas indígenas'),
                ('porcentaje', 'Porcentaje de mujeres que hablan lenguas indígenas')
            ],
            'violencia': [
                ('2018', '2018'),
                ('2019', '2019'),
                ('2020', '2020'),
                ('2021', '2021'),
                ('casos 2021', 'Cantidad de casos de violencia 2021')
            ],
            'violencia_familiar': [
                ('2019', '2019'),
                ('2020', '2020'),
                ('2022', '2022'),
                ('casos 2022', 'Cantidad de casos de violencia 2022')
            ],
            'menores': [
                ('2017', '2017'),
                ('2018', '2018'),
                ('2019', '2019'),
                ('2020', '2020')
            ]
        }
        return sub_layers_dict.get(layer, [])

    def get_html_file_path(layer, sub_layer):
        if layer == 'feminicidios':
            return os.path.join(base_path, 'MapaDigital_Feminicidios.html')
        elif layer == 'mujeres':
            return {
                'total': os.path.join(base_path, 'MapaDigital_Totalmujeres.html'),
                'etnia': os.path.join(base_path, 'MapaDigital_Etniamujeres.html'),
                'porcentaje': os.path.join(base_path, 'MapaDigital_Porcentajeetniamujeres.html')
            }.get(sub_layer)
        elif layer == 'violencia':
            return {
                '2018': os.path.join(base_path, 'MapaDigital_Tasacasosviolencia2018.html'),
                '2019': os.path.join(base_path, 'MapaDigital_Tasacasosviolencia2019.html'),
                '2020': os.path.join(base_path, 'MapaDigital_Tasacasosviolencia2020.html'),
                '2021': os.path.join(base_path, 'MapaDigital_Tasacasosviolencia2021.html'),
                'casos 2021': os.path.join(base_path, 'MapaDigital_Numerocasosviolencia2021.html')
            }.get(sub_layer)
        elif layer == 'violencia_familiar':
            return {
                '2019': os.path.join(base_path, 'MapaDigital_Tasacasosviolenciafamiliar2019.html'),
                '2020': os.path.join(base_path, 'MapaDigital_Tasacasosviolenciafamiliar2020.html'),
                '2022': os.path.join(base_path, 'MapaDigital_Tasacasosviolenciafamiliar2022.html'),
                'casos 2022': os.path.join(base_path, 'MapaDigital_Casosviolenciafamiliar2022.html')
            }.get(sub_layer)
        elif layer == 'menores':
            return {
                '2017': os.path.join(base_path, 'MapaDigital_TEF10A14_2017.html'),
                '2018': os.path.join(base_path, 'MapaDigital_TEF10A14_2018.html'),
                '2019': os.path.join(base_path, 'MapaDigital_TEF10A14_2019.html'),
                '2020': os.path.join(base_path, 'MapaDigital_TEF10A14_2020.html')
            }.get(sub_layer)
        return None

    # Barra lateral para seleccionar capas
    st.sidebar.header("Capas del Mapa")
    selected_layer = st.sidebar.radio(
        "Selecciona la capa de consulta",
        options=["feminicidios", "mujeres", "violencia", "violencia_familiar", "menores"],
        format_func=get_layer_label
    )

    # Obtener las subcapas de la capa seleccionada
    sub_layers = get_sub_layers(selected_layer)

    # Si la capa seleccionada tiene subcapas, mostramos el selector de subcapas
    if sub_layers:
        selected_sub_layer = st.sidebar.selectbox(
            "Selecciona el sub-criterio",
            options=[sl[0] for sl in sub_layers],
            format_func=lambda x: dict(sub_layers).get(x, "")
        )
    else:
        selected_sub_layer = None

    # Obtener y mostrar el archivo HTML
    html_file_path = get_html_file_path(selected_layer, selected_sub_layer)
    if html_file_path:
        mostrar_html(html_file_path)

# Ejecutar la sección del mapa
show_map_section()