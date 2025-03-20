"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *    # Importa todas las funciones de Turtle
import turtle # Importa el módulo de Turtle
from freegames import vector # Importa la clase vector de freegames


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)  # Mueve sin dibujar al punto inicial
    down()
    goto(end.x, end.y)  # Dibuja la línea hasta el punto final


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y) # Mueve sin dibujar al punto inicial
    down()
    begin_fill()  # Comienza a llenar la figura

    for count in range(4):   # Repite 4 veces para formar un cuadrado
        forward(end.x - start.x) # Mueve hacia adelante la distancia entre los puntos
        left(90) #Gira 90 grados a la izquierda

    end_fill()  # Termina de llenar la figura


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)  # Mueve sin dibujar al punto inicial
    down()
    begin_fill()  # Comienza a llenar la figura

    radius = (end.x - start.x) / 2  # Calcula el radio del círculo
    turtle.circle(radius)  # Dibuja el círculo con el radio calculado

    end_fill()  # Termina de llenar la figura


def rectangle(start, end):
    up()
    goto(start.x, start.y) # Mueve sin dibujar al punto inicial
    down()
    begin_fill()  # Comienza a llenar la figura

    # Dibuja los cuatro lados del rectángulo
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)

    end_fill() # Termina de llenar la figura


def triangle(start, end):
    up()
    goto(start.x, start.y) # Mueve sin dibujar al punto inicial
    down()
    begin_fill() # Comienza a llenar la figura

    # Dibuja un triángulo conectando tres puntos
    goto(end.x, start.y)
    goto((start.x + end.x) / 2, end.y)
    goto(start.x, start.y)

    end_fill() # Termina de llenar la figura


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start'] # Obtiene el punto inicial almacenado

    if start is None:
        state['start'] = vector(x, y) # Guarda el punto de inicio
    else:
        shape = state['shape'] # Obtiene la forma actual
        end = vector(x, y) # Define el punto final
        shape(start, end)  # Dibuja la forma con los puntos especificados
        state['start'] = None  # Reinicia el punto de inicio


def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Estado inicial del programa
state = {'start': None, 'shape': line}

# Configuración de la ventana
setup(420, 420, 370, 0)

# Configuración de eventos del ratón y teclado
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Configuración de colores con teclas
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Configuración de formas con teclas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
