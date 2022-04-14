from turtle import Turtle

def init_hunter(x=-400, y=300):
    hunter = Turtle()
    hunter.penup()
    hunter.setposition(x, y)
    hunter.color("green")
    hunter.pendown()

    hunter.setheading(0)

    return hunter

def init_dog(x=-400, y=-300):
    dog = Turtle()
    dog.penup()
    dog.setposition(-400, -300)
    dog.color("red")
    dog.pendown()

    return dog

def chasing_curve_straight(hunter_velocity=2, dog_velocity=5, dt=1):
    hunter = init_hunter()
    dog = init_dog()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

def chasing_curve_circle(hunter_velocity=2, dog_velocity=5, hunter_turn_velocity=1, dt=1):
    hunter = init_hunter(x=0)
    dog = init_dog()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        hunter.right(hunter_turn_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

#chasing_curve_straight()
chasing_curve_circle(hunter_velocity=8, hunter_turn_velocity=2)