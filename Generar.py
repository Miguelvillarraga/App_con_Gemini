import pandas as pd
import re
import streamlit as st
from datetime import datetime
from io import BytesIO

# Función para validar correo electrónico
def validar_email(email):
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron_email, email))

# Función para validar teléfono (formato +57 y 10 dígitos)
def validar_telefono(telefono):
    patron_telefono = r'^\+57 \d{9}$'
    return bool(re.match(patron_telefono, telefono))

# Función para validar fecha en formato DD/MM/YY
def validar_fecha(fecha):
    patron_fecha = r'^\d{2}/\d{2}/\d{2}$'
    return bool(re.match(patron_fecha, fecha))

# Función para validar valores (números)
def validar_valor(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Función para procesar el archivo CSV
def procesar_archivo(csv_file):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file, header=None)
    
    # Definir los nombres de las columnas
    columnas = ['Correo electrónico', 'Fecha de compra', 'Número de serie', 'Teléfono', 'Nombre cliente', 'Otro dato', 'Valor']
    df.columns = columnas

    # Procesar cada fila
    valid_rows = []
    for index, row in df.iterrows():
        email = str(row['Correo electrónico'])
        fecha = str(row['Fecha de compra'])
        telefono = str(row['Teléfono'])
        valor = str(row['Valor'])
        nombre_cliente = str(row['Nombre cliente'])

        # Validar cada campo
        if (validar_email(email) and
            validar_telefono(telefono) and
            validar_fecha(fecha) and
            validar_valor(valor)):

            # Convertir la fecha al formato correcto (DD/MM/YY)
            fecha_formateada = datetime.strptime(fecha, '%d/%m/%y').strftime('%d/%m/%y')
            
            valid_rows.append({
                'Correo electrónico': email,
                'Nombre cliente': nombre_cliente,
                'Teléfono': telefono,
                'Fecha de compra': fecha_formateada,
                'Valor': valor
            })
    
    return valid_rows

# Función para generar un archivo Excel
def generar_excel(datos_validos):
    df = pd.DataFrame(datos_validos)
    # Guardar el archivo Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Productos')
    output.seek(0)
    return output

# Interfaz de usuario con Streamlit
def main():
    st.title('Procesador de Productos y Contactos')
    st.write('Sube el archivo CSV que contiene los productos y la información de los clientes.')

    # Subir archivo CSV
    csv_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    
    if csv_file:
        # Procesar el archivo CSV
        datos_validos = procesar_archivo(csv_file)
        
        if datos_validos:
            st.write("Los datos han sido procesados y validados correctamente.")
            
            # Mostrar los datos procesados
            st.write(pd.DataFrame(datos_validos))
            
            # Generar archivo Excel
            excel_file = generar_excel(datos_validos)
            
            # Descargar el archivo Excel
            st.download_button(
                label="Descargar archivo Excel",
                data=excel_file,
                file_name="productos_clientes.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.write("No se encontraron datos válidos en el archivo.")

    # Información adicional
    st.markdown("---")
    st.write("Programado por Miguel Angel Villarraga Franco")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
