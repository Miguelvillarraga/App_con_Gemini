import random
import string
import streamlit as st

# Función para generar una contraseña aleatoria
def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales):
    caracteres = string.ascii_lowercase  # Incluye letras minúsculas
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Incluye letras mayúsculas
    if incluir_numeros:
        caracteres += string.digits  # Incluye números
    if incluir_especiales:
        caracteres += string.punctuation  # Incluye caracteres especiales
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función principal de la app
def main():
    st.title("Generador de Contraseñas Seguras 🔒")
    
    st.write("""
    **Genera una contraseña segura** para tu cuenta. Elige las opciones que desees para crear una contraseña con los requisitos de seguridad que prefieras.
    """)
    
    # Definir la longitud mínima
    longitud = st.slider("Longitud de la contraseña:", min_value=8, max_value=20, value=12)
    
    # Opciones de inclusión
    incluir_mayusculas = st.checkbox("Incluir letras mayúsculas")
    incluir_numeros = st.checkbox("Incluir números")
    incluir_especiales = st.checkbox("Incluir caracteres especiales (!@#$%^&*)")
    
    # Generar contraseña al hacer clic en el botón
    if st.button("Generar Contraseña Segura"):
        contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales)
        st.subheader("Tu contraseña segura es:")
        st.write(contraseña)
        st.write("**¡Copia y guarda tu contraseña!** Asegúrate de que sea segura y no la compartas.")
        
    st.write("""
    **Consejo:** Usa contraseñas largas (más de 12 caracteres) y asegúrate de incluir una mezcla de letras mayúsculas, minúsculas, números y caracteres especiales para mayor seguridad.
    """)

if __name__ == "__main__":
    main()
