import os
import streamlit as st
#
base_path = os.path.join(os.path.dirname(__file__), 'material')

indicator_details = {
    'Índice de desarrollo humano': {
        'Descripción': 'Mide el grado de Desarrollo Humano de las personas en México desde tres dimensiones: salud, educación e ingreso.',
        'Periodicidad': 'Decenal',
        'Fórmula': 'A=A',
        'Fuente': 'Programa de las Naciones Unidas para el Desarrollo en México (PNUD).',
        'Línea Base': '0.739 (Unidad de medida: Puntos, Año de línea base: 2012)',
        'Verificación': 'Indicadores de Desarrollo Humano y Género en México: nueva metodología, 2014.',
        'link': 'https://www.mx.undp.org/content/mexico/es/home/library/poverty/indicadores-de-desarrollo-humano-y-genero-en-mexico--nueva-metod.html',
        'file': r"Sistema de Indicadores_actualización2024/Desarrollo social/Índice_de_Desarrollo_Humano_391.xlsx"
    },
    'Índice de Desarrollo Humano en Educación para las Mujeres': {
        'Descripción': 'Mide las posibilidades de desarrollo de las mujeres en el ámbito de educación, según los años promedio de estudios.',
        'Fórmula': 'A=A',
        'Periodicidad': 'Decenal',
        'Variables': 'A: Índice de Desarrollo Humano en Educación para las Mujeres',
        'Fuente': 'Programa de las Naciones Unidas para el Desarrollo en México (PNUD).',
        'Línea Base': '0.65 (Unidad de medida: Puntos, Año de línea base: 2012)',
        'Verificación': 'Indicadores de Desarrollo Humano y Género en México: nueva metodología, 2014.',
        'link': 'https://www.mx.undp.org/content/mexico/es/home/library/poverty/indicadores-de-desarrollo-humano-y-genero-en-mexico--nueva-metod.html',
        'file': r"Sistema de Indicadores_actualización2024/Desarrollo social/Índice_de_Desarrollo_Humano_en_Educación_para_las_Mujeres_388.xlsx"
    },
    'Índice de Desarrollo Humano en Ingreso de las Mujeres': {
        'Descripción': 'Mide el grado de desarrollo de las mujeres según su ingreso per cápita.',
        'Fórmula': 'A=A',
        'Periodicidad': 'Decenal',
        'Variables': 'A: Índice de Desarrollo Humano en Ingreso de las Mujeres',
        'Fuente': 'Programa de las Naciones Unidas para el Desarrollo en México (PNUD).',
        'Línea Base': '0.77 (Unidad de medida: Puntos, Año de línea base: 2012)',
        'Verificación': 'Indicadores de Desarrollo Humano y Género en México: nueva metodología, 2014.',
        'link': 'https://www.mx.undp.org/content/mexico/es/home/library/poverty/indicadores-de-desarrollo-humano-y-genero-en-mexico--nueva-metod.html',
        'file': r"Sistema de Indicadores_actualización2024/Desarrollo social/Índice_de_Desarrollo_Humano_en_Ingreso_de_las_Mujeres_387.xlsx"
    },
    'Índice de Desarrollo Humano en Salud para las Mujeres': {
        'Descripción': 'Mide la capacidad básica de contar con una vida larga y saludable, estimada por el índice de salud mediante la esperanza de vida al nacer de las mujeres.',
        'Fórmula': 'A=A',
        'Periodicidad': 'Decenal',
        'Variables': 'A: Índice de Desarrollo Humano en Salud para las Mujeres',
        'Fuente': 'Programa de las Naciones Unidas para el Desarrollo en México (PNUD).',
        'Línea Base': '0.91 (Unidad de medida: Puntos, Año de línea base: 2012)',
        'Verificación': 'Indicadores de Desarrollo Humano y Género en México: nueva metodología, 2014.',
        'link': 'https://www.mx.undp.org/content/mexico/es/home/library/poverty/indicadores-de-desarrollo-humano-y-genero-en-mexico--nueva-metod.html',
        'file': r"Sistema de Indicadores_actualización2024/Desarrollo social/Índice_de_Desarrollo_Humano_en_Salud_para_las_Mujeres_389.xlsx"
    },
    'Índice de Desigualdad de Género': {
        'Descripción': 'El índice muestra la pérdida en desarrollo humano debido a la desigualdad entre logros de mujeres y hombres en tres dimensiones: salud reproductiva, empoderamiento y participación en el mercado laboral.',
        'Fórmula': 'A=A',
        'Periodicidad': 'Decenal',
        'Variables': 'A: Índice de Desigualdad de Género',
        'Fuente': 'Programa de las Naciones Unidas para el Desarrollo en México (PNUD).',
        'Línea Base': '0.39 (Unidad de medida: Puntos, Año de línea base: 2012)',
        'Verificación': 'Indicadores de Desarrollo Humano y Género en México: nueva metodología, 2014.',
        'link': 'https://www.mx.undp.org/content/mexico/es/home/library/poverty/indicadores-de-desarrollo-humano-y-genero-en-mexico--nueva-metod.html',
        'file': r"Sistema de Indicadores_actualización2024/Desarrollo social/Índice_de_Desigualdad_de_Género_392.xlsx"
    },
    'Promedio de horas a la semana dedicadas al trabajo no remunerado de los hogares': {
        'Descripción': 'Mide el promedio de horas a la semana que dedican las mujeres, de 12 años y más, al trabajo no remunerado de los hogares. El promedio de horas a la semana dedicadas al trabajo no remunerado de los hogares se recaba a través de la Encuesta Nacional sobre Uso del Tiempo (ENUT), en el cual se contabiliza la población de 12 años y más que realiza actividades productivas, tasa de participación, horas semanales con su porcentaje y promedio, por entidad federativa, tipo de trabajo, grupo y tipo de actividad según sexo.',
        'Fórmula': 'A=A',
        'Periodicidad': 'Quinquenal',
        'Variables': 'A: Promedio de horas a la semana dedicadas al trabajo no remunerado de los hogares',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '48.77 (Unidad de medida: Promedio, Año de línea base: 2019)',
        'Verificación': 'Encuesta Nacional sobre Uso del Tiempo (ENUT).',
        'link': 'https://www.inegi.org.mx/programas/enut/2019/'
    },
    'Tasa de desocupación desagregada por sexo': {
        'Descripción': 'Mide la proporción de la población económicamente activa (PEA) que se encuentra sin trabajar, pero que está buscando trabajo, respecto del total de hombres y mujeres de 15 y más años de edad.',
        'Fórmula': 'A=(B/C)*100',
        'Periodicidad': 'Trimestral',
        'Variables': 'A: Tasa de desocupación desagregada por sexo, B: Población económicamente activa desocupada de 15 años y más, desagregada por sexo, C: Población económicamente activa de 15 años y más, desagregada por sexo',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '2.56 (Unidad de medida: Tasa, Año de línea base: 2019)',
        'Verificación': 'Encuesta Nacional de Ocupación y Empleo (ENOE).',
        'link': 'https://www.inegi.org.mx/programas/enoe/15ymas/'
    },
    'Tasa de desocupación desagregada por sexo en adolescentes de 15 a 19 años de edad': {
        'Descripción': 'Mide la proporción de la población de 15 a 19 años que se encontraba buscando activamente un empleo u ocupación, respecto de la población económicamente activa (PEA) de 15 a 19 años.',
        'Fórmula': 'A=(B/C)*100',
        'Periodicidad': 'Trimestral',
        'Variables': 'A: Tasa de desocupación desagregada por sexo en adolescentes de 15 a 19 años de edad, B: Población económicamente activa desocupada de 15 a 19 años, desagregada por sexo, C: Población económicamente activa de 15 a 19 años, desagregada por sexo',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '8.3 (Unidad de medida: Tasa, Año de línea base: 2020)',
        'Verificación': 'Microdatos de la Encuesta Nacional de Ocupación y Empleo (ENOE).',
        'link': 'https://www.inegi.org.mx/programas/enoe/15ymas/'
    },
    'Tasa de ocupación desagregada por sexo': {
        'Descripción': 'Mide la proporción de la población económicamente activa (PEA) ocupada, respecto del total de hombres y mujeres de 15 y más años de edad.',
        'Fórmula': 'A=(B/C)*100',
        'Periodicidad': 'Trimestral',
        'Variables': 'A: Tasa de ocupación desagregada por sexo, B: Población económicamente activa ocupada de 15 años y más, desagregada por sexo, C: Población económicamente activa de 15 años y más, desagregada por sexo',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '97.44 (Unidad de medida: Tasa, Año de línea base: 2019)',
        'Verificación': 'Encuesta Nacional de Ocupación y Empleo (ENOE).',
        'link': 'https://www.inegi.org.mx/programas/enoe/15ymas/'
    },
    'Tasa de participación económica desagregada por sexo': {
        'Descripción': 'Mide la proporción de la población económicamente activa (PEA) respecto del total de la población, según el sexo, de 15 y más años de edad.',
        'Fórmula': 'A=(B/C)*100',
        'Periodicidad': 'Trimestral',
        'Variables': 'A: Tasa de participación económica desagregada por sexo, B: Población económicamente activa (definida como las personas que trabajan o buscan trabajo) de 15 años y más, desagregada por sexo, C: Población de 15 años y más, desagregada por sexo',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '53.16 (Unidad de medida: Tasa, Año de línea base: 2019)',
        'Verificación': 'Encuesta Nacional de Ocupación y Empleo (ENOE).',
        'link': 'https://www.inegi.org.mx/programas/enoe/15ymas/'
    },
    'Distribución de escaños legislativos desagregada por sexo': {
        'Descripción': 'Mide la proporción de mujeres y hombres que integran los congresos locales.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Distribución de escaños legislativos desagregada por sexo; B: Número de diputadas/diputados en el Congreso Local de Yucatán; C: Total de escaños legislativos en el Congreso Local de Yucatán',
        'Periodicidad': 'Trianual',
        'Fuente': 'Cámara de Diputados LXV Legislatura.',
        'Línea Base': '48 (Unidad de medida: Porcentaje, Año de línea base: 2019)',
        'Verificación': 'Cámara de Diputados LXV Legislatura, composición política por entidad federativa.',
        'link': 'http://sitl.diputados.gob.mx/LXV_leg/composicion_politicanp.php'
    },
    'Distribución de presidencias municipales desagregada por sexo': {
        'Descripción': 'Mide la proporción de ayuntamientos gobernados por mujeres respecto al total de ayuntamientos del estado de Yucatán.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Distribución de presidencias municipales desagregada por sexo; B: Número de presidentas/presidentes municipales; C: Total de presidencias municipales',
        'Periodicidad': 'Trianual',
        'Fuente': 'INMUJERES.',
        'Línea Base': '26.42 (Unidad de medida: Porcentaje, Año de línea base: 2018)',
        'Verificación': 'Número y porcentaje de mujeres en alcaldías del país, por entidad federativa.',
        'link': 'https://datos.gob.mx/busca/dataset/liderazgo-politico-de-las-mujeres-en-mexico-de-inmujeres/resource/26d852a8-0493-4241-8d2f-68cd783fc3f0'
    },
    'Integración de ayuntamientos por sexo': {
        'Descripción': 'Mide el porcentaje de regidoras o regidores que integran las regidurías de los 106 ayuntamientos de Yucatán.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Integración de ayuntamientos por sexo; B: Número de regidores o regidoras por ayuntamiento; C: Total de regidurías',
        'Periodicidad': 'Trianual',
        'Fuente': 'Sistema Nacional de Información Municipal del INAFED.',
        'Línea Base': '52.65 (Unidad de medida: Porcentaje, Año de línea base: 2018)',
        'Verificación': 'Integración de Ayuntamientos.',
        'link': 'http://snim.rami.gob.mx/'
    },
    'Incidencia registrada de Infecciones de Transmisión Sexual en mujeres de 10 a 19 años': {
        'Descripción': 'Mide la cantidad de casos nuevos registrados de Infecciones de Transmisión Sexual (ITS) en niñas y adolescentes de 10 a 19 años por cada 100,000 niñas y mujeres adolescentes de 10 a 19 años.',
        'Fórmula': 'A=A',
        'Variables': 'A: Incidencia registrada de Infecciones de Transmisión Sexual en mujeres de 10 a 19 años',
        'Periodicidad': 'Anual',
        'Fuente': 'Consejo Nacional de Población (Conapo).',
        'Línea Base': '31.98 (Unidad de medida: Tasa, Año de línea base: 2018)',
        'Verificación': 'Sistema de Indicadores para Monitoreo y Seguimiento de la ENAPEA.',
        'link': ''
    },
    'Porcentaje de mujeres de 15 a 24 años con necesidad insatisfecha de métodos anticonceptivos': {
        'Descripción': 'Mide la proporción de mujeres de 15 a 24 años de edad que se encuentran sexualmente activas y manifiestan querer evitar, limitar o espaciar un embarazo, pero no utilizan un método anticonceptivo.',
        'Fórmula': 'A=A',
        'Variables': 'A: Porcentaje de mujeres de 15 a 24 años con necesidad insatisfecha de métodos anticonceptivos',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Consejo Nacional de Población (Conapo).',
        'Línea Base': '26.35 (Unidad de medida: Porcentaje, Año de línea base: 2018)',
        'Verificación': 'Sistema de Indicadores para Monitoreo y Seguimiento de la ENAPEA.',
        'link': ''
    },
    'Porcentaje de población desagregada por sexo, afiliada a servicios de salud': {
        'Descripción': 'Mide la proporción de hombres y mujeres en edad de 12 años y más que cuentan con afiliación a servicios de salud en relación al total de la población desagregada por sexo.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Porcentaje de población desagregada por sexo, afiliada a servicios de salud; B: Total de mujeres o de hombres de 12 y más años afiliadas a servicios de salud; C: Total de mujeres o de hombres de 12 y más años',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geográfica (INEGI).',
        'Línea Base': '79.65 (Unidad de medida: Porcentaje, Año de línea base: 2020)',
        'Verificación': 'Derechohabiencia, Censo de Población y Vivienda 2020, INEGI.',
        'link': 'https://www.inegi.org.mx/temas/derechohabiencia/#Tabulados 2/ Encuesta Intercensal 2015.'
    },
    'Razón de mortalidad materna por cada 100,000 nacidos vivos': {
        'Descripción': 'Se reduce a la razón de mortalidad materna de mujeres embarazadas o dentro de los 42 días siguientes a la terminación del embarazo.',
        'Fórmula': 'A=A',
        'Variables': 'A: Razón de mortalidad materna por cada 100,000 nacidos vivos',
        'Periodicidad': 'Trimestral',
        'Fuente': 'Secretaría de Salud.',
        'Línea Base': '56 (Unidad de medida: Razón, Año de línea base: 2020)',
        'Verificación': 'Informes semanales para la vigilancia epidemiológica de muertes maternas 2020.',
        'link': 'https://www.gob.mx/salud/documentos/informes-semanales-para-la-vigilancia-epidemiologica-de-muertes-maternas-2020'
    },
    'Tasa de defunción de mujeres por tumor maligno': {
        'Descripción': 'Mide la proporción de mujeres que fallecen a causa de los efectos de tumor maligno de mama y de cuello del útero.',
        'Fórmula': 'A=(B/C)*100000',
        'Variables': 'A: Tasa de defunción de mujeres por tumor maligno; B: Defunciones por tumor maligno de la mama y del cuello del útero; C: Total de mujeres de 15 años y más',
        'Periodicidad': 'Anual',
        'Fuente': '1/ Instituto Nacional de Estadística y Geográfica (INEGI). 2/ Consejo Nacional de Población (CONAPO).',
        'Línea Base': '23 (Unidad de medida: Tasa, Año de línea base: 2017)',
        'Verificación': '1/ Anuario Estadístico y Geográfico por Entidad Federativa Nueva estructura. (2018, 2019 y 2020). 2/ Población a mitad de año 1970-2050.',
        'link': ''
    },
    'Tasa de defunción de mujeres por tumor maligno de mama': {
        'Descripción': 'Mide la proporción de mujeres de 15 años y más que fallecen a causa de los efectos de tumor maligno de mama.',
        'Fórmula': 'A=(B/C)*100000',
        'Variables': 'A: Tasa de defunción de mujeres por tumor maligno de mama; B: Defunciones por tumor maligno de la mama; C: Total de mujeres de 15 años y más',
        'Periodicidad': 'Anual',
        'Fuente': '1/ Instituto Nacional de Estadística y Geográfica (INEGI). 2/ Consejo Nacional de Población (CONAPO).',
        'Línea Base': '11.26 (Unidad de medida: Tasa, Año de línea base: 2017)',
        'Verificación': '1/ Anuario Estadístico y Geográfico por Entidad Federativa Nueva estructura 2018, 2019 y 2020. 2/ Población a mitad de año 1970-2050.',
        'link': ''
    },
    'Tasa de defunción de mujeres por tumor maligno del cuello de útero': {
        'Descripción': 'Mide la proporción de mujeres de 15 y más años que fallecen a causa de los efectos de tumor maligno del cuello del útero.',
        'Fórmula': 'A=(B/C)*100,000',
        'Variables': 'A: Tasa de defunción de mujeres por tumor maligno del cuello de útero; B: Defunciones por tumor maligno del cuello del útero; C: Total de mujeres de 15 años y más',
        'Periodicidad': 'Anual',
        'Fuente': '1/ Instituto Nacional de Estadística y Geográfica (INEGI). 2/ Consejo Nacional de Población (CONAPO).',
        'Línea Base': '11.74 (Unidad de medida: Tasa, Año de línea base: 2017)',
        'Verificación': '1/ Anuario Estadístico y Geográfico por Entidad Federativa Nueva estructura 2018, 2019 y 2020. 2/ Población a mitad de año 1970-2050.',
        'link': ''
    },
    'Tasa Específica de Fecundidad en mujeres adolescentes de 15 a 19 años de edad': {
        'Descripción': 'Mide la cantidad de nacidos vivos en mujeres adolescentes de 15 a 19 años de edad que ocurren en un año por cada 1000 mujeres adolescentes de 15 a 19 años de edad a mitad de ese mismo año.',
        'Fórmula': 'A= (B/C)*1000',
        'Variables': 'A: Tasa Específica de Fecundidad en mujeres adolescentes de 15 a 19 años de edad; B: Total de nacimientos en adolescentes entre 15 y 19 años en el periodo t; C: Total de adolescentes entre 15 y 19 años en periodo t',
        'Periodicidad': 'Anual',
        'Fuente': '1/ Secretaría de Salud. Dirección General de Información en Salud. 2/ Consejo Nacional de Población (Conapo).',
        'Línea Base': '58.93 (Unidad de medida: Tasa, Año de línea base: 2018)',
        'Verificación': 'Estimación propia con base en: 1/ Secretaría de Salud. Dirección General de Información en Salud con base en la información oficial del Subsistema de Información sobre Nacimientos (SINAC). Nacimientos registrados por Entidad de residencia habitual según grupos de edad de la madre al nacimiento. 2/ Consejo Nacional de Población (Conapo). Proyecciones de la Población a mitad de año para las entidades federativas el periodo es de 1970-2050. Dirección General de Estudios Sociodemográficos y Prospectiva.',
        'link': ''
    },
    'Tasa Específica de Fecundidad en niñas de 10 a 14 años de edad': {
        'Descripción': 'Mide la cantidad de nacidos vivos en niñas de 10 a 14 años de edad que ocurren en un año por cada 1000 niñas de 10 a 14 años de edad a mitad de ese mismo año.',
        'Fórmula': 'A= (B/C)*1000',
        'Variables': 'A: Tasa Específica de Fecundidad en niñas de 10 a 14 años de edad; B: Total de nacimientos en niñas entre 10 y 14 años en el periodo t; C: Total de niñas entre 10 y 14 años en periodo t',
        'Periodicidad': 'Anual',
        'Fuente': '1/ Secretaría de Salud. Dirección General de Información en Salud. 2/ Consejo Nacional de Población (Conapo).',
        'Línea Base': '1.92 (Unidad de medida: Tasa, Año de línea base: 2018)',
        'Verificación': 'Estimación propia con base en: 1/ Secretaría de Salud. Dirección General de Información en Salud con base en la información oficial del Subsistema de Información sobre Nacimientos (SINAC). Nacimientos registrados por Entidad de residencia habitual según grupos de edad de la madre al nacimiento. 2/ Consejo Nacional de Población (Conapo). Proyecciones de la Población a mitad de año para las entidades federativas el periodo es de 1970-2050. Dirección General de Estudios Sociodemográficos y Prospectiva.',
        'link': ''
    },
    'Cifra negra de incidencia delictiva ocurrida en mujeres': {
        'Descripción': 'Mide la proporción de delitos en los que la víctima fue una mujer y no fueron denunciados por ésta ante las instancias de seguridad pública correspondientes, o bien, se reporta que la denuncia fue realizada pero no existe una carpeta de investigación o averiguación propia.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Cifra negra de incidencia delictiva ocurrida en mujeres; B: Total de delitos contra mujeres no denunciados; C: Total de delitos ocurridos contra mujeres',
        'Periodicidad': 'Anual',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '92.9 (Unidad de medida: Porcentaje, Año de línea base: 2020)',
        'Verificación': 'Encuesta Nacional de Victimización y Percepción sobre Seguridad Pública (ENVIPE). Información de Interés Nacional.',
        'link': ''
    },
    'Porcentaje de mujeres que vivieron violencia en los últimos 12 meses': {
        'Descripción': 'Mide la proporción de mujeres de 15 y más años que han vivido violencia por parte de su pareja y otros agresores en los últimos 12 meses previos a la entrevista.',
        'Fórmula': 'A=A',
        'Variables': 'A: Porcentaje de mujeres que vivieron violencia en los últimos 12 meses',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '45.2 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Porcentaje de municipios que cuentan con una instancia o centro para la atención a las violencias contra las mujeres': {
        'Descripción': 'Mide la proporción de municipios que cuentan con una instancia o centro para la atención a las violencias contra las mujeres.',
        'Fórmula': 'A=(B/C)*100',
        'Variables': 'A: Porcentaje de municipios que cuentan con una instancia o centro para la atención a las violencias contra las mujeres; B: Total de municipios que cuentan con una instancia o centro para la atención a las violencias contra las mujeres; C: Total de municipios del estado de Yucatán',
        'Periodicidad': 'Anual',
        'Fuente': 'Instituto Nacional de Desarrollo Social (Indesol).',
        'Línea Base': '11.32 (Unidad de medida: Porcentaje, Año de línea base: 2020)',
        'Verificación': 'Servicios de Atención a Mujeres, Niñas, Niños y Adolescentes en situaciones de violencia.',
        'link': ''
    },
    'Prevalencia de las violencias hacia las mujeres': {
        'Descripción': 'Mide el porcentaje de mujeres de 15 y más años que han vivido algún tipo de violencia a lo largo de su vida.',
        'Fórmula': 'A=A',
        'Variables': 'A: Prevalencia de las violencias hacia las mujeres',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '66.8 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Prevalencia de violencia económica o patrimonial hacia las mujeres': {
        'Descripción': 'Mide el porcentaje de mujeres de 15 y más años que han vivido violencia económica a lo largo de su vida.',
        'Fórmula': 'A=A',
        'Variables': 'A: Prevalencia de violencia económica o patrimonial hacia las mujeres',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '29.81 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Prevalencia de violencia emocional hacia las mujeres': {
        'Descripción': 'Mide el porcentaje de mujeres de 15 y más años que han vivido violencia emocional a lo largo de su vida.',
        'Fórmula': 'A=A',
        'Variables': 'A: Prevalencia de violencia emocional hacia las mujeres',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '48.82 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Prevalencia de violencia física hacia las mujeres': {
        'Descripción': 'Mide el porcentaje de mujeres de 15 y más años que han vivido violencia física a lo largo de su vida.',
        'Fórmula': 'A=A',
        'Variables': 'A: Prevalencia de violencia física hacia las mujeres',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '30.05 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Prevalencia de violencia sexual hacia las mujeres': {
        'Descripción': 'Mide el porcentaje de mujeres de 15 y más años que han vivido violencia sexual a lo largo de su vida.',
        'Fórmula': 'A=A',
        'Variables': 'A: Prevalencia de violencia sexual hacia las mujeres',
        'Periodicidad': 'Quinquenal',
        'Fuente': 'Instituto Nacional de Estadística y Geografía (INEGI).',
        'Línea Base': '41.4 (Unidad de medida: Porcentaje, Año de línea base: 2016)',
        'Verificación': 'Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH).',
        'link': ''
    },
    'Tasa de feminicidios por cada 100 mil mujeres': {
        'Descripción': 'Mide la proporción de presuntos casos de feminicidio por cada 100 mil mujeres.',
        'Fórmula': 'A=(B/C)*100000',
        'Variables': 'A: Tasa de feminicidios por cada 100 mil mujeres; B: Número de presuntos feminicidios (carpetas de investigación abiertas); C: Proyección de mujeres a mitad de año',
        'Periodicidad': 'Mensual',
        'Fuente': 'Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública.',
        'Línea Base': '0.52 (Unidad de medida: Tasa, Año de línea base: 2020)',
        'Verificación': 'Informe mensual sobre violencia contra las mujeres (incidencia delictiva y llamadas al 911) emitido por el Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública.',
        'link': ''
    },
    'Tasa de homicidios dolosos de mujeres por cada 100 mil mujeres': {
        'Descripción': 'Mide la proporción de muertes clasificadas como presuntos homicidios dolosos por cada cien mil mujeres.',
        'Fórmula': 'A=(B/C)*100000',
        'Variables': 'A: Tasa de homicidios dolosos de mujeres por cada 100 mil mujeres; B: Número de presuntos homicidios dolosos de mujeres (carpetas de investigación abiertas); C: Proyección de mujeres a mitad de año',
        'Periodicidad': 'Mensual',
        'Fuente': 'Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública.',
        'Línea Base': '0.44 (Unidad de medida: Tasa, Año de línea base: 2020)',
        'Verificación': 'Informe mensual sobre violencia contra las mujeres (incidencia delictiva y llamadas al 911) emitido por el Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública.',
        'link': ''
    }
}
