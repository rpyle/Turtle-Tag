import turtle as trtl
import math
 

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

field_drawer = trtl.Turtle()
field_drawer.hideturtle()

def draw_gameboard():
  wn.tracer(False)
  field_drawer.pencolor("light gray")
  size = 18
  for j in range(-10,11,1):
    for i in range(-10,11,1):
      draw_tile(size, find_xy(size, (i,j)))
  wn.tracer(True)

def draw_tile(size, position):
  field_drawer.pu()
  field_drawer.goto(position)
  #field_drawer.write(position)
  field_drawer.setheading(30)
  field_drawer.forward(size)
  field_drawer.setheading(-90)
  field_drawer.pd()
  for i in range(6):
    field_drawer.forward(size)
    field_drawer.rt(60)

def find_xy(size, location):
  w = math.sqrt(3)*size
  h = 2*size
  x = location[0]*w+0.5*w*(location[1]%2)
  y = location[1]*h*3/4
  return (x,y)



draw_gameboard()

player_one = trtl.Turtle()
player_one.pu()
player_one.shape("turtle")
player_one.color("green")
player_one.goto(find_xy(18,(-10,10)))
player_one.rt(60)
player_one.forward(math.sqrt(3)*18)
player_one.lt(60)
player_one.forward(math.sqrt(3)*18)

wn.mainloop()


