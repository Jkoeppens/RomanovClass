#1 fibunacci
def fibunacci():
    print("I calculate the nth fibunacci number")
    n=int(input("what n? "))
    x,y=1,1
    for i in range (n-2):
        x,y=x+y,x
    print("the ", n , "th fibunacci is ", x)
fibunacci()
        




#   Windchill Table

# c08ex02.py
#   Windchill Table

def windChill(t, v):
    if v > 3:
        chill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    else:
        chill = t
    return chill

def main():

    # Print table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(40))
    print("MPH|", end=' ')
    temps = list(range(-20,61,10))
    for t in temps:
        print("{0:5}".format(t), end=' ')
    print("\n---+" + 55 * '-')

    # Print lines in table
    for vel in range(0,51,5):
        print("{0:3}|".format(vel), end=' ')
        for temp in temps:
            print("{0:5.0f}".format(windChill(temp, vel)), end=' ')
        print()
    print()

main()


#when double?


def main():
    print("number of years to double")
    interest=(float(input("what interest rate?")))
    have=1
    y=0
    while have < 2:
        have=have*(1+interest)
        y=y+1
    #print(y)
    print ("whith an interest of ", interest, "you would need ", y, "years to double your initial investment")

main()

#
def main():
    x=int(input("enter a number "))
    while x>1:
        if x//2==0:
            x=x/2
        else:
            x=3*x+1
        print (x)
main()

# in dont understand the job

# prime giver
from math import sqrt
def isPrime(n):
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True

def main():
    print(" i will give you all the primes up to your number")
    n=int(input("what is your number: "))
    for i in range (2,n+1):
        if isPrime(i):
            print(i, " is prime")
    print("done")
main()




#chapter 11
#1
from math import sqrt

def getnumbers():
    numbs = []
    xStr=input("enter a Numberl, enter to quit") #why not already float?
    while xStr != "":
        x=float(xStr)
        numbs.append(x)
        xStr=input("enter a Numberl, enter to quit") #why not already float?
    return numbs #why?

def mean (numbs):
    sum=0.0
    for numb in numbs:
        sum=sum+numb
        return sum/len(numbs)

def meanStDev(numbs):
    xbar=mean(numbs)
    sumDevsq=0.0
    for numb in numbs:
        dev=numb-xbar
        sumDevsq=sumDevsq+dev**2
    return xbar, sqrt(sumDevsq/(len(numbs)-1))

def stdev():
    xbar, stdev=meanStDev(numbs)
    return stdev

def median(numbs):
    numbs.sort()
    size=len(numbs)
    mid=size/2
    if size%2==0:
        #median=(numbs[int(mid)])
        median=(numbs[int(mid)] + numbs[int(mid)-1]) / 2
    else:
        median=numbs[int(mid)]
    return median

def main():
    print("I will give you the mean, median and standard deviation of numbers")
    data=getnumbers()
    xbar, stdev =meanStDev(data)
    med=median(data)
    print("\n the mean is ", xbar)
    print("\nthe standard deviation is ", stdev)
    print("\n the median is", med)

if __name__ == '__main__': main()
