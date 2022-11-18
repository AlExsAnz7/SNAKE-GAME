from  turtle import Turtle 
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0


#Definición y creación de la clase que hará cobrar vida a la serpiente. 

class Snake: 

    def __init__(self): 
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

#Función para la creación de la serpiente e inicialización de la misma en la posición 0, 0. 

    def create_snake(self): 
        for position in STARTING_POSITIONS: 
            self.add_segment(position)

#Función para la agregación de segmentos para garantizar el crecimiento de la serpiente mediante su comida. 

    def add_segment(self, position ): 
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

#Función para la extensión de la serpiente al momento de colisionar con su comida. 

    def extend(self): 
        self.add_segment(self.segments [-1].position())

#Función para garantizar el movimiento de la serpiente por todas las direcciones que se le dictaminen. 

    def move(self): 
        for seg_num in range(len(self.segments) -1, 0, -1): 
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

#Funciones para definir el movimiento por todo el plano cartesiano inicializado desde el punto (0, 0). 

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
