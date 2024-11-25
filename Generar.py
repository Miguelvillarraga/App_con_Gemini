import pandas as pd
import re
from openpyxl import Workbook
from io import BytesIO

# Función para validar los datos usando regex
def validar_datos(row):
    # Validar correo electrónico
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, row['Correo electrónico']):
        return False
    
    # Validar teléfono (formato +57 y número)
    telefono_regex = r'^\+57 \d{10}$'
    if not re.match(telefono_regex, row['Teléfono']):
        return False
    
    # Validar fecha en formato DD/MM/YY
    fecha_regex = r'^\d{2}/\d{2}/\d{2}$'
    if not re.match(fecha_regex, row['Fecha de compra']):
        return False
    
    return True

# Función para generar el archivo Excel
def generar_excel(datos_validos):
    # Convertir los datos válidos a un DataFrame de pandas
    df = pd.DataFrame(datos_validos)

    # Crear un archivo Excel en memoria
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Productos')

    # Guardar el archivo Excel
    output.seek(0)
    return output

# Función principal de la aplicación
def procesar_archivo_csv():
    # Leer el archivo CSV (el archivo debe estar en el mismo directorio o proporcionar la ruta completa)
    archivo_csv = 'regex_productos.csv'
    df = pd.read_csv(archivo_csv)

    # Filtrar los datos válidos
    datos_validos = []
    for _, row in df.iterrows():
        if validar_datos(row):
            datos_validos.append({
                'Número de serie del producto': row['Número de serie del producto'],
                'Nombre del producto': row['Nombre del producto'],
                'Valor': row['Valor'],
                'Fecha de compra': row['Fecha de compra'],
                'Correo electrónico': row['Correo electrónico'],
                'Teléfono': row['Teléfono']
            })
    
    # Si hay datos válidos, generar el archivo Excel
    if datos_validos:
        excel_file = generar_excel(datos_validos)
        with open('productos_validos.xlsx', 'wb') as f:
            f.write(excel_file.read())
        print("Archivo Excel generado exitosamente: productos_validos.xlsx")
    else:
        print("No se encontraron datos válidos en el archivo CSV.")

# Ejecutar el procesamiento
if __name__ == '__main__':
    procesar_archivo_csv()
