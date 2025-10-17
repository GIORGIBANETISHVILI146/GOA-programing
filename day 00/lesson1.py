from turtle import*

#we want paint a house

# step 1: draw a square

width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)
     
forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end door

# drawing a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end roof

#drawing a window

goto(200, 200)
color("green")
left(30)
forward(60)
color("brown")
begin_fill()
right(90)
forward(65)
right(90)
forward(56)
right(90)
forward(64)
right(90)
forward(56)
end_fill()
right(90)
forward(32)
color("blue")
right(90)
forward(56)
color("brown")
right(90)
forward(33)
right(90)
forward(33)
color("blue")
right(90)
forward(64)

#end window



exitonclick()