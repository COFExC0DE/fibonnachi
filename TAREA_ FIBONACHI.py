import turtle
turtle.reset()
turtle.speed(10)

def fibonachi(n):

    if n == 1:

        respuesta = 1

    elif n == 0:

        respuesta = 1

    else:

        respuesta = fibonachi(n - 1) + fibonachi(n - 2)

    return respuesta    

#def dibujar_espiral(n):

#def dibujar_espiral_aux(n):    

def cre_cuadrado(n):

    turtle.fw(90)
    turtle.left(90)
    crear_cuadrado_aux(n)

def crear_cuadrado_aux(lado, parada):

    if parada == 0:

        crear_cuadrado(n)
    
    
    
    
