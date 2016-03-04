# 2/4/16
print("Hello, what is your name?")
name = raw_input()
print("Hello " + name)

print("Enter a dividend.")
dividend = int(raw_input())

print("Enter a divisor.")
divisor = int(raw_input())

answer = int(dividend / divisor)
remainder = float(dividend % divisor)
 
if remainder != 0:
	print("{} divided by {} is {} with a remainder of {}".format(divisor, dividend, answer, remainder))

if remainder == 0:
	print("{} divided by {} is {}".format(divisor, dividend, answer))