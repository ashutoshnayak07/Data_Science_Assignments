#Calculate Factorial Using a Function
n=int(input("Enter a number: ")) #Take input from the user
def factorial(n): #Calculate factorial using a recursive function
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)
print(f"Factorial of {n} is: {result}") #Print the result to the user