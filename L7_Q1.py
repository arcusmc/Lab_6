#Chris Davidson
#October 20 2014
#GIS 501

import turtle,arcpy,random    #imports necessary systems

wn= turtle.Screen()    #opens a window to see turtle

Leonardo = turtle.Turtle()    #names the turtle

play = raw_input("How many sides would you like to draw, please use whole numbers? (ex-3):")


if play == "3":
    import turtle    #Draws a triangle
        
    wn = turtle.Screen()
    Three = turtle.Turtle()

    for i in range(3):
        Three.forward(100)
        Three.left(360/3)


elif play == "4":
    import turtle    #Draws a square

    wn = turtle.Screen()
    Four = turtle.Turtle()

    for i in range(4):
        Four.forward(100)
        Four.left(360/4)


elif play == "5":
    import turtle    #Draws a pentagon

    wn = turtle.Screen()
    Five = turtle.Turtle()

    for i in range(5):
        Five.forward(100)
        Five.left(360/5)

    
elif play == "6":
    import turtle    #Draws a hexagon

    wn = turtle.Screen()
    Six = turtle.Turtle()

    for i in range(6):
        Six.forward(100)
        Six.left(360/6)


elif play == "7":
    import turtle    #Draws a heptagon

    wn = turtle.Screen()
    Seven = turtle.Turtle()

    for i in range(7):
        Seven.forward(100)
        Seven.left(360/7)


elif play == "8":
    import turtle    #Draws an octagon

    wn = turtle.Screen()
    Eight = turtle.Turtle()

    for i in range(8):
        Eight.forward(100)
        Eight.left(360/8)


elif play == "9":
    import turtle    #Draws an enneagon

    wn = turtle.Screen()
    Nine = turtle.Turtle()

    for i in range(9):
        Nine.forward(100)
        Nine.left(360/9)


elif play == "10":
    import turtle    #Draws an decagon

    wn = turtle.Screen()
    Ten = turtle.Turtle()

    for i in range(10):
        Ten.forward(100)
        Ten.left(360/10)


elif play == "11":
    import turtle    #Draws an hendecagon

    wn = turtle.Screen()
    Eleven = turtle.Turtle()

    for i in range(11):
        Eleven.forward(100)
        Eleven.left(360/11)


elif play == "12":
    import turtle    #Draws an dodecagon

    wn = turtle.Screen()
    Twelve = turtle.Turtle()

    for i in range(12):
        Twelve.forward(100)
        Twelve.left(360/12)


elif play == "13":
    import turtle    #Draws an tridecagon

    wn = turtle.Screen()
    Thirteen = turtle.Turtle()

    for i in range(13):
        Thirteen.forward(100)
        Thirteen.left(360/13)


elif play == "14":
    import turtle    #Draws an tetradecagon

    wn = turtle.Screen()
    Fourteen = turtle.Turtle()

    for i in range(14):
        Fourteen.forward(100)
        Fourteen.left(360/14)


wn.exitonclick()

from arcpy import env

env.overwriteOutput = True

infile = "F:/GradSchool/MSGT_GIS_501/Labs/Lab_6/L7_Q1.py"

fc = "F:/GradSchool/MSGT_GIS_501/Labs/Lab_6/Polygon.shp"

arcpy.CreateFeatureclass_management("F:/GradSchool/MSGT_GIS_501/Labs/Lab_6", fc, "Polygon")

cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])

array = arcpy.Array()

point = arcpy.Point()

for line in fileinput.input(infile):

    point.ID, point.X, Point.Y, = line.split()

    line_array.add(point)

polygon = arcpy.Polygon(array)

cursor.insertRow([polygon])

fileinput.close()

for row in cursor:
    
    x, y = row[0]

    print("{0}, {1}".format(x, y))

del cur

#References:
#
#www.w3schools.com, www.microsoftvisualacademy.com, www.codeacademy.com, and google,
#http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html,
#https://www.python.org/, http://www.tutorialspoint.com/python/.htm
