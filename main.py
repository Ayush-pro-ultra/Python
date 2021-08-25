import turtle;
s = turtle.getscreen();
t = turtle.Turtle();
t.shape("turtle")
t.fillcolor("white")
t.speed(10)
t.pensize(20)
screen = turtle.Screen()
t.turtlesize(3,3,3)
t.fillcolor("green")
def going(x,y):
	t.pencolor("black")
	t.ondrag(None)
	t.goto(x,y)
	t.ondrag(going)
	
def cl(x1,y1):
     t.pencolor("")
     t.goto(x1,y1)
 			
t.ondrag(going)
screen.onclick(cl)
		
screen.mainloop()