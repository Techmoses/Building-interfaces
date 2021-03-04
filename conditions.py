age = int(input("Enter your age: "))

if age <= 12:
	print("It's great to be a kid!")
elif age in range(13, 20):
	print("You're a teenager!")
else:
	print("Time to grow up")

# If any of these statements are true
# the corresponding message will be displayed.
# If neither statement is true, the "else"
# message is displayed.

#===========================================
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# Later in the program, you can call your Fibonacci
# function for any value you specify
fib(1000)

#==============================================
# Each number in the Fibonacci sequence is 
# the sum of the previous two numbers 
a, b = 0, 1
while b < 100:
	print(b, end=' ')
	a, b = b, a+b
