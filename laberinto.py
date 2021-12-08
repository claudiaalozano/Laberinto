laberinto = {
    ["recorrido" , "X" , "X" , "X" , "X"],
    ["recorrido" , "X" , "recorrido" , "recorrido" , "recorrido"],
    ["recorrido" , "X" , "recorrido" , "X" , "X"],
    ["recorrido" , "recorrido" , "recorrido" , "X" , "X"],
    ["X" , "X" , "X" , "X" , "X"]

}
#posiciones para el inicio de la partida
x=0
y=0

print("Comienza el juego. Para finalizarlo debe completar el laberito.")
print("Usted comienza en la casilla (0,0)")

while (laberinto[y])[x] == "recorrido":
    dirección_recorrido = input("¿Hacia que dirreción desea moverse?:")
    if dirección_recorrido = "arriba" , "abajo" , "derecha" or "izquierda":
         
