import random
import time

def MostrarTablero(tableroJuego, dimen):
    # 1. Definir e iniciar las variables
    fila = 0
    columna = 0
    # 2. Letrero
    print()
    print("------------------------------------------")
    print("| TABLERO - HUNDIR LA FLOTA |")
    print("------------------------------------------")
    
    # 3. Mostrar el tablero de juego
    for fila in range(dimen):
        for columna in range(dimen):
            print(tableroJuego[fila][columna], end=" ")
        print()
    
    print()

def TamTablero(nivelDificultad):
    # 1. Definir e iniciar variables
    long = 0
    
    # 2. Obtenemos el tamaño del tablero, en función de la dificultad: 1 --> 3x3;  2 --> 4x4; 3 --> 5x5
    if nivelDificultad == 1:
        long = 3
    elif nivelDificultad == 2:
        long = 4
    else:
        long = 5
    
    return long

def Jugar(tablero, long):
    # 1. Definir e iniciar variables
    barcos = 0
    intentos = 0  # Máximo de 5 intentos para hundir los barcos
    filaUsuario = 0
    columnaUsuario = 0
    
    # 2. Pedir filas y columnas tantas veces como número de intentos tengamos, y comprobar si es un barco
    while intentos < 5:
        # 2.1. Pedir fila y columna
        time.sleep(1)
        print()
        print(f"Intento {intentos + 1}")
        time.sleep(1)
        filaUsuario = int(input(f"Introduce un número de fila [0-{long-1}]: "))
        columnaUsuario = int(input(f"Introduce un número de columna [0-{long-1}]: "))
        
        # 2.2. Comprobamos si en esa posición del tablero, hay un barco. De ser así, lo marcamos como hundido
        if tablero[filaUsuario][columnaUsuario] == "B":
            print("         ¡¡Barco hundido!!")
            tablero[filaUsuario][columnaUsuario] = "H"
            barcos += 1
        else:
            print("¡Agua!")
        
        # 2.3. Incrementamos el número de intentos
        intentos += 1
        
        # 2.4. Si ya hemos hundido todos los barcos, no hace falta que sigamos con más intentos y podemos acabar el bucle
        if barcos == 3:
            intentos = 5
    
    # 3. Mostramos el tablero final, llamando a otra función
    MostrarTablero(tablero, long)
    
    return barcos

# Juego de Hundir la flota
def HundirFlota():
    # 1. Definir e inicar variables
    tablero = []
    dificultad = 0
    dimen = 0
    fila = 0
    columna = 0
    barcos = 0
    filaBarco = 0
    columnaBarco = 0
    barcosHundidos = 0
    
    print("---------------------------------------")
    print("¡Bienvenido al juego Hundir la Flota!")
    print("---------------------------------------")
    print()
    time.sleep(3)
    
    # 2. Llamar a la funcion que establece el tamño del tablero en función de la dificultad del juego
    print("Introduce la dificultad del juego: 1 (fácil) | 2 (medio) | 3 (alta)")
    dificultad = int(input())
    
    dimen = TamTablero(dificultad)
    
    # 3. Dar dimensión al tablero
    tablero = [["**" for _ in range(dimen)] for _ in range(dimen)]
    
    # 4. Creamos el tablero
    print("Creando tablero...")
    time.sleep(1)
    
   # 4.2. Poner los tres barcos, de forma aleatoria
    while barcos < 3:
        filaBarco = random.randint(0, dimen - 1)
        columnaBarco = random.randint(0, dimen - 1)
        if tablero[filaBarco][columnaBarco] == "**":
            tablero[filaBarco][columnaBarco] = "B"
            barcos += 1
        else:
            # Si la posición ya está ocupada, volvemos a generar nuevas coordenadas
            continue
    
    print("---------------------------------------")
    print("-----------¡Tablero creado!------------")
    print("---------------------------------------")
    print()
    
    # 5. Llamar a la función que ejecuta el juego
    print("¡Empieza el juego! Tienes 5 intentos para adivinar los 3 barcos. ¡Suerte!")
    barcosHundidos = Jugar(tablero, dimen)
    
    # 6. Comprobamos si hemos ganado, en base del número de barcos hundidos devueltos por la función
    if barcosHundidos == barcos:
        print("¡Has ganado! Has hundido todos los barcos")
    else:
        print("¡Perdiste! Aún quedan barcos")

# Llamamos a la función principal para ejecutar el juego
HundirFlota()
