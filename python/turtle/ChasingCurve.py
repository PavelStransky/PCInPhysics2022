from turtle import Turtle

ACOEF = 1.1

def init_hunter(x=-400, y=300):
    hunter = Turtle()
    hunter.penup()
    hunter.setposition(x, y)
    hunter.color("green")
    hunter.speed(0)
    hunter.pendown()

    hunter.setheading(0)

    return hunter

def init_dog(x=-400, y=-300):
    dog = Turtle()
    dog.penup()
    dog.setposition(-400, -300)
    dog.color("red")
    dog.speed(0)
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

def chasing_curve_events(hunter_velocity=2, dog_velocity=5, dt=1):
    hunter = init_hunter()
    dog = init_dog()

    def right_event():
        hunter.right(3)

    def left_event():
        hunter.left(3)

    def up_event():
        nonlocal hunter_velocity
        hunter_velocity *= ACOEF

    def down_event():
        nonlocal hunter_velocity
        hunter_velocity /= ACOEF

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)
    hunter_screen.onkeypress(right_event, "Right")
    hunter_screen.onkeypress(left_event, "Left")
    hunter_screen.onkeypress(up_event, "Up")
    hunter_screen.onkeypress(down_event, "Down")
    hunter_screen.listen()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()


#chasing_curve_straight()
#chasing_curve_circle(hunter_velocity=8, hunter_turn_velocity=2)
chasing_curve_events(dog_velocity=3)