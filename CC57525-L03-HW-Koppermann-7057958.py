""""
 1. False/true
1. False
2. False
3. False
4. True
5. True
6. True
7. True
8. False
9. True
10. False

2. Multiple Choice
1. c
2. a
3. a
4. c
5. c
6.
7. b
8. d
9. a
10. d





"""

def conv1():
	print("this converts Degrees Celsius into Degrees Fahrenheit")
    celsius = eval(input("Whats the temperature in Celsius"))
    fahrenheit = (9/5*celsius+32)
    print("the temperature in Fahrenheit is:", fahrenheit, "degrees.")
    input("press any key to end the program")
	conv1()


#Exam average

def average():
	print("this calculates the average grade for three exams")
	a=eval(input("Grade one: "))
	b=eval(input("Grade two: "))
	c=eval(input("Grade three: "))
	print("a"+"b"+"c", ""=")
	print((a+b+c)/3)
average()




def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

def conv2():
	print("this converts Degrees Celsius into Degrees Fahrenheit")
    celsius = eval(input("Whats the temperature in Celsius"))
	for i in range(5):
		fahrenheit = 9/5*celsius+32
		print("the temperature in Fahrenheit is:", fahrenheit, "degrees.")
    input("press any key to end the program")
conv2()

def conv2():
	celsius=0
	for i in range(10):
		celsius=celsius+10
		fahrenheit = (9/5*celsius+32)
		print("the temperature in Fahrenheit is:", fahrenheit, "degrees, ", celsius, "degrees celsius")
conv2()


def interestreturn():
	principal = eval(input("what did you invest in the beginning?"))
	#x=eval(input("how many years to run?"))
	interest=eval(Input("whats the interest rate"))
	#annually=eval(input("what do ou invest annually"))
	#balance = annually

	for i in range(10)
		principal = principal*(1 + interest)
		#balance =((balance*(1+interest)+anually)
	
print("after", x, "years", "you get back", Investment)

interestreturn()

def main():
  #  print("This program calculates the future value")
   # print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = 1/3+eval(input("Enter the annual interest rate: "))
	y=eval(input("how many years?: "))
	p=y/4

    for i in range(p):
        principal = principal * (1 + apr)

print("The value after",y, "years is:", principal)

main()


#9
def conv1():
	print("this converts Degrees Fahreinheit into Degrees Celsius")
    fahrenheit = eval(input("Whats the temperature in Celsius"))
	celsius = (fahrenheit-39)*5/9
    print("the temperature in Celsius is:", celsius, "degrees.")
conv1()

#12
def calc():
	for i in range(100):
		print("this is a calculator")
		calculation=input("What do you want to calculate?")
		result=eval(calculation)
	print(calculation, "=", result)
calc()