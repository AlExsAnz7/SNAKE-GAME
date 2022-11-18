# PROYECTO: SNAKE GAME
<h2>Librería Turtle.</h2>

La libreria Turtle es una forma habitual de introduccion a la programacion a niños y niñas. Era una parte fundamental y original de la programación Logo, todo esto desarrolllado por Walley Feurzeig, Seymour Papet y Cynthia Solomon a mediados de 1967. Este lenguaje fue programado con fines educativos, el cuál incluye (haciéndole honor a su nombre) "gráficas tortugas". 

La "tortuga" de Logo es un cursor al que se le pueden dar órdenes de movimiento (avance, retroceso o giro) y que puede ir dejando un rastro sobre la pantalla. Moviendo adecuadamente la tortuga se pueden conseguir dibujar todo tipo de figuras.

Python incluye un módulo llamado "turtle" que permite crear gráficos de tortuga la cuál fue utilizada para la creación de este minijuego. 

# Creación del proyecto. 
El día de hoy creamos un minijuego de serpiente, el cual explicaré lo más breve posible. 

Antes de iniar, se debe crear la venta (o contenedor) que albergará a nuestra serpiente y todo nuestro minijuego. 

De esta forma la creamos: 

    screen = Screen()   
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    screen.tracer(0)

Todas estas son las medidas necesarias para que la ventana se cree, sin embargo, aún existe un factor que es necesario solucionar, el cuál es el cierre de la ventana. 

La ventana una vez creada, no tiene configurada la opcion de poder cerrarse una vez lo queramos, sino que estará cerrandose automáticamente. 

Esto es lo que necesitamos para que la ventana no pueda cerrarse autoamáticamente, sino que podamos cerrarla cada vez que queramos: 

    screen.exitonclick()

Ahora, una vez definido todo esto, prosigamos con la documentación.

El primer paso es crear a la serpiente, es decir, sus características y medidas. 

Este código es el neecsario para definirla: 

     def __init__(self): 
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

De esta forma creamos a la serpiente. Ahora, es darle movimiento. 

Este es el código necesario: 

    def create_snake(self): 
        for position in STARTING_POSITIONS: 
            self.add_segment(position)

"Starting position" es una función que definimos previamente, la cuál tiene una posición en el plano cartesiano de la librería de (0, 0). En pocas palabras, la serpiente inicializa en el centro de la pantalla, y el movimiento se lo daremos nosotros mediante la codificación. 

Ahora, definamos la creación del aumento de la serpiente una vez colisione con su comida.

Este es el código para ello:

     def add_segment(self, position ): 
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

La función "add_segments" es la que permite que la serpiente pueda crecer una vez se alimente, lo cuál, a su vez, también se relaciona con el récord en la tabla de puntaje. 

Ahora, continuemos con darle movimiento a la serpiente. 

Primero debemos de definir el movimiento con las flechas, o en este caso, el movimiento que se deba admitir en grados por todo el plano cartesiano para la serpiente. 

De esta forma lo realizamos: 

    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270 
    LEFT = 180
    RIGHT = 0

Ahora, prosigamos con darle el movimiento a la serpiente: 

        def move(self): 
        for seg_num in range(len(self.segments) -1, 0, -1): 
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

"xcor" y "ycor" son funciones para definir el cursor en x & y.
"goto" es una función para definir hacía dónde tendrá que ir la serpiente. Cabe destacar que esta no es una función para garantizar el movimiento por todo el plano, sino que garantiza el movimiento hacia todas las direcciones que se dictamine a la serpiente. 

Ahora, esta es la función necesaria para garantizar el movimiento por todo el plano, seguidamente de las direcciones que se dictaminaron: 


    def up(self): 
       if self.head.heading() != DOWN:
        self.head.setheading(UP)

    def down(self): 
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self): 
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self): 
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)

Estas tres cumplen la funcionalidad de direccionar a la serpiente de arriba, abajo, izquierda y derecha debidamente de la dirección que se le entregue. 

Y por último pero no menos importante, creemos el crecimiento de la serpiente. 

    def extend(self): 
        self.add_segment(self.segments [-1].position())

De esta forma, la serpiente crece al colisionarse con su comida, y por supuesto, también aumenta el record en la tabla de puntaje. 

Para más información, favor de consultar la documentación en el código realizado.
