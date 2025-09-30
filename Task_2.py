import turtle
import math

def draw_tree(t, length, level):
    if level == 0:
        return
    
    t.forward(length)

    pos = t.pos()
    ang = t.heading()

    # left branch
    t.left(45)
    draw_tree(t, length / math.sqrt(2), level - 1)

    # turn back to the original position and angle
    t.penup()
    t.setpos(pos)
    t.setheading(ang)
    t.pendown()

    # right branch
    t.right(45)
    draw_tree(t, length / math.sqrt(2), level - 1)

    # turn back to the original position and angle
    t.penup()
    t.setpos(pos)
    t.setheading(ang)
    t.pendown()

def main():
    wn = turtle.Screen()
    wn.title("Pythagoras Tree")
    wn.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    
    level = int(input("Enter the number of levels (5 - 12): "))
    draw_tree(t, 100, level)

    wn.mainloop()

if __name__ == "__main__":
    main()
