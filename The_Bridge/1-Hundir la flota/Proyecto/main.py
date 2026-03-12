import Tablero as tb
import Barcos
import Fases_del_juego as fdj
# Tablero.path.append("./Proyecto")

def main():
    # Crear 3 tableros:
        # tablero_usu: Tablero con los barcos del usuario (se muestran los disparos del PC)
        # tablero_PC: Tablero con los barcos del PC (no se muestra al usuario)
        # tablero_PCoculto: Tablero con los disparos del usuario
    tablero_usu, tablero_PC, tablero_PCoculto = fdj.inicio_hundir()
    
    # Tablero usuario
    # fdj.configuracion_hundir(tablero_usu)
    # Tablero del PC
    barcos_usu, barcos_PC = fdj.configuracion_hundir(tablero_usu, tablero_PC)
    
    #urko - pruebas
    # tb.mostrar_tablero(tablero_PC)
    # input()
    
    # Se escoge turno de inicio
    turno = fdj.quien_empieza()
    
    ganador = fdj.turnos_hundir(tablero_usu, tablero_PC, tablero_PCoculto, barcos_usu, barcos_PC, turno)
    
    fdj.fin_hundir(ganador)
    
    



if __name__ == "__main__":
    main()





    