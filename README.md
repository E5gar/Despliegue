
# 🌟 Despliegue de Modelos de Machine Learning para Clasificación de Patologías Relacionadas con la Hipertensión

Este proyecto tiene como objetivo desarrollar y evaluar modelos de aprendizaje supervisado que permitan clasificar patologías relacionadas con la hipertensión en pacientes de **EsSalud**. Se emplean técnicas avanzadas de Machine Learning para maximizar la precisión y el rendimiento de las predicciones.

---

## 📋 **Descripción del Proyecto**

La investigación se centra en entrenar, ajustar y comparar modelos de Machine Learning que clasifiquen diagnósticos médicos relacionados con la hipertensión. Los modelos filtrados utilizados incluyen:

- **Decision Tree**
- **Random Forest**
- **Extra Trees**

Estos modelos se evaluaron utilizando métricas estándar como *Precision*, *Recall*, *F1-Score* y *AUC-ROC*. Además, se utilizó la técnica de búsqueda de hiperparámetros (*GridSearchCV*) para optimizar el rendimiento.

---

## ⚙️ **Hiperparámetros Optimizados**

### 🔹 **Decision Tree**

| Hiperparámetro          | Valor       |
|-------------------------|-------------|
| **Criterion**           | `entropy`   |
| **min_samples_split**   |    `2`      |
| **max_features**        |   `sqrt`    |

### 🔹 **Random Forest**

| Hiperparámetro          | Valor       |
|-------------------------|-------------|
| **Criterion**           | `gini`      |
| **min_samples_split**   | `3`         |
| **max_features**        | `sqrt`      |
| **n_estimators**        | `200`       |

### 🔹 **Extra Trees**

| Hiperparámetro          | Valor       |
|-------------------------|-------------|
| **Criterion**           | `entropy`   |
| **max_features**        | `sqrt`      |
| **n_estimators**        | `500`       |

---

## 📊 **Resultados Principales**

1. **Random Forest**:  
   - **Accuracy**: `0.807031`  
   - **Profundidad promedio por árbol**: `39.77`  
   - **Nodos promedio por árbol**: `35456.22`

2. **Extra Trees**:  
   - **Accuracy**: `0.807564`  
   - **Profundidad promedio por árbol**: `40.74`  
   - **Nodos promedio por árbol**: `81595.42`

### Métricas de Evaluación Comparativa

| Modelo          | Precision (Promedio) | Recall (Promedio) | F1-Score (Promedio) |
|------------------|-----------------------|--------------------|---------------------|
| **Decision Tree** | `0.79`               | `0.81`            | `0.80`             |
| **Random Forest** | `0.82`               | `0.84`            | `0.83`             |
| **Extra Trees**   | `0.83`               | `0.85`            | `0.84`             |

---

## 📖 **Conclusiones**

1. **Random Forest** y **Extra Trees** mostraron el mejor desempeño general.
2. La optimización de hiperparámetros mejoró significativamente la precisión de los modelos.
3. Las métricas obtenidas demuestran que los modelos son confiables para clasificar patologías relacionadas con la hipertensión.

---


## 🚀 **Despliegue en Streamlite.Io**

Accede a través del enlace: [Clasificación de Patologías de Hipertensión](https://clasificacion-patologias-de-hipertension.streamlit.app)  
Paper: [Enlace al Paper](https://drive.google.com/file/d/14Fo91J1vmBWxGb6KnGUJ0-qJbmtrjhL0/view?usp=sharing)

### Visualización en PC
<img src="https://github.com/user-attachments/assets/4cc35dd6-c4a6-469d-a385-2adb1dd67167" alt="Despliegue en PC #01" width="900">
<img src="https://github.com/user-attachments/assets/506340ff-0e7e-46b7-9252-e8c498a32851" alt="Despliegue en PC #02" width="900">


### Visualización en Móvil
<img src="https://github.com/user-attachments/assets/4f51f600-b3e5-4994-a5e5-5b6daf51b2c7" alt ="Despliegue en Móvil #01" width = "230">
<img src="https://github.com/user-attachments/assets/58b041c0-f1e7-4af5-abfb-5f15e33ff4c9" alt ="Despliegue en Móvil #02" width = "230">
<img src="https://github.com/user-attachments/assets/b5a64cee-f82e-4bc6-8d58-67df20d4516c" alt ="Despliegue en Móvil #03" width = "230">

---
