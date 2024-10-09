import streamlit as st  # type: ignore
from home import show_home
from map_section_custom import show_map_section
from gender_indicators import show_gender_indicators, show_indicator_details
from crv import crv
from styles import load_styles
from instructions import (show_general_instructions, 
                          show_map_instructions, 
                          show_gender_indicators_instructions, 
                          show_crv_instructions)

# Cargar estilos personalizados
load_styles()

# Configurar la página inicial si no existe en la sesión
if "page" not in st.session_state:
    st.session_state.page = "home"
if "show_instructions" not in st.session_state:
    st.session_state.show_instructions = True

# Navegación
st.write("### Navegación")
col1, col2, col3, col4 = st.columns(4)
if col1.button("Inicio"):
    st.session_state.page = "home"
    st.session_state.show_instructions = True
if col2.button("Mapa Digital"):
    st.session_state.page = "map"
    st.session_state.show_instructions = True
if col3.button("Indicadores"):
    st.session_state.page = "gender_indicators"
    st.session_state.show_instructions = True
if col4.button("CRV"):
    st.session_state.page = "state_data_bank"
    st.session_state.show_instructions = True

# Mostrar instrucciones antes de que el usuario seleccione algo
if st.session_state.show_instructions:
    if st.session_state.page == "home":
        show_general_instructions()
    elif st.session_state.page == "map":
        show_map_instructions()
    elif st.session_state.page == "gender_indicators":
        show_gender_indicators_instructions()
    elif st.session_state.page == "state_data_bank":
        show_crv_instructions()

    if st.button("Aceptar"):
        st.session_state.show_instructions = False  # Ocultar instrucciones al aceptar
else:
    # Renderizar el contenido de la sección seleccionada
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "map":
        show_map_section()
    elif st.session_state.page == "gender_indicators":
        show_gender_indicators()
    elif st.session_state.page == "state_data_bank":
        crv()

# Verificar si se ha seleccionado un indicador para mostrar detalles
if "selected_indicator" in st.session_state:
    show_indicator_details(st.session_state.selected_indicator)
    del st.session_state.selected_indicator  # Limpiar la variable de sesión después de mostrar los detalles

# Pie de página
st.markdown("""<div class="footer">© 2024 Semujeres</div>
<div class="footer2">Teléfonos: Emergencias 911 | Policía municipal (999) 942 00 60 | Cruz roja (999) 983 02 27 | Denuncia anónima 089</div>
""", unsafe_allow_html=True)
