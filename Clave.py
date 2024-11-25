import streamlit as st
import re

def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña y devuelve un mensaje.

    Args:
        contrasena (str): La contraseña a evaluar.

    Returns:
        str: Un mensaje indicando si la contraseña es fuerte o débil, y sugerencias.
    """

    # Expresiones regulares para cada criterio
    longitud = re.compile(r".{8,}")
    mayuscula = re.compile(r"[A-Z]")
    minuscula = re.compile(r"[a-z]")
    numero = re.compile(r"\d")
    especial = re.compile(r"[^\w\s]")

    # Inicializar variables
    fuerte = True
    sugerencias = []

    # Evaluar cada criterio
    if not longitud.search(contrasena):
        fuerte = False
        sugerencias.append("Debe tener al menos 8 caracteres.")
    if not mayuscula.search(contrasena):
        fuerte = False
        sugerencias.append("Debe incluir al menos una letra mayúscula.")
    if not minuscula.search(contrasena):
        fuerte = False
        sugerencias.append("Debe incluir al menos una letra minúscula.")
    if not numero.search(contrasena):
        fuerte = False
        sugerencias.append("Debe incluir al menos un número.")
    if not especial.search(contrasena):
        fuerte = False
        sugerencias.append("Debe incluir al menos un carácter especial.")

    # Mensaje final
    if fuerte:
        return "La contraseña es fuerte. ¡Excelente!"
    else:
        return "La contraseña es débil. Sugerencias: " + ", ".join(sugerencias)

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas ")
st.subheader("Aplicación creada por Miguel Ángel Villarraga Franco")
st.markdown("**¿Qué tan segura es tu contraseña?**")

contrasena = st.text_input("Ingrese su contraseña", type="password")
if st.button("Evaluar"):
    resultado = evaluar_contrasena(contrasena)
    st.success(resultado) if fuerte else st.warning(resultado)

# Información adicional
st.info("Una contraseña fuerte incluye una combinación de letras mayúsculas y minúsculas, números y caracteres especiales.")
st.write("**Consejos adicionales:**")
st.write("- Evita usar contraseñas obvias como fechas de nacimiento o nombres.")
st.write("- Utiliza un gestor de contraseñas para almacenar tus contraseñas de forma segura.")
