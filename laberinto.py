laberinto = [
    ["recorrido" , "X" , "X" , "X" , "X"],
    ["recorrido" , "X" , "recorrido" , "recorrido" , "recorrido"],
    ["recorrido" , "X" , "recorrido" , "X" , "X"],
    ["recorrido" , "recorrido" , "recorrido" , "X" , "X"],
    ["X" , "X" , "X" , "X" , "X"]
]
#posiciones para el inicio de la partida
x=0
y=0

print("Comienza el juego. Para finalizarlo debe completar el laberito.")
print("Usted comienza en la casilla (0,0)")

while (laberinto[y])[x] == "recorrido":
    dirección_recorrido = input("¿Hacia que dirreción desea moverse?:")
    if dirección_recorrido == "arriba" or "abajo" or "derecha" or "izquierda":
        print ("El movimiento se ejecutara hacia", dirección_recorrido)
    if dirección_recorrido == "arriba":
        x = x
        y = y + 1
    if dirección_recorrido == "abajo":
        x = x
        y = y - 1
    if dirección_recorrido == "izquierda":
        x = x - 1
        y = y
    if dirección_recorrido == "derecha":
        x = x + 1
        y = y
    if (laberinto[y])[x] == "X":
        print ("Usted ha chocado contra un muro, elija otra dirrección.")
    
# A continuación muestro la posición en la que te encuentras

print ("Usted se encuentra en la posición ", "(", x , "," , y , ")")
