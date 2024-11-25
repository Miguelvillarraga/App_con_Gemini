import streamlit as st
import re

# Función para validar el nombre
def validar_nombre(nombre):
    patron = r'^[A-Z][a-zA-Z]+$'  # Inicia con mayúscula y solo caracteres alfabéticos
    if re.match(patron, nombre):
        return True
    return False

# Función para validar el correo electrónico
def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Formato de correo electrónico
    if re.match(patron, email):
        return True
    return False

# Función para validar el número de teléfono
def validar_telefono(telefono):
    patron = r'^\d{10}$'  # 10 dígitos, puedes ajustarlo si es necesario
    if re.match(patron, telefono):
        return True
    return False

# Función para validar la fecha
def validar_fecha(fecha):
    patron = r'^\d{2}/\d{2}/\d{4}$'  # Formato de fecha DD/MM/YYYY
    if re.match(patron, fecha):
        return True
    return False

# Función para manejar la validación
def validar_datos(nombre, email, telefono, fecha):
    validacion_nombre = validar_nombre(nombre)
    validacion_email = validar_email(email)
    validacion_telefono = validar_telefono(telefono)
    validacion_fecha = validar_fecha(fecha)
    
    return validacion_nombre, validacion_email, validacion_telefono, validacion_fecha

# Interfaz de usuario con Streamlit
def main():
    st.title('Formulario de Validación de Datos')
    
    # Ingresar datos
    nombre = st.text_input('Ingrese su nombre:')
    email = st.text_input('Ingrese su correo electrónico:')
    telefono = st.text_input('Ingrese su número de teléfono (10 dígitos):')
    fecha = st.text_input('Ingrese la fecha (DD/MM/YYYY):')
    
    if st.button('Validar'):
        validacion_nombre, validacion_email, validacion_telefono, validacion_fecha = validar_datos(nombre, email, telefono, fecha)
        
        # Resultados de la validación
        if validacion_nombre:
            st.markdown("✔️ **Nombre válido**")
        else:
            st.markdown("❌ **Nombre inválido**. Asegúrese de que el nombre comience con mayúscula y contenga solo caracteres alfabéticos.")
        
        if validacion_email:
            st.markdown("✔️ **Correo electrónico válido**")
        else:
            st.markdown("❌ **Correo electrónico inválido**. Asegúrese de que el formato sea 'usuario@dominio.com'.")
        
        if validacion_telefono:
            st.markdown("✔️ **Número de teléfono válido**")
        else:
            st.markdown("❌ **Número de teléfono inválido**. Asegúrese de que tenga 10 dígitos.")
        
        if validacion_fecha:
            st.markdown("✔️ **Fecha válida**")
        else:
            st.markdown("❌ **Fecha inválida**. Asegúrese de que el formato sea 'DD/MM/YYYY'.")
    
    # Información adicional
    st.markdown("---")
    st.write("Programado por Miguel Angel Villarraga Franco")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
