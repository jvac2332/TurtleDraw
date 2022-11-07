import turtle


TEXTFILENAME = 'Turtledraw'

f = input('what is the name of file:')
fa = open(f)


screen = turtle.Screen()
screen.setup(450,450)


redhood = turtle.Turtle()
redhood.speed(10)

counter = 0
line = fa.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        redhood.color(color)
        redhood.goto(x,y)

       

        redhood.pendown()

    if (len(parts) == 1): 
        redhood.penup()
    if redhood.isdown():
        counter += redhood.distance(x,y)
    print('counter', counter)    
    line = fa.readline()
 


turtle.write(counter)
turtle.done()
fa.close()



print('\nEnd')

#/Users/joshuavachachira/lewis/cspc-2000/Sprint-5/demo