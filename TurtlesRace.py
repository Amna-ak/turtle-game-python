# Created on 4/15/2020
# Author @Amina Khalil
# Amna-ak
from turtles import *
import turtle
from random import *
import time

class TurtleRaceGame:
    def __init__(self):
        self.window=turtle.Screen()
        self.window.title("Turtle Race")
        self.window.bgcolor("black")
        self.stamp_list=[]
        """- this list keeps track of the number of steps taken by each turtle. The
        length of this list should also be equal to the number of turtles."""
        self.steps_list=[0,0,0,0,0]
        """this list should be of length three and keeps track of the winners
        of the race."""
        self.winners_list=[]
        self.bank=0
    """this function draws a square at location (x,y), where x is
    represents the x-axis, and y represents the y-axis"""
    def draw_squares(self,x,y):
        self.stamp_size=20
        self.square_size=15
        self.square=turtle.Turtle()
        self.square.speed(0)
        self.square.color("white")
        self.square.shape("square")
        self.square.shapesize(0.5,0.5)
        self.square.penup()
        self.square.setx(x)
        self.square.sety(y)
        self.square.pendown()
    # Function to draw starting line
    def draw_start(self):
        self.line=turtle.Turtle()
        self.line.color('white')
        self.line.write(" ")
        self.line.penup()
        self.line.goto(-250,200)
        self.line.right(90)
        self.line.forward(10)
        self.line.pendown()
        self.line.forward(400)
    # Function to draw finishing line , calls draw_box function to draw multiple boxes
    def draw_finish(self):
        x1=220
        y1=200
        x2=230
        for i in range(0,20):
            self.draw_squares(x1,y1)
            y1=y1-10
            self.draw_squares(x2,y1)
            y1=y1-10
    """- this function stamps a turtle at location (x,y). The turtle
    will have the color represented by a string represented by the variable color"""
    def stamp_turtle(self,x,y,color):
        tess=turtle.Turtle()
        tess.color(color)
        tess.shape('turtle')
        #self.tess.backward(300)
        tess.penup()
        tess.setx(x)
        tess.sety(y)
        tess.pendown()
        #self.tess.goto(200,y)
        #self.tess.up()
        #self.tess.stamp()
        return tess
    # Function to decide if the user has won the bet or not
    # bet_turtle is turtle for which user bet
    """The winnings can be calculated by the following formula:
    winnings = [ ( number of turtles (which is 5) / finishing place ) × bet amount ]"""
    def bet(self,bet_amount,bet_turtle):
        wining=0
        if self.winners_list[0]==bet_turtle:
            wining=(5/1)*bet_amount
        elif self.winners_list[1]==bet_turtle:
            wining=(5/2)*bet_amount
        elif self.winners_list[2]==bet_turtle:
            wining=(5/3)*bet_amount
        else:
            wining=0-bet_amount
        #print(wining)
        return wining
    def mainM(self,bet_amount,bet_turtle):
        self.draw_start()
        self.draw_finish()
        # initialize 5 turtles with different color
        self.A=self.stamp_turtle(-250,100,"blue")
        self.B=self.stamp_turtle(-250,50,"red")
        self.C=self.stamp_turtle(-250, 0, "orange")
        self.D=self.stamp_turtle(-250, -50, "yellow")
        self.E=self.stamp_turtle(-250, -100, "green")
        time.sleep(1)
        # Move turtles randomly
        for turn in range(170):
            A_step=randint(1, 5)
            self.steps_list[0]+=A_step
            B_step=randint(1, 5)
            self.steps_list[1] += B_step
            C_step=randint(1, 5)
            self.steps_list[2] += C_step
            D_step=randint(1, 5)
            self.steps_list[3] += D_step
            E_step=randint(1, 5)
            self.steps_list[4] += E_step
            # Stop race if three turtles have crossed the finishing point
            if len(self.winners_list)==3:
                break
            # Check if any turtle has cross the finishing point and add it in winning list
            if self.steps_list[0]>=481 and len(self.winners_list)<3 :
                if 'A' not in self.winners_list:
                    self.winners_list.append('A')
            if self.steps_list[1]>=481 and len(self.winners_list)<3 :
                if 'B' not in self.winners_list:
                    self.winners_list.append('B')
            if self.steps_list[2]>=481 and len(self.winners_list)<3 :
                if 'C' not in self.winners_list:
                    self.winners_list.append('C')
            if self.steps_list[3]>=481 and len(self.winners_list)<3 :
                if 'D' not in self.winners_list:
                    self.winners_list.append('D')
            if self.steps_list[4]>=481 and len(self.winners_list)<3 :
                if 'E' not in self.winners_list:
                    self.winners_list.append('E')
            #print(self.steps_list)
            #print(self.winners_list)
            self.A.forward(A_step)
            self.B.forward(B_step)
            self.C.forward(C_step)
            self.D.forward(D_step)
            self.E.forward(E_step)
        # add current stamps to stamp list
        self.stamp_list.append(self.A.stamp())
        self.stamp_list.append(self.B.stamp())
        self.stamp_list.append(self.C.stamp())
        self.stamp_list.append(self.D.stamp())
        self.stamp_list.append(self.E.stamp())
        #print(self.steps_list)
        #print(self.winners_list)
        # Call function to decide for bet
        wins=self.bet(bet_amount,bet_turtle)
        #self.window.exitonclick()
        #print("winner",wins)
        self.A.clearstamp(self.steps_list[0])
        # Return the winning points and winning list
        return wins,self.winners_list

