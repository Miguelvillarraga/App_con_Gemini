import pandas as pd
import re
import streamlit as st
from datetime import datetime
from io import BytesIO

# Validaciones con expresiones regulares
def validar_email(email):
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron_email, email))

def validar_telefono(telefono):
    patron_telefono = r'^\+57 \d{9}$'
    return bool(re.match(patron_telefono, telefono))

def validar_fecha(fecha):
    patron_fecha = r'^\d{2}/\d{2}/\d{2}$'
    return bool(re.match(patron_fecha, fecha))

def validar_valor(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def procesar_archivo(csv_file):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(csv_file, header=None)
        st.write("Datos cargados correctamente:")
        st.write(df.head())

        # Convertir el DataFrame a una lista de texto para procesar línea por línea
        lineas = df.astype(str).apply(lambda x: ','.join(x), axis=1).tolist()

        # Listas para almacenar los resultados
        datos_validos = []

        # Procesar cada línea
        for linea in lineas:
            # Buscar los campos en la línea con regex
            email = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', linea)
            telefono = re.search(r'\+57 \d{9}', linea)
            fecha = re.search(r'\d{2}/\d{2}/\d{2}', linea)
            valor = re.search(r'\b\d+(\.\d+)?\b', linea)
            nombre = re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b', linea)

            # Verificar que haya al menos dos nombres en la fila
            if email and telefono and fecha and valor and len(nombre) >= 2:
                datos_validos.append({
                    'Correo electrónico': email.group(),
                    'Nombre cliente': ' '.join(nombre),  # Unir los nombres si hay más de uno
                    'Teléfono': telefono.group(),
                    'Fecha de compra': fecha.group(),
                    'Valor': valor.group()
                })

        return datos_validos

    except Exception as e:
        st.error(f"Error procesando el archivo: {e}")
        return []

def generar_excel(datos_validos):
    df = pd.DataFrame(datos_validos)
    output = BytesIO()
    # Usar openpyxl como motor para generar el archivo Excel
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Productos')
    output.seek(0)
    return output

def main():
    st.title('Validador y Exportador de Productos y Contactos')
    st.write('Sube un archivo CSV con datos para validarlos y exportarlos.')

    csv_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    if csv_file:
        datos_validos = procesar_archivo(csv_file)
        
        if datos_validos:
            st.write("Datos válidos procesados:")
            st.write(pd.DataFrame(datos_validos))
            
            excel_file = generar_excel(datos_validos)
            st.download_button(
                label="Descargar archivo Excel",
                data=excel_file,
                file_name="productos_clientes_validos.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("No se encontraron datos válidos en el archivo.")

    st.markdown("---")
    st.write("Programado por Miguel Angel Villarraga Franco")

if __name__ == "__main__":
    main()
