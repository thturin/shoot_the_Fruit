import pgzrun, pygame, random
"""
Project Shoot the fruit 

Hacks and Tweaks 
add more actors to the game

keep count of the number of clicks (score)


"""
WIDTH = 1280
HEIGHT = 700

#introducing an actor/sprite
apple = Actor('apple')
pineapple = Actor('pineapple')
pineapple.x = random.randint(0,WIDTH-100)
pineapple.y = random.randint(0,HEIGHT-100)
orange = Actor('orange')
orange.x=random.randint(0,WIDTH-100)
orange.y=random.randint(0,HEIGHT-100)

count = 0

def draw():
    screen.fill((55, 100, 30))
  #  screen.clear()

    apple.draw()
    pineapple.draw()
    orange.draw()


def place_apple():
    apple.x = random.randint(0,WIDTH-100)
    apple.y = random.randint(0,HEIGHT-100)
    print(apple.x,apple.y)



def on_mouse_down(pos): #pre-built function in pygame zero that runs everytime you click the mouse
    global count
    if apple.collidepoint(pos): #collidepoint() is a method of the actor object that checks to see if the cursor is in the same position as the apple
        print("Good Shot!")
        count+=1
        print('Your total score is {}'.format(count))
        place_apple()
    else:
        print("You missed!")
        quit() #stops the program entirely



pgzrun.go()