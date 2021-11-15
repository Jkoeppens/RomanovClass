#Exercises Zelle Chapter 3

#1
from math import pi, sqrt


def main():
    import math
    from math import pi
    r=float(input("What is the radius? "))
    volume=((4/3)*pi*r**3)
    surface = (3.0*pi*r**2)
    print ("the Volume is ",volume)
    print (f"The surface Area is: {surface}")

main()

#2 price per surface area of pizza
def main():
    import math
    from math import pi
    price=float(input("what is the price "))
    #price = 9
    d=float(input("What is the diameter? "))
    #d = 24
    surface = (pi*(d/2)**2)
    pps = price/surface
    print ("the price per cm2 is ", pps)
main()

#3: weigth of molecules
def main():
    print ("Weight counter")
    print ("please enter the number of molecules for each element")
    H=int(input("how many Hydrogens"))
    C=int(input("how many Carbons"))
    O=int(input("how many Oxygens"))
    weight= ((H*1.00794)+(C*12.0107)+(O*15.9994))
    print ("the total weight in mole is: ", weight)
main()

#4: lightning distance
def lightning():
    print ("i will calculate distance of lightning")
    t=int(input(("how many seconds between lightning and thunder?")))
    d=t*343
    print ("the distance of the lightning was", d, "meters")
lightning()

#coffe delivery

def coffee():
    print("i will calculate the price of a coffee delivery for you")
    pricekg = 10.50
    pricedel = 1.50
    pricedelkg = 0.86
    kg=float(input("how many pounds of coffee do you want to order?"))
    price = pricekg*kg+pricedel+pricedelkg*kg
    print ("the price of your order would be ", price, "Dollars")
coffee()

#6. Slope

def slope():
    print("i will calculate the slope between two points")
    x1=float(input("what is the x coordinate of the frist coordinate?"))
    y1=float(input("what is the y coordinate of the frist coordinate?"))
    x2=float(input("what is the x coordinate of the second coordinate?"))
    y2=float(input("what is the y coordinate of the second coordinate?"))
    coordinate1 = [x1,y1]
    coordinate2 = [x1,y1]
    slope = (y1-y2)/(x1-x2)
    print ("the slope between", coordinate1, "and", coordinate2, "would be", slope)

slope()

#7 distance
def distance():
    import math
    print("i will calculate the distance between two points")
    x1=float(input("what is the x coordinate of the frist coordinate?"))
    y1=float(input("what is the y coordinate of the frist coordinate?"))
    x2=float(input("what is the x coordinate of the second coordinate?"))
    y2=float(input("what is the y coordinate of the second coordinate?"))
    coordinate1 = [x1,y1]
    coordinate2 = [x1,y1]
    dist=math.sqrt(x2-x1)**2+(y1-y2)**2
    print ("the distance between", coordinate1, "and", coordinate2, "would be", dist)
distance()

#8. easter
#does not work

def easter():
    year=int(input("easter which year?"))
    c=year//100
    epact=(8+(c//4)-c+((8*c+13)//25)+11(year%19))%30
    print ("easter in", year, "is", epact)

easter()

#Chapter 5
#dateconvert
#my model did not work:

'def dateconvert():
    print ("this converts numerical dates into Words")
    datestr = (input("please enter the date (mm/dd/yyy)"))
    monthstr, daystr, yearstr = datestr.split("/") 
    print monthstr
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month= months[int(monthstr)-1]
    print ("the date is", daystr, "th of ", month, yearstr)
    
dateconvert()'

def main():
    # get the day month and year
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = "{0}/{1}/{2}".format(month,day,year)

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    date2 = "{0} {1}, {2}".format(months[month-1],day,year)

    print("The date is {0} or {1}.".format(date1, date2))

main()


#2. Quizz grading
def grade1():
    numbgrade=int(input("enter your grade: "))
    chargrade = "FFDCBA"[numbgrade]
    print ("the grade is", chargrade)

grade1()

#3 grademaker 100
#I dont understand the operation in line 2
def grade1():
    numbgrade=int(input("enter your score out of 100: "))
    chargrade = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print ("the grade is", chargrade[numbgrade])

grade1()


#4. Acronym maker
def acron():
    words= input("Enter the words to be acronymed: ")
    acronym=""
    for word in words.split():
        acronym=acronym+word[0]
    acronym=acronym.upper()
    print("the acronym is", acronym)

acron()

#5. namevalue calculator
def namenumb():
    name=input("enter the name")
    total=0
    for letter in name:
        total=total+ord(letter.lower())-ord('a')+1
    print("the value is", total)
namenumb()

#6. namevalue 3 Names


def namenumb():
    name=input("enter the name")
    name1,name2,name3=name.split(" ") 
    name1numb=0
    name2numb=0
    name3numb=0
    
    for letter in name1:
        name1numb=name1numb+ord(letter.lower())-ord('a')+1    
print("the name value of ",name1 "is", name1numb,
    for letter in name2:
        name2numb=name2numb+ord(letter.lower())-ord('a')+1
print("the name value of ",name2 "is", name2numb)
    for letter in name2:
        name3numb=name3numb+ord(letter.lower())-ord('a')+1
    print("the name value of ",name3 "is", name3numb)
print("the total name value is", name1numb, "+"name3numb, "+"name3numb, "=", (name1numb+name2numb+name3numb))
namenumb()

#7 caesar cypher
def caesar():
    print("I will encode your message on a whacky basis")
    key=int(input("Enter a number as a key"))
    unenc=input("enter the message")
    unenc2=("")
    enc=""
    for letter in unenc:
        enc=enc+chr(ord(letter+key))
    print("the encoded message is: ", enc)

    unenc2=("")
    for letter in enc:
        unenc2=unenc2+chr(ord(letter+key))

    print("the deciphered message is", unenc2)

caesar()