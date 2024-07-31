import streamlit as st
import base64
from PIL import Image
import io
import time


def gif_to_base64(gif_path):
    with open(gif_path, "rb") as gif_file:
        return base64.b64encode(gif_file.read()).decode("utf-8")

# Reemplaza con la ruta de tu GIF
gif_base64 = gif_to_base64("gi.gif")
# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Bienvenida Lov <3</h1>", unsafe_allow_html=True)


# Inicializar estado para controlar la visibilidad del contenido
if "step" not in st.session_state:
    st.session_state.step = 0
if "confirmar_seleccion" not in st.session_state:
    st.session_state.confirmar_seleccion = False
if "opcion_seleccionada" not in st.session_state:
    st.session_state.opcion_seleccionada = None

# Función para avanzar al siguiente paso
def next_step():
    st.session_state.step += 1

# Mostrar contenido dependiendo del paso actual
if st.session_state.step == 0:
    # Cargar y reproducir primer archivo de audio
    audio_file = "/Users/cristianusca/Downloads/Intro.m4a"
    audio_bytes = open(audio_file, "rb").read()
    st.audio(audio_bytes, format="audio/m4a")
    
    # Botón para avanzar al siguiente paso
    if st.button("Siguiente"):
        next_step()

elif st.session_state.step == 1:
    # Mostrar primer texto
    st.write("¿Cuál sorpresa?")
    
    # Cargar y reproducir segundo archivo de audio
    audio_file_2 = "/Users/cristianusca/Downloads/Opción.m4a"
    audio_bytes2 = open(audio_file_2, "rb").read()
    st.audio(audio_bytes2, format="audio/m4a")
    
    # Botón para avanzar al siguiente paso
    if st.button("Siguiente"):
        next_step()

elif st.session_state.step == 2:
    # Mostrar segundo texto
    st.write("Por favor, selecciona una opción.")
    
    # Mostrar opciones y botón de confirmación
    opciones = ["Ya no te amo", "Estoy embarazado", "Vamos a ver a la MC"]
    st.session_state.opcion_seleccionada = st.selectbox("", opciones)
    
    if st.button("Confirmar selección"):
        st.session_state.confirmar_seleccion = True
        if st.session_state.opcion_seleccionada == "Vamos a ver a la MC":
            next_step()  # Avanzar inmediatamente al siguiente paso
        # No reiniciar confirmar_seleccion aquí para mantener la opción de mostrar mensajes

elif st.session_state.step == 3:
    if st.session_state.confirmar_seleccion:
        if st.session_state.opcion_seleccionada == "Ya no te amo":
            st.write("Amorcito yo te amo con mi vida, ¿Cómo crees que esta es la opción?😔")
        
        elif st.session_state.opcion_seleccionada == "Estoy embarazado":
            st.write("Creo que los hombres aun no nos podemos embarazar o whisky ya tendría 2")
        
        elif st.session_state.opcion_seleccionada == "Vamos a ver a la MC":
            # Mostrar el GIF sobre el contenido existente
            st.markdown(f"""
                <style>
                .overlay1 {{
                    position: fixed;
                top: 0;
                    left: 0;
                    width: 50%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 0;
                    background: rgba(0, 0, 0, 0);
                }}
                .overlay2 {{
                    position: fixed;
                    top: 0;
                    left: 50%;
                    width: 50%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 0;
                    background: rgba(0, 0, 0, 0);
                }}
                .overlay img {{
                    max-width: 1000%;
                    max-height: 1000%;
                }}
                </style>
                <div class="overlay1">
                    <img src="data:image/gif;base64,{gif_base64}" />
                </div>
                <div class="overlay2">
                    <img src="data:image/gif;base64,{gif_base64}" />
                </div>
                """, unsafe_allow_html=True)
            st.write("Correcto, así que ¿aceptas?")
            songs = "/Users/cristianusca/Downloads/song.mp3"
            audio_bytes_3 = open(songs, "rb").read()
            st.audio(audio_bytes_3, format="audio/m4a")
            
            reb = "/Users/cristianusca/Downloads/Reb.PNG"
            image = Image.open(reb)
            
            # Convertir imagen a base64
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            img_base64 = base64.b64encode(buffer.getvalue()).decode()

            # Mostrar imagen centrada
            st.markdown(f"<div style='text-align: center;'><img src='data:image/png;base64,{img_base64}' width='300'/></div>", unsafe_allow_html=True)
            
            che = "/Users/cristianusca/Downloads/Che.JPG"
            image_2 = Image.open(che)
            
            # Convertir imagen a base64
            buffer_2 = io.BytesIO()
            image_2.save(buffer_2, format="JPEG")
            img_base64_2 = base64.b64encode(buffer_2.getvalue()).decode()

            # Mostrar imagen centrada
            st.markdown(f"<div style='text-align: center;'><img src='data:image/png;base64,{img_base64_2}' width='300'/></div>", unsafe_allow_html=True)
            
            gif_base64 = gif_to_base64("/Users/cristianusca/Downloads/gi.gif")
            # Definir el arte ASCII del corazón lleno
            st.write = (
            "  ******     ******  ",
            "**    **   **    ** ",
            "**      ** **      **",
            "**       **       **",
            "**                **",
            " **             ** ",
            "   **         **   ",
            "     **     **     ",
            "       ** **       ",
            "         **         "
            )

        
            
            st.stop()  # Detiene la ejecución de la aplicación
            
# Mostrar la selección si se confirmó, independientemente del paso
if st.session_state.step == 2 and st.session_state.confirmar_seleccion and st.session_state.opcion_seleccionada != "Vamos a ver a la MC":
    if st.session_state.opcion_seleccionada == "Ya no te amo":
        st.write("Amorcito yo te amo con mi vida, ¿Cómo crees que esta es la opción?😔")
    elif st.session_state.opcion_seleccionada == "Estoy embarazado":
        st.write("Creo que los hombres aun no nos podemos embarazar o whisky ya tendría 2")
