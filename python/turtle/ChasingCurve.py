from turtle import Turtle

def chasing_curve_straight(hunter_velocity=2, dog_velocity=5, dt=1):
    hunter = Turtle()
    hunter.penup()
    hunter.setposition(-400, 300)
    hunter.color("green")
    hunter.pendown()

    hunter.setheading(0)

    dog = Turtle()
    dog.penup()
    dog.setposition(-400, -300)
    dog.color("red")
    dog.pendown()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

chasing_curve_straight()