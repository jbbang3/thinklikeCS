#1
import turtle
import math
bob=turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """ 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(bob, length, n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)

def circle(t,r):
    n=int(2*math.pi*r/5)
    polygon(t, n, 5)

def arc(t,r, angle):
    n=int((2*math.pi*r/5)*angle/360)
    for i in range(n):
        t.fd(5)
        t.lt(angle/n)

# polygon(bob,200,5)
# circle(bob,100)
arc(bob,100,170)

turtle.mainloop()