import pgzrun, pygame, random

WIDTH = 1280
HEIGHT = 800

#introducing an actor/sprite
apple = Actor('apple')




def draw():
    screen.clear()
    apple.draw()
    #screen.blit('background',(0,0))

def place_apple():
    apple.x = random.randint(0,WIDTH-100)
    apple.y = random.randint(0,HEIGHT-100)
    print(apple.x,apple.y)



def on_mouse_down(pos): #pre-built function in pygame zero that runs everytime you click the mouse
    if apple.collidepoint(pos): #collidepoint() is a method of the actor object that checks to see if the cursor is in the same position as the apple
        print("Good Shot!")
        place_apple()
    else:
        print("You missed!")
        quit() #stops the program entirely



pgzrun.go()