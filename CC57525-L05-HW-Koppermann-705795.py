''' searches

1.1: eat
\beat(s|en|r|ing|ery?)?|ate\b

1.2 Gaddafi
M[oa][au']mm?[ae]r? ([AaEe][Il]?[- ])?[KG]h?a[dz]+h?af+[iy]

1.3 Isfahan
[Hh]?[iIeE][sṣ][bfp][aā]h[aā]n

1.4 Vienna
search ", " replace by |

2.1 switch positions
search: \t(\w+), (\w+)\n
replace: \2 \1

2.2 austrian cities: extra doc and replace ", " with |, place brackets around

2.3.
\b([\w ]+)(?=( \(Lower Austria\)))  
'''

#Zelle Exercises
#Chapter 6

#1 Old MACDONALD 

def donald():
    return "Old MACDONALD had a farm\n E-I-E-I-O\n"

def verseFor(x):
    animals= ["cow", "horse", "bird", "fish", "pig"]
    shouts= ["moo", "neigh", "peep", "blub", "oink"]
    a=donald()*2+ "and on his farm he had a "+ animals[x+1]+"\n"
    b="whith a "+ (shouts[x+1])*2+" here and a "+(shouts[x+1])*2+" there"+"\n"
    c="Everywhere "+(shouts[x+1])*2+"\n"
    lyrics= a+b+c+donald()
    return lyrics


def main():
    for x in range (4):
        print (verseFor(x))
main()

#2

def ground():
    return "\nAnd they all go marching down to the ground\nTo get out of the rain, BOOM! BOOM! BOOM!\n"

def verseFor(x):
    numbers=["one", "two", "three", "four"]
    activities=["suck his thumb", "tie his shoe", "climb a tree", "shut the door"]
    numbcount= "The ants go marching " + numbers[x]+" by "+numbers[x]+"\n"
    hurrah="hurrah, hurrah\n"
    acticount="the little one stops to "+activities[x+1]
    lyrics=(numbcount+hurrah)*2+numbcount+acticount+ground()
    return lyrics

def main():
    for x in range (3):
        print (verseFor(x))
    
    
main()

#3
from _typeshed import StrPath
import math

def sphereArea(r):
    return 4 * math.pi * r**2

def sphereVolume(r):
    return 4.0/3.0 * math.pi * r**3

