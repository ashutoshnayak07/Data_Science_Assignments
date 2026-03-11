# Data_Science_Assignments
All assignments 
Assignment 2:
#Assignment _2_Task_1: Check if a Number is Even or Odd
Code:

num = int(input("Enter a number :"))
if num % 2 == 0: 
    print(f"{num} is an Even number.")
else: # If the number is not divisible by 2, then it is an Odd number.
    print(f"{num} is an Odd number.")

Explanation:
1st we take input from the user using (input) function & using typecasting make that input an integer ( as initial inputs are strings )
In 2nd line we check the number whether it's properly divisible by 2 or not by using modulo operator.
  If its divisible & its remainder is 0 then we print that number is an even number.
In the else statement we are checking the opposite of the if state ment 
  If the number is not divisible by 2 then it will give a remainder other than 0 so we print that the number is an odd number
___________________________________________________________________________________________________________________________________________________

#Assignment _2_Task_2:Sum of Integers from 1 to 50 Using a Loop
Code:

total = 0
for i in range(1, 51):
    total += i
print(f"The sum of numbers from 1 to 50 is: {total}")

Explanation:
1st we declare a variable total to keep the value of the sum of number from 1 - 50 & kept the starting value as 0 so that other garbage value wont get assigned to it.
Then we initiate a  for loop in which i will iterate in the range of 1 to 51 as the last is excluded & we need the sum of 50 numbers we keep the rage 1-51
___________________________________________________________________________________________________________________________________________________

#Assessment_3_Task 1: Calculate Factorial Using a Function

Code:
n=int(input("Enter a number: ")) #
def factorial(n): 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)
print(f"Factorial of {n} is: {result}")

Explanation: 
In first line we take input from the user. Then in second line we create a function which will calculate the factorial of any given number.Inside that function first it will check if the number is 0 or 1 ,& if the condition satisfies then it will return 1 otherwise it will run else part where we use recursive function as we are already inside factorial function & in the else part again its calling the factorial function. we call the second function by giving the input a less than the the current cycle number gradually ythe number will decrease to 1 & it will out of the loop. Then we in the last we print the result.

___________________________________________________________________________________________________________________________________________________

#Asssesment_3_Task 2: Using the Math Module for Calculations
import math

Code:
import math
num = int(input("Enter a number: ")) #Take input from the user
sqrt_num = math.sqrt(num) #Calculate the square root using the math module
natural_log= math.log(num) #Calculate the natural logarithm using the math module
sine_num= math.sin(num) #Calculate the sine using the math module

print(f"Square root: {sqrt_num}") #Print the square root of the number
print(f"Logarithm: {natural_log}") #Print the natural logarithm of the number
print(f"Sine: {sine_num}") #Print the sine of the number

Explanation: 
Here in first line we import the math module & then using that module we get the square root, log & sine of the number.

___________________________________________________________________________________________________________________________________________________
