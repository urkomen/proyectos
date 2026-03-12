import Metodos_varios as mv
import Tablero as tb
import Barcos as bar
import Disparos as disp
import Fases_del_juego as fdj
import random
import time


def disparos_usu(tablero1, tablero2, tablero3, barcos_PC):
    while True:
        coord_disp = disp.recibir_disparos()
        
        # Si las coordenadas no son válidas, las volvemos a pedir
        if not disp.comprobar_coords(tablero2, coord_disp):
            print("Coordenadas inválidas. Inténtalo de nuevo.\n")
            continue
            
        print("Disparo realizado.\n")
        time.sleep(2)        
        
        
        # Si el objetivo no es un barco, cambio de turno
        if not disp.comprobar_objetivo2(coord_disp, tablero1, tablero2):
            print('Cambio turno')
            break
        
        tb.mostrar_tableros2(tablero2, tablero3)
        
        # Buscamos cuál es el barco impactado
        # barco = {'tipo': 1, 'coords': [], 'hundido': False}
        for i, barco in enumerate(barcos_PC):
            if coord_disp in barco['coords']:
                ind = i

        # Se ha hundido el barco?
        if bar.barco_hundido(tablero1, barcos_PC, ind):
            for coord in barcos_PC[ind]['coords']:
                # Pintamos en los dos tableros del PC
                tb.pintar_casilla(tablero1, coord, 'HUNDIDO')
                tb.pintar_casilla(tablero2, coord, 'HUNDIDO')
            barcos_PC[ind]['hundido'] = True
            tb.mostrar_tableros2(tablero2, tablero3)
            print("Barco hundido!")
            time.sleep(1)
        
        
        # Quedan barcos por hundir?
        if not bar.quedan_barcos(barcos_PC):
            return True, barcos_PC # Si no hay barcos por hundir --> fin de juego
            
    time.sleep(1)        
    return False, barcos_PC



def disparos_PC(tablero1, tablero2, barcos_usu):
    while True:
        coord_disp = disp.recibir_disparos(maquina = True)
        
        # Si las coordenadas no son válidas, las volvemos a pedir
        if not disp.comprobar_coords(tablero2, coord_disp):
            print("Coordenadas inválidas. Inténtalo de nuevo.\n")
            continue
            
        print("Disparo realizado.\n")
        time.sleep(2)        
        
        # Si el objetivo no es un barco, cambio de turno
        if not disp.comprobar_objetivo(coord_disp, tablero2):
            print('Cambio turno')
            break
        
        tb.mostrar_tableros2(tablero1, tablero2)
        
        # Buscamos cuál es el barco impactado
        ind = 0
        for i, barco in enumerate(barcos_usu):
            if coord_disp in barco['coords']:
                ind = i

        # Se ha hundido el barco?
        if bar.barco_hundido(tablero2, barcos_usu, ind):
            for coord in barcos_usu[ind]['coords']:
                tb.pintar_casilla(tablero2, coord, 'HUNDIDO')
            barcos_usu[ind]['hundido'] = True
            tb.mostrar_tableros2(tablero1, tablero2)
            print("Barco hundido!")
            time.sleep(1)
            
            
        # Quedan barcos por hundir?
        if not bar.quedan_barcos(barcos_usu):
            return True, barcos_usu  # Si no hay barcos por hundir --> fin de juego
    
    time.sleep(1)        
    return False, barcos_usu






def recibir_disparos(maquina = False):
    '''
    Recibir coordenadas del disparo del usuario
    '''
    
    if not maquina:
        coords = input(f"Introduce coordenadas del objetico que quieres disparar (ej: A1, C2, G9): ")
        casilla = mv.coords2index(coords)
    else:
        casilla = disparo_aleatorio()
    
    return casilla
    
    

def comprobar_objetivo(coords:tuple[int, int], tablero:tuple[int, int]):
    '''
    Comprobar si el disparo de la máquina impacta en un barco del usuario o cae al agua
    '''
    
    
    if tb.es_agua(tablero, coords[0], coords[1]):
        tb.pintar_casilla(tablero, coords, 'DISP_AGUA')
        # tb.mostrar_tableros2(tablero, tablero)
        print("Agua!")
        time.sleep(1)
        
        return False # Disparo al agua
    
    else:    
        tb.pintar_casilla(tablero, coords, 'TOCADO')
        # tb.mostrar_tableros2(tablero, tablero)
        print("Tocado!")
        # Comprobar si el barco se ha hundido
        # if bar.barco_hundido(tablero, coords):
        #     print("Barco hundido!")
        #     tb.pintar_casilla(tablero, coords, 'HUNDIDO')
        
        return True # Impacto en un barco


def comprobar_objetivo2(coords:tuple[int, int], tablero1:tuple[int, int], tablero2:tuple[int, int]):
    '''
    Comprobar si el disparo del usuario impacta en un barco enemigo o cae al agua
    '''
    
    
    if tb.es_agua(tablero1, coords[0], coords[1]):
        tb.pintar_casilla(tablero1, coords, 'DISP_AGUA')
        tb.pintar_casilla(tablero2, coords, 'DISP_AGUA')
        print("Agua!")
        time.sleep(1)
        
        return False # Disparo al agua
    
    else:    
        tb.pintar_casilla(tablero1, coords, 'TOCADO')
        tb.pintar_casilla(tablero2, coords, 'TOCADO')
        # tb.mostrar_tablero(tablero2)
        print("Tocado!")
        
        return True # Impacto en un barco



def comprobar_coords(tablero:tuple[int, int], casilla:tuple[int, int]):
    '''
    Comprobar si las coordenadas introducidas están dentro del tablero
    '''
    
    # Índice fuera de rango (tablero 10x10)
    for ind in casilla:
        if ind < 0 or ind > 9:
            print('El disparo ha terminado en Narnia. Int')
            return False
    
    # Casilla previamente disparada
    if tb.ya_disparado(tablero, casilla[0], casilla[1]):
        # tb.mostrar_tablero(tablero)
        print('Ya has disparado en esa casilla')
        return False
    
    return True



def disparo_aleatorio():
    fil = random.randint(0,9)
    col = random.randint(0,9)
    
    return (fil, col)