from turtle import Turtle 
import random 

class Food(Turtle): 

#Función para darle forma a la comida de la serpiente. 

    def __init__ (self): 
        super().__init__()
        self.shape('triangle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()
    
#Función para la reaparición aleatoria de la comida de la serpiente por todo el plano cartesiano. 

    def refresh(self): 
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)