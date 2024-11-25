import random
import string
import streamlit as st

# Función para generar la contraseña aleatoria
def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales, incluir_letras_min, incluir_espacios, incluir_guiones):
    caracteres = ""
    
    # Siempre incluimos letras minúsculas
    caracteres += string.ascii_lowercase if incluir_letras_min else ''
    
    # Añadimos mayúsculas si es necesario
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    
    # Añadimos números si es necesario
    if incluir_numeros:
        caracteres += string.digits
    
    # Añadimos caracteres especiales si es necesario
    if incluir_especiales:
        caracteres += string.punctuation
    
    # Opciones adicionales de caracteres
    if incluir_espacios:
        caracteres += " "
    
    if incluir_guiones:
        caracteres += "-_"
    
    # Validación de que haya al menos una opción seleccionada
    if not caracteres:
        st.error("Debe seleccionar al menos una opción para generar una contraseña.")
        return ""
    
    # Generamos la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función principal de la app
def main():
    st.title("Generador de Contraseñas Seguras 🔒")
    
    st.write("""
    **Genera una contraseña segura** para tu cuenta. Elige las opciones que desees para crear una contraseña con los requisitos de seguridad que prefieras.
    """)

    # Ingreso manual de la longitud de la contraseña
    longitud = st.number_input("Longitud de la contraseña:", min_value=8, max_value=16, value=12)
    
    # Opciones de inclusión
    incluir_mayusculas = st.checkbox("Incluir letras mayúsculas")
    incluir_numeros = st.checkbox("Incluir números")
    incluir_especiales = st.checkbox("Incluir caracteres especiales (!@#$%^&*)")
    incluir_letras_min = st.checkbox("Incluir letras minúsculas", value=True)
    
    # Opciones adicionales
    incluir_espacios = st.checkbox("Incluir espacios")
    incluir_guiones = st.checkbox("Incluir guiones (-_)")
    
    # Generar contraseña al hacer clic en el botón
    if st.button("Generar Contraseña Segura"):
        contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales, incluir_letras_min, incluir_espacios, incluir_guiones)
        if contraseña:
            st.subheader("Tu contraseña segura es:")
            st.write(contraseña)
            st.write("**¡Copia y guarda tu contraseña!** Asegúrate de que sea segura y no la compartas.")
        
    st.write("""
    **Consejo:** Usa contraseñas largas (más de 12 caracteres) y asegúrate de incluir una mezcla de letras mayúsculas, minúsculas, números y caracteres especiales para mayor seguridad.
    """)

    st.write("""
    **Programado por**: Miguel Angel Villarraga Franco
    """)

if __name__ == "__main__":
    main()
