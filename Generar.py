import pandas as pd
import re
from openpyxl import Workbook

# Función para procesar el archivo CSV y extraer la información relevante
def procesar_datos(input_file):
    # Cargar el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(input_file, header=None)
    
    # Definir las expresiones regulares para cada campo
    regex_serie = r'^\d{6,8}$'  # Número de serie del producto (6-8 dígitos)
    regex_nombre_producto = r'^[A-Za-z\s]+$'  # Nombre del producto (solo letras y espacios)
    regex_valor = r'^\d+(\.\d{1,2})?$'  # Valor del producto (números con hasta 2 decimales)
    regex_fecha = r'\d{2}/\d{2}/\d{2}'  # Fecha de compra (DD/MM/YY)
    regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Correo electrónico
    regex_telefono = r'^\+?\d{1,3}?[-. \(\)]?\(?\d{1,4}?\)?[-. \(\)]?\d{1,4}[-. \(\)]?\d{1,4}$'  # Teléfono

    # Listas para almacenar los datos válidos
    valid_data = []

    # Recorrer cada fila del DataFrame
    for index, row in df.iterrows():
        serie_valida = bool(re.match(regex_serie, str(row[0])))
        nombre_valido = bool(re.match(regex_nombre_producto, str(row[1])))
        valor_valido = bool(re.match(regex_valor, str(row[2])))
        fecha_valida = bool(re.match(regex_fecha, str(row[3])))
        email_valido = bool(re.match(regex_email, str(row[4])))
        telefono_valido = bool(re.match(regex_telefono, str(row[5])))

        # Verificar si todos los campos son válidos
        if serie_valida and nombre_valido and valor_valido and fecha_valida and email_valido and telefono_valido:
            valid_data.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    return valid_data

# Función para generar el archivo Excel
def generar_excel(valid_data, output_file):
    # Crear un DataFrame con los datos válidos
    df = pd.DataFrame(valid_data, columns=['Número de serie', 'Nombre del producto', 'Valor', 'Fecha de compra', 'Correo electrónico', 'Teléfono'])

    # Guardar los datos en un archivo Excel
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Productos')

# Función principal
def main():
    input_file = 'regex_productos.csv'  # Nombre del archivo CSV
    output_file = 'productos_validos.xlsx'  # Nombre del archivo Excel de salida
    
    # Procesar los datos
    valid_data = procesar_datos(input_file)
    
    if valid_data:
        # Generar el archivo Excel si hay datos válidos
        generar_excel(valid_data, output_file)
        print(f"Archivo generado correctamente: {output_file}")
    else:
        print("No se encontraron datos válidos.")

if __name__ == '__main__':
    main()