"""The game begins by asking the user for a bet and a turtle to bet on (the number of turtles is up to you, in
our example the number of turtles is 5, you can also name your turtles)"""
print("Welcome to Turtle Racing")
# Amount in dollars is 100 at start
wins=100
"""To keep track the numbers of times each turtle has
come in first, second, or third. """
wins_t1=[0,0,0]
wins_t2=[0,0,0]
wins_t3=[0,0,0]
wins_t4=[0,0,0]
wins_t5=[0,0,0]
while True:
    bet_amount=int(input("How much do you want to bet $"))
    bet_turtle=''
    while True:
        turtle_number=int(input("which turtle?(1 to 5)? "))
        if turtle_number==1:
            bet_turtle='A'
            break
        elif turtle_number==2:
            bet_turtle='B'
            break
        elif turtle_number==3:
            bet_turtle='C'
            break
        elif turtle_number==4:
            bet_turtle='D'
            break
        elif turtle_number==5:
            bet_turtle='E'
            break
        else:
            print("Invalid choice...Please enter again")

    t = TurtleRaceGame()
    bet_res,win_lst=t.mainM(bet_amount,bet_turtle)
    # update list after one round
    for i in range(3):
        if win_lst[i]=='A':
            wins_t1[i]+=1
        elif win_lst[i]=='B':
            wins_t2[i]+=1
        elif win_lst[i]=='C':
            wins_t3[i]+=1
        elif win_lst[i]=='D':
            wins_t4[i]+=1
        elif win_lst[i]=='E':
            wins_t5[i]+=1
    #w=bank+bet_res
    wins=wins+bet_res
    print("Your win so far ",wins,"$")
    choice=input("Do you want to play again? y/n")
    if choice=='y':
        t.window.reset()
    else:
        break

#print(wins_t1)
#print(wins_t2)
#print(wins_t3)
#print(wins_t4)
#print(wins_t5)
"""At the end, the program will write to a file called ‘history.txt’ the numbers of times each turtle has
come in first, second, or third. """
f=open('History.txt','a')
r1="Turtle 1 first:"+str(wins_t1[0])+" second:"+str(wins_t1[1])+" third:"+str(wins_t1[2])+"\n"
r2="Turtle 2 first:"+str(wins_t2[0])+" second:"+str(wins_t2[1])+" third:"+str(wins_t2[2])+"\n"
r3="Turtle 3 first:"+str(wins_t3[0])+" second:"+str(wins_t3[1])+" third:"+str(wins_t3[2])+"\n"
r4="Turtle 4 first:"+str(wins_t4[0])+" second:"+str(wins_t4[1])+" third:"+str(wins_t4[2])+"\n"
r5="Turtle 5 first:"+str(wins_t5[0])+" second:"+str(wins_t5[1])+" third:"+str(wins_t5[2])+"\n"
data=r1+r2+r3+r4+r5
print(data)
f.writelines(data)