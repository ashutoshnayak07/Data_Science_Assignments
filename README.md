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
Then as the value of I iterates it get added to total & get stored in total so that for the next iteration there will be the updated value for (total) Variable
___________________________________________________________________________________________________________________________________________________
