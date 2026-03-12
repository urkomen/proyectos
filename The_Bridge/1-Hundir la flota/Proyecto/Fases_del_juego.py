import Tablero as tb
import Barcos as bar
import Disparos as disp
import Display as dp
import time

def inicio_hundir(n = 10):
    ''' 
    INICIO DE JUEGO
        - Intro juego
        - Crear tablero inicial
        - Imprimir tablero
    '''
    
    intro_hundir()
    time.sleep(1)
    # dp.mostrar_imagen()
    # time.sleep(1.5)
    
    # tablero:
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    tb.limpiar()
    tablero_usu = tb.crear_tablero(n)
    tablero_PC = tb.crear_tablero(n)
    tablero_PCoculto = tb.crear_tablero(n)
    
    
    dp.intro(dp.frames_intro)
    time.sleep(1.5)
    
        
    tb.mostrar_tableros2(tablero_usu, tablero_PC)
    
    return tablero_usu, tablero_PC, tablero_PCoculto



def configuracion_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int]):
    '''
    CONFIGURACIÓN
        - Se colocan los barcos del usuario (modo manual/aleatorio)
          4 barcos de 1 casilla
          3 barcos de 2 casillas
          2 barcos de 3 casillas
          1 barco de 4 casillas
    '''
    
    # Usuario coloca sus barcos
    manual_aleatorio = 2 #input('Colocar barcos de manera (1 - manual o 2 - aleatoria): ')
    barcos = bar.lista_barcos
    if manual_aleatorio == '1':
        barcos_usu = bar.colocar_barcos(tablero_usu, barcos,True)
    else:
        barcos_usu = bar.colocar_barcos(tablero_usu, barcos, False)
    
    # Se colocan barcos de la máquina
    barcos_PC = bar.colocar_barcos(tablero_PC, barcos_usu, False)
    
    time.sleep(1.5)
    
    
    # tb.mostrar_tableros2(tablero_usu, tablero_PC)
    return barcos_usu, barcos_PC


def quien_empieza():
    empieza = input('Quién comienza el primer turno? (YO/PC)').upper()
    
    if empieza == 'YO':
        return 1
    else:
        return 0
    
    

def turnos_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int], tablero_PCoculto:tuple[int, int], barcos_usu:list, barcos_PC:list, turno:int):
    '''
    DISPAROS
        - Recibir coordenadas
        - Comprobación de objetivo
        - Marcar casilla (tocado/agua)
    '''
    
    tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
    print('Todo listo. Que comience la batalla!')
    time.sleep(1)
        
    fin = False
    # turno = 1
    
    while not fin:
        turno += 1 # Siguiente turno
        if turno%2 == 0: # Turnos pares son del usuario
            tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
            print('TURNO DE USUARIO')
            #urko
            # print(barcos_PC)
            fin, barcos_PC = disp.disparos_usu(tablero_PC, tablero_PCoculto, tablero_usu, barcos_PC)
        else: # Turnos impares son de la máquina
            tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
            print('TURNO DE PC')
            fin, barcos_usu = disp.disparos_PC(tablero_PCoculto, tablero_usu, barcos_usu)
        print(fin)

        tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
        print('Turno finalizado.')        
    
    if turno%2 == 0: 
        # El juego ha finalizado en el turno del usuario
        # Gana usuario
        return 'USUARIO'
    else:
        # El juego ha finalizado en el turno de la máquina
        # Gana máquina
        return 'MAQUINA'
    

def intro_hundir():
    tb.limpiar()
    for linea in dp.titulo_intro:
        print(linea)
        time.sleep(0.05)


def fin_hundir(gana):
    
    if gana == 'USUARIO':
        dp.outro(dp.frames_victoria)
    else:
        # Gana máquina
        dp.outro(dp.frames_derrota)
        

