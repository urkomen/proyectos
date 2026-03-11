
import Tablero as tb
import time
import os
from PIL import Image
# import pathlib

# Frases de fin de partida
VICTORIA = '¡Arrr, victoria pirata! \nTus cañones han hablado y los barcos enemigos ya alimentan a los peces. \n¡El tesoro del océano es tuyo!'

DERROTA = 'Las olas se llevan los restos de tu flota… \nEl mar ya no es tuyo.'

frames_intro = [
    "El mar está en calma…\n\n      🌊",
    "Una sombra aparece en el horizonte…\n\n      🌊     🚢",
    "La flota se aproxima lentamente…\n\n      🌊   🚢🚢",
    "Los barcos toman posición. \n\n      🌊 🚢🚢🚢",
    "Las banderas ondean… el silencio es absoluto.\n\n      🚢💥🚢💥🚢",
    "¡Comienza la partida!"
]
frames_victoria = [
    "Las olas se abren paso… tu flota avanza victoriosa.\n      🌊",
    "Las olas se abren paso… tu flota avanza victoriosa.\n      🌊🚢",
    "El enemigo se retira. Tu bandera ondea en el horizonte.\n      🌊🚢🏳️",
    "La batalla ha terminado. El mar es tuyo.\n      🌊🚢🏳️✨",
    "¡Victoria total!\n      🚢✨🚢✨",
    "Tus barcos navegan libres. El océano te pertenece.\n      🌊🚢🌊🚢🌊",
    VICTORIA
]
frames_derrota = [
    "Tu última nave se tambalea entre las olas...",
    "Tu última nave se tambalea entre las olas...\n     🌊",
    "Tu última nave se tambalea entre las olas...\n     🌊🌊",
    "Tu última nave se tambalea entre las olas...\n     🌊🌊🌊",
    "El casco cede... el barco se hunde lentamente.\n     🌊🌊🌊   ⚓",
    "Solo quedan burbujas en la superficie.\n     🌊🌊💧🌊🌊",
    "GAME OVER.\nTu flota descansa en el fondo del mar.\n     ⚓☠️⚓",
    DERROTA
]


titulo_intro = [
" ███████╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗███████╗",
" ██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝",
" █████╗  ███████║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗",
" ██╔══╝  ██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║",
" ███████╗██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║",
" ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝",
"                                                                  ",
"                         PRESENTA...                              "
]


def intro(frames):
    tb.limpiar()
    for f in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(f)
        time.sleep(1.5)

def outro(frames):
    tb.limpiar()
    for f in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(f)
        time.sleep(1.6)

# No me ha dado tiempo para añadir la imagen, descarto la idea
# def mostrar_imagen():
#     img_path = pathlib.Path(__file__).parent / "img" / "hundir.png"
#     img = Image.open(img_path)
#     img.show()
