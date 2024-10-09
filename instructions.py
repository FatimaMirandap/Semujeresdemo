import streamlit as st # type: ignore

def load_instructions_styles():
    st.markdown("""
    <style>
    .instructions-container {
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        text-align: center;  /* Centramos el texto */
    }
    .instructions-title {
        font-size: 2em;
        color: #4B0082;
        margin-bottom: 10px;
    }
    .instruction-section {
        margin: 15px 0;
    }
    .instruction-section h3 {
        color: #0078a8;
        font-size: 1.5em;
    }
    .instruction-text {
        font-size: 1.1em;
        line-height: 1.5;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def show_general_instructions():
    load_instructions_styles()
    st.markdown('<div class="instructions-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="instructions-title">Instrucciones Generales de Uso de la Página</h2>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Utiliza la barra de navegación superior para acceder a las secciones de la página y por cada sección puedes acceder a la barra lateral. Cada sección está claramente etiquetada para facilitar la selección.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_map_instructions():
    load_instructions_styles()
    st.markdown('<div class="instructions-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="instructions-title">Instrucciones para el Mapa Digital</h2>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Las capas en el mapa digital representan diferentes conjuntos de datos. Al seleccionar una capa, podrás visualizar información específica en el mapa.</p>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Asegúrate de explorar las subcapas y haz clic en los elementos del mapa para obtener más información.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_gender_indicators_instructions():
    load_instructions_styles()
    st.markdown('<div class="instructions-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="instructions-title">Instrucciones para Indicadores de Género</h2>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Los indicadores son métricas que representan aspectos clave del género. Están divididos en categorías para facilitar la navegación.</p>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Selecciona una categoría para ver los indicadores disponibles y sus metadatos asociados.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_crv_instructions():
    load_instructions_styles()
    st.markdown('<div class="instructions-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="instructions-title">Instrucciones para CRV (Centros de Referencia para la Violencia)</h2>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Los CRV son centros que brindan apoyo a víctimas de violencia. Puedes encontrar el CRV más cercano utilizando el listado en la barra lateral.</p>', unsafe_allow_html=True)
    st.markdown('<p class="instruction-text">Al hacer clic en un CRV, podrás ver su ubicación en el mapa junto con su contacto y dirección.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