def main():
    print ("i will compute surface area and volume of a sphere given the radius"
    r = float(input("Please enter the radius of the sphere: "))
    print ("the Surface area of the Sphere is %0.2f" %sphereArea(r))
    print ("the Volume  of the Sphere is %0.2f" %sphereVolume(r))

main()

#4

def sumN(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total

def sumNCube(n):
    total=0
    for i in range(1,n+1):
        total=total+i**2
    return total

def main():
    print ("this does somethin with rows")

    n=int(input("what is your number? "))
    print ("the sum of %d numbers is %d" % (n, sumN(n)))
    print ("the square of %d numbers is %d" % (n, sumNCube(n)))

main()


#5 - why does it not finish importing math??
import math

def pizzarea(d):
    return ((0,5*d)**2)*pi

def price(d):
    return pizzarea (d)/price

def main():
    d=float(input("what is the diameter of the pizza? "))
    price=float(input("what is the pizzas price"))
    print ("the size of the pizza is %0.2f cm2 and the price per cm2 is %0.2f") % (pizzarea(d), price(d))

main()

#6
import math

def triarea(a,b,c):
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

def main():

    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    print ("the surface area is %d") %(triarea(a,b,c))

main ()

#solution
import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def triArea(a, b, c):
    s = (a+b+c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def main():
    win = GraphWin("Draw a Triangle",500,500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p3,p1)
    message.setText("perimeter: %0.2f  area: %0.2f "
                    % ((d1+d2+d3),triArea(d1,d2,d3)))

    # Wait for another click to exit
    win.getMouse()

main()

#7 Fibonacci - why not working?

def fibon(n):
    curr, prev=1,1
    for i in range (n-2)
        curr, prev = curr+prev, curr
    return curr 

def main():
    print ("I calculate the fibunacci number of your choosing")
    n = int(input("enter Number "))
    print ("the fibunacci number is "+fibon(n)

main()

#8 - do nit understand the objective

#chapter 7
#1
def main():
    print("Weekly pay calculator\n")
    hours=float(input("how many hours did you work?"))
    hourwage=float(input("what is the wage per hour?"))
    if hours <= 40:
        wage=hours*hourwage
    else:
        wage=40*hourswage+(hours-40)*1,5*hourswage
    print ("your total wage is "+wage)

    main()


#solution
    def main():
    print ("Weekly pay calculator\n")
    hours = float(input("Enter hours worked: "))
    wage = float(input("Enter hourly wage: "))
    if hours <= 40:
        pay = hours * wage
    else:
        pay = 40 * wage + (hours-40) * 1.5 * wage

    print("Your week's pay is ${0:0.2f}".format(pay))
main()
if __name__ == '__main__':
    main()
#2
def main():
    score=int(input("what is your grade number? "))
    if score<=4.5:
        grade=A
    elif score<=3.5:
        grade=B
    elif score<=2.5:
        grade=C
    elif score<=1.5:
        grade=D
    elif score<=0.5:
        grade=E
    else:
        grade=F
    print ("your grade is", grade)
main()

#3
def main():
    score=int(input("what is your grade number? "))
    if score<=90:
        grade=A
    elif score<=80:
        grade=B
    elif score<=70:
        grade=C
    elif score<=60:
        grade=D
    else:
        grade=F
    print ("your grade is", grade)
main()

#4
def main():
    credits=int(input("what is your number of credits? "))
    if credits<=7:
        status=Sophomore
    elif credits<=16:
        status=Junior
    else credits<=26:
        status=Senior
  
    print ("your status is", status)
main()

#5
def main():
    weight=int(input("what is your weight? "))
    size=int(input("what is your hight? "))
    BMI=wight*720/size
    if BMI > 25:
        print ("you have a bit much BMI")
    elif BMI < 9:
        print ("you skinny")
    else:
        print ("you healthy")
    main()

#6 speed limit and fine
def main():
    speed=int(input("how fast are you going? "))
    limit=int(input("what is the speed limit? "))
    if speed<limit:
        print("your are driving ", speed, "and that is ok")
    elif (speed-limit)<=90:
        fine=50+5*(speed-limit)
        print("your are going too fast and have to pay ", fine, "dollars")
    elif speed>90:
        fine=50+5*(speed-limit)+200
        print("lunatic! pay ", fine, "dollars")
    else   
        print("sorry, I freaked it :´(")
main()

#7
def main():
    startHours, startMins = input("Starting time (hh:mm): ").split(":")
    endHours, endMins=input("End time (hh:mm): ").split(":")
    start=int(startHours)+float(startMins)/60
    end=int(endHours)+float(endMins)/60

    if end < start:
        end=end+24

    bedtime=21.0
    if start<bedtime:
        if end<bedtime:
            normalH=end-start
            nightH=0
        else:
            normalH=bedtime-start
            nightH=end-bedtime
    else
        normalH=0
        nightH=end-start 
    pay=normalH*2.5+nightH*1.5
    print("your wage is ", pay, "dollars, as you worked ", normalH, "normal Hours and", nightH, "nighthours")
main()

#8 representative

def rep():
    a=int(input("how old are you? "))
    c=int(input("for how long have you been a citizen? "))
    if a>= 30:
        if c>=9:
            sensent = "you can run for Senator, "
        else:
            sensent = "you can't run for Senator, "
    else:
            sensent = "you can't run for Senator, "
    if a>= 25:
        if c>=7:
            repsent = "you can run for House of Representatives"
        else:    
            repsent = "you can't run for House of Representatives"
    else:
            repsent = "you can't run for House of Representatives"
    
    print(sensent, repsent)
rep()
    

#easter
def (easter):
    year=int("input(easter which year?"))
    cannot="sorry, I cannot calculate that, its very hard."
    if year >=2048:
        sentence=cannot
    elif year<=1982:
        sentence=cannot
    else:
        a=year%19
        b=year%4
        c=year%7
        d=(19a+17)%30
        e=(2b+4c+6d+5)%7
        numdate=22+d+e
        month=March
        if numdate >=31:
            month="April "
        else:
            month="March "
            numdate=numdate-31
        print ("the date of easter ", year, " is ", month, numdate)
    easter()