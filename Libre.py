import streamlit as st
import re
import pandas as pd
from io import BytesIO

# Expresiones regulares
PATRONES = {
    "RFC": r"\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b",
    "UUID": r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
    "Fecha": r"\b\d{4}-\d{2}-\d{2}\b",
    "Monto": r"\b\d+\.\d{2}\b"
}

# Función para analizar texto
def analizar_facturas(texto):
    resultados = {campo: re.findall(patron, texto) for campo, patron in PATRONES.items()}
    return resultados

# Función para generar un archivo Excel
def generar_excel(resultados):
    dataframes = []
    for campo, valores in resultados.items():
        df = pd.DataFrame({campo: valores})
        dataframes.append(df)

    resultado_df = pd.concat(dataframes, axis=1)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        resultado_df.to_excel(writer, index=False, sheet_name="Facturas")
    output.seek(0)
    return output

# App principal
def main():
    st.title("💳 Validador y Extractor de Facturas Electrónicas")
    st.write("""
    Suba un archivo de texto o escriba/pegue información de facturas electrónicas.
    La aplicación extraerá y validará RFCs, UUIDs, fechas y montos.
    """)

    # Entrada del usuario
    texto_usuario = st.text_area(
        "Escribe o pega el contenido del archivo aquí:",
        placeholder="Ejemplo: RFC: ABCD910101XXX, UUID: a1b2c3d4-1234-5678-9abc-def123456789, Monto: 1200.50, Fecha: 2023-11-23"
    )

    archivo_cargado = st.file_uploader("O carga un archivo de texto:", type=["txt"])

    texto = ""
    if archivo_cargado:
        texto = archivo_cargado.read().decode("utf-8")
    elif texto_usuario.strip():
        texto = texto_usuario

    # Procesar el texto
    if texto:
        resultados = analizar_facturas(texto)

        # Mostrar resultados
        st.subheader("📋 Resultados de la validación:")
        for campo, valores in resultados.items():
            if valores:
                st.write(f"**{campo}s encontrados:** {', '.join(valores)}")
            else:
                st.write(f"**{campo}s encontrados:** Ninguno")

        # Generar Excel
        if st.button("Descargar resultados en Excel"):
            archivo_excel = generar_excel(resultados)
            st.download_button(
                label="Descargar archivo Excel",
                data=archivo_excel,
                file_name="resultados_facturas.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Por favor, ingresa texto o carga un archivo para analizar.")

    st.markdown("---")
    st.write("Programado por Miguel Angel Villarraga Franco")

if __name__ == "__main__":
    main()
