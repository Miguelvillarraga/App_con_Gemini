import streamlit as st
import re

# Función para verificar la fortaleza de la contraseña
def evaluar_contraseña(password):
    """
    Evalúa la fortaleza de una contraseña según los siguientes criterios:
    - Al menos 8 caracteres.
    - Al menos una letra mayúscula.
    - Al menos una letra minúscula.
    - Al menos un número.
    - Al menos un carácter especial.
    
    Parámetros:
        password (str): La contraseña que se va a evaluar.
    
    Retorna:
        dict: Un diccionario con el estado de los criterios y sugerencias.
    """
    criterios = {
        'Longitud mínima (8 caracteres)': len(password) >= 8,
        'Contiene mayúsculas': re.search(r'[A-Z]', password) is not None,
        'Contiene minúsculas': re.search(r'[a-z]', password) is not None,
        'Contiene números': re.search(r'[0-9]', password) is not None,
        'Contiene caracteres especiales': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    # Sugerencias basadas en los criterios que no se cumplan
    sugerencias = []
    if len(password) < 8:
        sugerencias.append('La contraseña debe tener al menos 8 caracteres.')
    if not re.search(r'[A-Z]', password):
        sugerencias.append('La contraseña debe contener al menos una letra mayúscula.')
    if not re.search(r'[a-z]', password):
        sugerencias.append('La contraseña debe contener al menos una letra minúscula.')
    if not re.search(r'[0-9]', password):
        sugerencias.append('La contraseña debe contener al menos un número.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        sugerencias.append('La contraseña debe contener al menos un carácter especial.')

    return criterios, sugerencias

# Interfaz de usuario con Streamlit
def main():
    st.title('Evaluador de Fortaleza de Contraseña')
    st.write('Ingrese su contraseña para evaluar su fortaleza.')
    
    # Entrada de contraseña
    password = st.text_input('Contraseña:', type='password')

    if password:
        # Evaluar la contraseña
        criterios, sugerencias = evaluar_contraseña(password)
        
        # Mostrar resultados
        st.subheader('Criterios de Seguridad:')
        for criterio, valido in criterios.items():
            if valido:
                st.markdown(f'✔️ **{criterio}**')
            else:
                st.markdown(f'❌ **{criterio}**')

        # Mostrar sugerencias
        if sugerencias:
            st.subheader('Sugerencias para mejorar la contraseña:')
            for sugerencia in sugerencias:
                st.markdown(f'- {sugerencia}')
        else:
            st.markdown('🎉 ¡Tu contraseña es segura!')

    # Información adicional
    st.markdown("---")
    st.write("Programado por Miguel Angel Villarraga Franco")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
