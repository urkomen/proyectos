import numpy as np
import os

# Constantes
AGUA = '⬜'
BARCO1 = '🛶'
BARCO2 = '⛵'
BARCO3 = '🚤'
BARCO4 = '🚢'
DISP_AGUA = '💦'
TOCADO   = '💥'
HUNDIDO  = '⚓'


coordenadas = ['A','B','C','D','E','F','G','H','I','J']

def crear_tablero(n=10): 
    '''
    Crea tablero de juego '~' representa agua
    Tamaño por defecto matriz cuadrada de dimensión 10
    '''
    # return np.full((n,n),'~')
    return np.full((n,n), AGUA)


def mostrar_tablero(tablero:tuple[int, int]):
    limpiar()
    print('TABLERO DE USUARIO')
    print('-'*30)
    dibujar_tablero(tablero)
    print('-'*30)
    
    
    
def mostrar_tableros2(tablero1:tuple[int, int], tablero2:tuple[int, int]):
    limpiar()
    print('TABLERO DE LA MÁQUINA')
    print('-'*30)
    dibujar_tablero(tablero1)
    print('-'*30)
    print('TABLERO DEL USUARIO')
    dibujar_tablero(tablero2)
    print('-'*30)
    
#URKO - Borrar tras pruebas
def mostrar_tableros3(tablero1:tuple[int, int], tablero2:tuple[int, int], tablero3:tuple[int, int]):
    limpiar()
    print('TABLERO DE LA MÁQUINA')
    print('-'*30)
    dibujar_tablero(tablero1)
    print('-'*30)
    print('TABLERO DEL USUARIO')
    dibujar_tablero(tablero2)
    print('-'*30)
    print('TABLERO OCULTO MÁQUINA')
    dibujar_tablero(tablero3)
    print('-'*30)
    
    
def dibujar_tablero(tablero:tuple[int, int]):
    '''
    Muestra el tablero en pantalla
    '''
    
    # Encabezado numérico
    numeros = "  " + " ".join(f"{i:2}" for i in range(1, 11))
    print(numeros)

    # Filas con letras
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        contenido = " ".join(fila)
        print(f"{letra} {contenido}")


def es_agua(tablero:tuple[int, int], fil:int, col:int):
    return tablero[fil][col] == AGUA

def ya_disparado(tablero, fil, col):
    casilla_disparada = tablero[fil][col] == TOCADO or tablero[fil][col] == DISP_AGUA or tablero[fil][col] == HUNDIDO
    return casilla_disparada


def pintar_casilla(tablero:tuple[int, int], casilla:tuple, state:str):
    '''
    Cambiamos el estado de la casilla del tablero: 
    BARCO(1)  --> '🛶'
    BARCO(2)  --> '⛵'
    BARCO(3)  --> '🚤'
    BARCO(4)  --> '🚢'
    DISP_AGUA --> '💦'
    TOCADO    --> '💥'
    HUNDIDO   --> '☠️'
    '''

    n = casilla[0]
    m = casilla[1]
    
    match state:
        case 'BARCO1':
            tablero[n,m] = BARCO1
        case 'BARCO2':
            tablero[n,m] = BARCO2
        case 'BARCO3':
            tablero[n,m] = BARCO3
        case 'BARCO4':
            tablero[n,m] = BARCO4
        case 'DISP_AGUA':
            tablero[n,m] = DISP_AGUA
        case 'TOCADO':
            tablero[n,m] = TOCADO
        case 'HUNDIDO':
            tablero[n,m] = HUNDIDO
    
    return tablero
    



def pintar_disparos():
    pass



def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


