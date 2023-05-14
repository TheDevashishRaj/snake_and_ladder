from snake_ladder_template import *

#for beautifying the movement of turtle:--
def move_to(p,ps,x):
    '''this part of code makes turtle to move one by one step'''
    p.speed(5)
    while ps != x:
        p.goto(get_xy(ps+1))
        ps += 1
        time.sleep(0.4)
      

#function to roll the dice--
def roll_dice():
    return random.randint(1,6)

#function to get the (x,y) for a given cell--
def get_xy(x: int) -> tuple:
    if (x//10)%2 == 0:
        if x% 10 ==0:
            x_coordinate = 0
        else:
            x_coordinate = (x%10 -1)*50
    else:
        if x%10 == 0:
            
            x_coordinate = 9*50
        else:
            x_coordinate = (10-x%10)*50
        

    if x%10 == 0:
        y_coordinate = (x//10 - 1) * 50 
    else:
        y_coordinate = (x//10)*50

    
    
    return (-225 + x_coordinate,-225 + y_coordinate)



while(pos1!=100 and pos2!=100):
    r1 = roll_dice()
    
    dice1.write(r1,move=False,align="center",font=("Arial",20,"normal"))
    dice1.ht()
    time.sleep(0.3)
    dice1.st()
    
    for i in range(3):
        dice1.undo()
    #print(f"you got {r1}")
    x = pos1 + r1
    if x<=100:
        move_to(p1,pos1,x)
    if x in snakes:
        x = snakes[x]
    elif x in ladders:
        x = ladders[x]
    elif x>100:
        x = x - r1
    pos1 = x
    p1.goto(get_xy(x))
    time.sleep(1)
    if pos1==100:
        break
    
    r2=roll_dice()
    dice2.write(r2,move=False,align="center",font=("Arial",20,"normal"))
    dice2.ht()
    time.sleep(0.3)
    dice2.st()
   
    for i in range(3):
        dice2.undo()
    #print(f"you got {r2}")
    x = pos2 + r2
    if x<=100:
        move_to(p2,pos2,x)
    if x in snakes:
        x = snakes[x]
    elif x in ladders:
        x = ladders[x]
    elif x>100:
        x = x -r2
    pos2 = x
    p2.goto(get_xy(x))
    time.sleep(1) 

result = tl.Turtle()
result.ht()
result.up()
result.color("black","white")

if pos1 == 100:
    result.write("Congrates! first player wins the game",move=True,align="center",font=("Lucida sans",30,"normal"))
else:
    result.write("Congrates! second player wins the game",move=True,align="center",font=("Lucida sans",30,"normal"))

tl.done()