import os
import streamlit as st
# Define la ruta base de los archivos multimedia
base_path = os.path.join(os.path.dirname(__file__), 'material')

# Define las categorías con detalles y rutas de imágene
categories = [
    {
        'id': 'social-development',
        'title': 'Desarrollo Social',
        'description': 'Selecciona',
        'details': [
            {'title': 'Índice de desarrollo humano', 'url': '/gender-indicators/social-development/index-desarrollo-humano'},
            {'title': 'Índice de Desarrollo Humano en Educación para las Mujeres', 'url': '/gender-indicators/social-development/educacion-mujeres'},
            {'title': 'Índice de Desarrollo Humano en Ingreso de las Mujeres', 'url': '/gender-indicators/social-development/ingreso-mujeres'},
            {'title': 'Índice de Desarrollo Humano en Salud para las Mujeres', 'url': '/gender-indicators/social-development/salud-mujeres'},
            {'title': 'Índice de Desigualdad de Género', 'url': '/gender-indicators/social-development/desigualdad-genero'},
        ],
        'image': os.path.join(base_path, 'gen_social.png'),
        'background': os.path.join(base_path, 'desarrolloh.jpg')
    },
    {
        'id': 'economy',
        'title': 'Economía',
        'description': 'Selecciona',
        'details': [
            {'title': 'Promedio de horas a la semana dedicadas al trabajo no remunerado de los hogares', 'url': '/gender-indicators/economy/trabajo-no-remunerado'},
            {'title': 'Tasa de desocupación desagregada por sexo', 'url': '/gender-indicators/economy/desocupacion'},
            {'title': 'Tasa de desocupación desagregada por sexo en adolescentes de 15 a 16 años de edad', 'url': '/gender-indicators/economy/desocupacion-adolescentes'},
            {'title': 'Tasa de ocupación desagregada por sexo', 'url': '/gender-indicators/economy/ocupacion'},
            {'title': 'Tasa de participación económica desagregada por sexo', 'url': '/gender-indicators/economy/participacion-economica'},
        ],
        'image': os.path.join(base_path, 'gen_economia.png'),
        'background': os.path.join(base_path, 'economia.png')
    },
    {
        'id': 'politics',
        'title': 'Política',
        'description': 'Selecciona',
        'details': [
            {'title': 'Distribución de escaños legislativos desagregada por sexo', 'url': '/gender-indicators/politics/escanos-legislativos'},
            {'title': 'Distribución de presidencias municipales desagregada por sexo', 'url': '/gender-indicators/politics/presidencias-municipales'},
            {'title': 'Integración de ayuntamientos por sexo', 'url': '/gender-indicators/politics/ayuntamientos'},
        ],
        'image': os.path.join(base_path, 'gen_politica.png'),
        'background': os.path.join(base_path, 'politica.png')
    },
    {
        'id': 'health',
        'title': 'Salud',
        'description': 'Selecciona',
        'details': [
            {'title': 'Incidencia registrada de Infecciones de Transmisión Sexual en mujeres de 10 a 19 años', 'url': '/gender-indicators/health/its-mujeres'},
            {'title': 'Porcentaje de mujeres de 15 a 24 años con necesidad insatisfecha de métodos anticonceptivos', 'url': '/gender-indicators/health/metodos-anticonceptivos'},
            {'title': 'Porcentaje de población desagregada por sexo, afiliada a servicios de salud', 'url': '/gender-indicators/health/servicios-salud'},
            {'title': 'Razón de mortalidad materna por cada 100,000 nacidos vivos', 'url': '/gender-indicators/health/mortalidad-materna'},
            {'title': 'Tasa de defunción de mujeres por tumor maligno', 'url': '/gender-indicators/health/tumor-maligno'},
            {'title': 'Tasa de defunción de mujeres por tumor maligno de mama', 'url': '/gender-indicators/health/tumor-mama'},
            {'title': 'Tasa de defunción de mujeres por tumor maligno del cuello de útero', 'url': '/gender-indicators/health/tumor-cuello-uterino'},
            {'title': 'Tasa Específica de Fecundidad en mujeres adolescentes de 15 a 19 años de edad', 'url': '/gender-indicators/health/fecundidad-15-19'},
            {'title': 'Tasa Específica de Fecundidad en niñas de 10 a 14 años de edad', 'url': '/gender-indicators/health/fecundidad-10-14'}
        ],
        'image': os.path.join(base_path, 'gen_salud.png'),
        'background': os.path.join(base_path, 'salud.jpg')
    },
    {
        'id': 'security-violence',
        'title': 'Seguridad y violencia',
        'description': 'Selecciona',
        'details': [
            {'title': 'Cifra negra de incidencia delictiva ocurrida en mujeres', 'url': '/gender-indicators/security-violence/cifra-negra'},
            {'title': 'Porcentaje de mujeres que vivieron violencia en los últimos 12 meses', 'url': '/gender-indicators/security-violence/violencia-12-meses'},
            {'title': 'Porcentaje de municipios que cuentan con una instancia o centro para la atención a las violencias contra las mujeres', 'url': '/gender-indicators/security-violence/municipios-instan'},
            {'title': 'Prevalencia de las violencias hacia las mujeres', 'url': '/gender-indicators/security-violence/prevalencia-violencias'},
            {'title': 'Prevalencia de violencia económica o patrimonial hacia las mujeres', 'url': '/gender-indicators/security-violence/violencia-economica'},
            {'title': 'Prevalencia de violencia emocional hacia las mujeres', 'url': '/gender-indicators/security-violence/violencia-emocional'},
            {'title': 'Prevalencia de violencia física hacia las mujeres', 'url': '/gender-indicators/security-violence/violencia-fisica'},
            {'title': 'Prevalencia de violencia sexual hacia las mujeres', 'url': '/gender-indicators/security-violence/violencia-sexual'},
            {'title': 'Tasa de feminicidios por cada 100 mil mujeres', 'url': '/gender-indicators/security-violence/feminicidios'},
            {'title': 'Tasa de homicidios dolosos de mujeres por cada 100 mil mujeres', 'url': '/gender-indicators/security-violence/homicidios-dolosos'}
        ],
        'image': os.path.join(base_path, 'gen_seguridad.png'),
        'background': os.path.join(base_path, 'seguridadvio.jpg')
    },
    {
        'id': 'education',
        'title': 'Educación',
        'description': 'Selecciona',
        'details': [
            {'title': 'Porcentaje de abandono escolar en el nivel media superior, desagregado por sexo', 'url': '/gender-indicators/education/abandono-escolar'},
            {'title': 'Porcentaje de absorción en la educación media superior, desagregado por sexo', 'url': '/gender-indicators/education/absorcion-media-superior'},
        ],
        'image': os.path.join(base_path, 'gen_educacion.png'),
        'background': os.path.join(base_path, 'educacion.png')
    }
]
