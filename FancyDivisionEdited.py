# 2/4/16
print("Hello, what is your name?")   # asks the user what their name is						
name = raw_input()
print("Hello " + name)			     # greets user

print("Enter a dividend.")			 # gets the dividend the user wants to use
dividend = int(raw_input())

print("Enter a divisor.")			  # gets the divisor the user wants to use
divisor = int(raw_input())

answer = int(dividend / divisor)	  # gets the answer with no remainder
remainder = float(dividend % divisor) # gets the remainder of the two numbers
 
if remainder != 0:
	print("{} divided by {} is {} with a remainder of {}".format(divisor, dividend, answer, remainder)) # if the remainder is no 0, the program prints the answer with the remainder 

if remainder == 0:
	print("{} divided by {} is {}".format(divisor, dividend, answer)) # if the remainder is 0, it means there is no remainder and the program prints the answer without the remainder clause