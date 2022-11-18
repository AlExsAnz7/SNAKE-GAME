from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Comic Sans', 24, 'italic')

class Scoreboard(Turtle): 

#Función para la configuración de la tabla de récord. 

    def __init__(self): 
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

#Función para la actualización de la tabla de récord.  

    def update_scoreboard(self): 
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)

#Función para definir en caso de perder el juego con la colisión erronéa de la serpiente, un anuncio que se dispare al instante.

    def game_over(self): 
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

#Función para el incremento del puntaje en la tabla de récord. 

    def increase_score(self): 
        self.score += 1
        self.clear()
        self.update_scoreboard()