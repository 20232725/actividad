# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Reducción de Dimensionalidad", layout="wide")
st.title("📊 Reducción de Dimensionalidad para Clasificación")

# 1. Se añaden extensiones .xlsx y .xls al uploader
uploaded_file = st.sidebar.file_uploader(
    "Sube tu archivo (CSV o Excel)", 
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:
    # 2. Lectura dinámica según el formato del archivo subido
    file_name = uploaded_file.name
    if file_name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Vista previa de los datos originales")
    st.dataframe(df.head())

    all_columns = df.columns.tolist()
    target_col = st.sidebar.selectbox("Selecciona la variable Objetivo (Target):", all_columns)

    X = df.drop(columns=[target_col])
    y = df[target_col].reset_index(drop=True)
    
    # Seleccionar solo variables numéricas
    X_numeric = X.select_dtypes(include=[np.number]).copy()

    if X_numeric.empty:
        st.error("El dataset no contiene características numéricas para reducir.")
    else:
        # Imputación básica de nulos
        if X_numeric.isnull().sum().sum() > 0:
            X_numeric = X_numeric.fillna(X_numeric.mean())

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_numeric)

        method = st.sidebar.selectbox(
            "Método de reducción:",
            ["PCA (Principal Component Analysis)", "LDA (Linear Discriminant Analysis)", "SelectKBest (ANOVA F-value)"]
        )

        n_features_max = X_numeric.shape[1]
        n_classes = len(np.unique(y))
        
        # Límite máximo de componentes según el método
        if "LDA" in method:
            max_components = max(1, min(n_features_max, n_classes - 1))
        else:
            max_components = n_features_max

        n_components = st.sidebar.slider(
            "Número de dimensiones/características:", 
            1, 
            max_components, 
            min(2, max_components)
        )

        df_transformed = pd.DataFrame()

        if "PCA" in method:
            pca = PCA(n_components=n_components)
            X_res = pca.fit_transform(X_scaled)
            df_transformed = pd.DataFrame(X_res, columns=[f"PC_{i+1}" for i in range(n_components)])
            st.info(f"Varianza explicada retenida: {np.sum(pca.explained_variance_ratio_)*100:.2f}%")

        elif "LDA" in method:
            lda = LDA(n_components=n_components)
            X_res = lda.fit_transform(X_scaled, y)
            df_transformed = pd.DataFrame(X_res, columns=[f"LD_{i+1}" for i in range(n_components)])

        elif "SelectKBest" in method:
            selector = SelectKBest(score_func=f_classif, k=n_components)
            X_res = selector.fit_transform(X_scaled, y)
            selected_cols = X_numeric.columns[selector.get_support()].tolist()
            df_transformed = pd.DataFrame(X_res, columns=selected_cols)

        df_final = df_transformed.copy()
        df_final[target_col] = y

        st.subheader("Resultado de la Reducción")
        st.dataframe(df_final.head())

        csv_data = df_final.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Descargar Dataset Reducido (CSV)", 
            csv_data, 
            f"dataset_{method.split()[0].lower()}.csv", 
            "text/csv"
        )