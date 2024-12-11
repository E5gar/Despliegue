import streamlit as st
import joblib
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Modelos de Machine Learning",
    page_icon=":medical_symbol:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Colores degradados
st.markdown("""
    <style>
    .reportview-container .sidebar-content {
        padding-top: 0rem;
    }
    .reportview-container .main .block-container {
        padding-top: 0rem;
    }
    header {
        visibility: hidden;
    }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(
            -45deg, 
            #FFDEE9, 
            #B5FFFC, 
            #FFF1BA,
            #FFFFFF,  
            #C4FFDC, 
            #FFDEE9
        );
        background-size: 400% 400%;
        animation: gradientBG 30s ease infinite;
    }

    @keyframes gradientBG {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
# Título de la aplicación
st.title("Clasificación de patologías relacionadas a la Hipertensión")

# Cargando modelos
ruta_modelo_DT = "Modelos/modelo_DT.pkl"
modelo_DT = joblib.load(ruta_modelo_DT)
# ruta_modelo_RF = "Modelos/modelo_RF.pkl"
# modelo_RF = joblib.load(ruta_modelo_RF)
# ruta_modelo_EX = "Modelos/modelo_EX.pkl"
# modelo_EX = joblib.load(ruta_modelo_EX)

# Cargando Label Encoders
label_encoders = {}
ruta_base = "LabelEncoders/"
columnas_categoricas = [
    'DEPARTAMENTO',
    'PROVINCIA',
    'DISTRITO',
    'RED',
    'IPRESS',
    'SEXO_PACIENTE',
    'COD_DIAG',
    'DIAGNOSTICO',
    'AREA_HOSPITALARIA',
    'SERVICIO_HOSPITALARIO',
    'ACTIVIDAD_HOSPITALARIA',
    'PROCEDIMIENTO_1',
    'UNIDADES_1',
    'PROCEDIMIENTO_2',
    'UNIDADES_2'
]
for columna in columnas_categoricas:
    ruta_encoder = f'{ruta_base}/{columna}_label_encoder.pkl'
    label_encoders[columna] = joblib.load(ruta_encoder)

# Diccionario de mapeo para los diagnósticos
mapeo_diagnosticos = {
    0: "HIPERTENSION ESENCIAL (PRIMARIA)",
    2: "ENFERMEDAD CARDIACA HIPERTENSIVA SIN INSUFICIENCIA CARDIACA (CONGESTIVA)",
    6: "HIPERTENSION SECUNDARIA A OTROS TRASTORNOS RENALES",
    1: "ENFERMEDAD CARDIACA HIPERTENSIVA CON INSUFICIENCIA CARDIACA (CONGESTIVA)",
    9: "HIPERTENSION SECUNDARIA, NO ESPECIFICADA",
}

# Cargando escalador
sc = joblib.load("Escalador/scaler.pkl")

# Función para predecir
def predecir_paciente(paciente, modelos):
    resultados = {}
    paciente_codificado = paciente.copy()
    paciente_codificado['DEPARTAMENTO'] = label_encoders['DEPARTAMENTO'].transform(
        [paciente['DEPARTAMENTO']])[0]

    # Crear DataFrame y normalizar
    paciente_df = pd.DataFrame([paciente_codificado])
    paciente_normalizado = sc.transform(paciente_df)

    # Predecir para cada modelo
    for nombre_modelo, modelo in modelos.items():
        prediccion_clase = modelo.predict(paciente_normalizado)[0]
        probabilidades_clases = modelo.predict_proba(paciente_normalizado)[0]

        # Decodificar clase predicha
        clase_predicha = label_encoders['COD_DIAG'].inverse_transform([prediccion_clase])[
            0]
        diagnostico_paciente = mapeo_diagnosticos.get(
            prediccion_clase, "Diagnóstico no encontrado")

        resultados[nombre_modelo] = {
            'codigo_diagnostico': clase_predicha,
            'diagnostico': diagnostico_paciente,
            'probabilidades': probabilidades_clases
        }

    return resultados


# Interfaz de Streamlit
with st.sidebar:
    st.header("🩺 Información del Paciente")

    # Formulario en la barra lateral
    with st.form("patient_form"):
        edad = st.number_input(
            "Edad del Paciente", min_value=0, max_value=120, value=30)
        creatinina = st.number_input(
            "Resultado de Creatinina (mg/dL)", min_value=0.0, value=1.0, step=0.01)
        trigliceridos = st.number_input(
            "Resultado de Triglicéridos (mg/dL)", min_value=0.0, value=100.0, step=0.1)
        departamento = st.selectbox(
            "Departamento", label_encoders['DEPARTAMENTO'].classes_)

        # Botón de submit dentro del form
        submitted = st.form_submit_button("🚀 Predecir")

# Procesar el formulario si se ha enviado
if submitted:
    # Datos del paciente ingresados
    paciente = {
        'RESULTADO_2': trigliceridos,
        'RESULTADO_1': creatinina,
        'DEPARTAMENTO': departamento,
        'EDAD_PACIENTE': edad,
    }
    # Realizando predicción con los modelos
    modelos = {
        '🌳 Decision Tree': modelo_DT,
        # '🌲 Random Forest': modelo_RF
        # '🌲 Extra Trees': modelo_ET
    }
    resultados = predecir_paciente(paciente, modelos)

    # Visualizando resultados
    st.subheader("📊 Resultados de la Predicción")
    st.markdown("""
        <style>
        .result-panel {
            background: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
            backdrop-filter: blur(5px);
        }
        .result-panel h3 {
            margin-bottom: 10px;
        }
        .result-panel p {
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)

    for nombre_modelo, resultado in resultados.items():
        # Panel de resultados
        st.markdown(f"""
        <div class="result-panel">
            <h3>{nombre_modelo}</h3>
            <p><strong>Código de Diagnóstico:</strong> {resultado['codigo_diagnostico']}</p>
            <p><strong>Diagnóstico:</strong> {resultado['diagnostico']}</p>
            <p><strong>Probabilidades por Clase:</strong></p>
        """, unsafe_allow_html=True)

        # Probabilidades de cada clase
        for clase, prob in zip(modelos[nombre_modelo].classes_, resultado['probabilidades']):
            clase_decodificada = label_encoders['COD_DIAG'].inverse_transform([clase])[
                0]
            st.markdown(f"""
            <p> - Clase <strong>{clase_decodificada}</strong>: {prob:.4f}</p>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
