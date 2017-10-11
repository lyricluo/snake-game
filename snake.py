from tkinter import*
import random

class Display :
    
    def __init__ ( self ) :
        self.root = Tk ()
        self.height = 400
        self.eidth = 640
        self.label = Label(self.root,text = 'Food Snake')
        self.label.pack ()
        self.canvas = Canvas( self.root,height = 400,width = 640,bg = 'black')
        self.canvas.pack()
        self.game = Game()
        self.snake = Snake()
        self.food = Food()
        self.root.bind('<Key>', self.KeyPress)
        self.direction = 'right'
        self.live = 1
        
    def KeyPress (self,event):
        sym = event.keysym
        if sym == 'w' and self.direction != 'down':
            self.direction = 'up'
        elif sym == 's' and self.direction != 'up':
            self.direction = 'down'
        elif sym == 'd' and self.direction != 'left':
            self.direction = 'right'
        elif sym == 'a' and self.direction != 'right':
            self.direction = 'left'
            
    def Refresh(self):
        if self.live == 0:
            self.canvas.delete('all')
        else:
            self.canvas.delete('all')
            self.update()
            self.drawFood()
            self.drawSnake()
            self.root.after(150,self.Refresh)
    def update(self):
        if (self.snake.body[0][0],self.snake.body[0][1]) == (self.food.fx,self.food.fy):
            self.snake.body.append((self.a,self.b))
            self.draw(self.food.fx,self.food.fy,'yellow')
            self.food.randomPosition()
            self.game.score += 1
        else:
            if self.direction =='left':
                self.snake.body.insert(0,(self.snake.body[0][0]-1,self.snake.body[0][1]))
                (self.a,self.b)=self.snake.body.pop(-1)
            elif self.direction =='right':
                self.snake.body.insert(0,(self.snake.body[0][0]+1,self.snake.body[0][1]))
                (self.a,self.b) = self.snake.body.pop(-1)
            elif self.direction == 'up':
                self.snake.body.insert(0,(self.snake.body[0][0],self.snake.body[0][1]-1))
                (self.a,self.b) = self.snake.body.pop(-1)
            elif self.direction == 'down':
                self.snake.body.insert(0,(self.snake.body[0][0],self.snake.body[0][1]+1))
                (self.a,self.b) = self.snake.body.pop(-1)
        if 0<=self.snake.body[0][0] < 32 and 0 <= self.snake.body[0][1]<20 :
            self.live = 1
            for i in range(1,len(self.snake.body)):
                if (self.snake.body[0][0],self.snake.body[0][1]) == (self.snake.body[i][0],self.snake.body[i][1]):
                    self.live = 0
        else:
            self.live = 0     
    def draw(self,x,y,color):
        self.canvas.create_rectangle(20*x,20*y,20*(x+1),20*(y+1),fill = color)
    def drawFood(self):
        self.draw(self.food.fx,self.food.fy,'red')
    def drawSnake(self):
        for i in self.snake.body:
            self.draw(i[0],i[1],'yellow')
class Food:
    def __init__(self):
        self.fx = 16
        self.fy = 0    
    def randomPosition(self):
        self.fx = random.randrange(0,32)
        self.fy = random.randrange(0,20)
            
        
class Snake:
    def __init__(self):
        self.body = []
        self.body = [(2,0),(1,0),(0,0)]
            
class Game:
    def __init__(self):
        self.score = 0
        self.food = Food()
        self.snake = Snake()
        
    
f=Display()
f.Refresh()
