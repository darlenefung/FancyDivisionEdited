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
 
if remainder != "0":
	print(str(divisor) + " divided by " + str(dividend) + " is " + str(answer) + " with a remainder of " + str(remainder))

if remainder == "0":
	print(str(divisor) + " divided by " + str(dividend) + " is " + str(answer))