# Importando librerias principales
import streamlit as st

# titulo APP
st.title('Tablas de Multiplicar')
st.write(
    '''
    [Repo-GitHub](https://github.com/D4n1Xp/tabla-multiplicar)
    '''
)
# body
st.write('Que tabla de multiplicar quieres consultar')

numero = st.number_input('Introduce la tabla a mostrar: ', step=1)

st.write(f'Has seleccionado la tabla de multiplicar: {numero}')

# Al pulsar el boton muestra la tabla elegida
if st.button('Mostrar tabla'):
    # Abre archivo y guarda el resultado de la tabla
    with open('archivo.txt', 'w') as file:
        for i in range(0, 13):
            resultado = i * numero
            total = f'{numero} x {i} = {resultado}'
            file.write(total + '\n')
            st.write(total)
    
    # Abre archivo, mustra boton y permite descargar fichero
    with open("archivo.txt", "r") as file:
     btn = st.download_button(
             label="Descargar tabla de multiplicar",
             data=file,
             file_name="archivo.txt",
             mime="text/plain"
           )

# Boton para limpiar y volver a empezar
if st.button('Limpiar'):
    st.write('Gracias :smile:')

st.markdown('**By. D4n1Xp**')
