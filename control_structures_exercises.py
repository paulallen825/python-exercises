#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input ("Please enter the day of the week")
if day_of_week =="Monday":
    print("Today is Monday")
else:
    print("Today is not Monday")

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input("Please enter the day of the week ")
if day_of_week ==("Monday"or "Tuesday" or"Wednesday"or"Thursday"or"Friday"):
    print("Today is a weekday")
else:
    print("Its the weekend!")

#create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
hours_worked = 41
hourly_rate = 120
Reg_pay = hours_worked * hourly_rate
Over_pay = (40 *hourly_rate) +((hours_worked - 40) * (hourly_rate*1.5))

if hours_worked > 40:
        print(Over_pay)
else:
    print(Reg_pay)

#2 Loop Basics

#while Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = int(5)
while i <=15:
    print(i)
    i+=1

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

for i in range (0,101):
    if i % 2 == 0:
        print(i)

#Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i <=100 and i >= -10:
    print(i)
    i-=5

#Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i <=1000000:
    print(i)
    
    i=pow(i,2)

#b For Loops
#Write some code that prompts the user for a number, 
#then shows a multiplication table up through 10 for that number.


num = int(input(" Enter the number : ")) #taking the input and turning it to an integer   
    print("Multiplication Table of : ")  #The statement to print
for i in range(1,11):                    #creating the range to multiply the input by with the for statement "i"
    print(num,'x',i,'=',num*i)

#Create a for loop that uses print to create the output shown below.

for i in range(1,10): #creating the range starting at 1 and ending at 9
    cn=str(i)         #changing the input i to a string and creating a variable cn
    print (cn * i)    #printing the new string number "cn" the number of times in the range "i" 1-9

#c
#break and continue

#Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
#  (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement 
# to output all the odd numbers between 1 and 50, except for the number the user entered.








