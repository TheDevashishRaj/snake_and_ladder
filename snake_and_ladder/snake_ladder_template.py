import time
import turtle as tl
import random


#define the snakes---
snakes = {
    97:61,
    76:54,
    51:10,
    38:20,
    91:73
}

#define the ladders---
ladders = {
    5:58,
    14:49,
    53:72,
    64:83,
}




#set the screen--
scrn = tl.Screen()
scrn.screensize(700,700)
tl.bgpic("snake7.gif")



#player 1 to initial position
p1 = tl.Turtle()
p1.ht()
p1.shape("circle")
p1.color("white","green")
p1.up()
p1.setpos(-225,-225)
p1.speed(3)



#player 2 to initial position
p2 = tl.Turtle()
p2.ht()
p2.shape("circle")
p2.color("black","blue")
p2.up()
p2.setpos(-225,-225)
p2.speed(3)
pos1 = 1
pos2 = 1


        
#setting the dice
dice1 = tl.Turtle()
dice1.color("black","red")
dice1.up()
dice1.ht()
dice1.shape("square")
dice1.shapesize(2,2,1)  #to resizes the turtle
dice1.setpos(-300,0)


dice2 = tl.Turtle()
dice2.color("black","red")
dice2.up()
dice2.ht()
dice2.shape("square")
dice2.shapesize(2,2,1)  #to resizes the turtle
dice2.setpos(300,0)



#show all the turtles together--
dice1.st()
dice2.st()
p1.st()
p2.st()
time.sleep(1)