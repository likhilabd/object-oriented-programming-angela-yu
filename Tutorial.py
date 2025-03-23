from turtle import Turtle, Screen

timmy = Turtle()
print(timmy) #prints <turtle.Turtle object at 0x11292fc10>. means new Turtle object from(<) turtle module at location 
#class(Turtle) is a blueprint, first letter is capital
#object(car, timmy) is a thing which can be made from that blueprint or class
#attributes(has= speed, fuel) are the variable which are associated wtih the things or objects 
#methods(does=move(),stop()) are the functions which are associated with the things or objects

my_screen= Screen() #from class(blueprint) called Screen we create an object called my_screen
print(my_screen.background_color) #we call an attribute(variable) called background_colour of an object my_screen
my_screen.exitonclick()


#dont paste the above code, paste the below one

from turtle import Screen, Turtle

timmy=Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(150)



my_screen=Screen()
my_screen.screensize(300,300)
my_screen.exitonclick()
