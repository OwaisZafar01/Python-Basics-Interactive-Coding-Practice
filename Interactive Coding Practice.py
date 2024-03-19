# QUESTION 01

# User will input three ages.Find the oldest one

age1 = int(input("Enter age: "))
age2 = int(input("Enter age: "))
age3 = int(input("Enter age: "))

if age1 > age2 and age1 > age3:
    if age1 > age3 or age1 > age2:
        print(age1,"is the oldest")


elif age2 > age1 and age2 > age3:
    if age2 > age3 or age2 > age1:
        print(age2,"is the oldest")

elif age3 > age1 and age3 > age2:
    if age3 > age2 or age3 > age1:
        print(age3,"is the oldest")

# QUESTION 02
        
# Write a program that will convert Celsius value into Fahrenheit
        
cel_val = int(input("Enter value in celsius: "))
res = (cel_val * 9/5) + 32
print(res)


# QUESTION 03

# Take list as an input and sum of the elements

num = input("Enter values: ")
num = list(num)
num = [int(i) for i in num]
print(sum(num))


# QUESTION 04

# Write a program that will reverse a four digit number. Also it checks wheater the reverse is True.

num = input("Enter values: ")
temp = []
num = list(num)

for i in num:
    a = int(i)
    temp.append(a)

res = temp[::-1]

for i in res:
     print(i,end = "")

if num == res:
     print("\nValues Matched")
    
else:
     print("\nValues not Matched")


# QUESTION 05

# Check the year is leap or not

year = int(input("Enter year: "))

if year % 4==0:
    print(year,"is a Leap Year")

else:
    print(year,"is not a Leap Year")


# QUESTION 06

# Write a program that will tell weather the number entered by the user is even or odd

num = int(input("Enter a number: "))

if num <0:
    print(f"{num} is negative")

elif num % 2 == 0:
    print(f"{num} is an even number")

else:
    print(f"{num} is an odd number")


# QUESTION 07

# Write a program to find the euclidean distance between two coordinates.

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
result = ((x2 - x1) **2 ) + ((y2 - y1) ** 2) **2

print(float(result))


# QUESTION 08

# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

angle1 = int(input("Enter angle: "))
angle2 = int(input("Enter angle: "))
angle3 = int(input("Enter angle: "))

if angle1 + angle2 + angle3 == 180:
    print("It's form a triangle")

else:
    print("It will not form a triangle ")


# QUESTION 9

# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost_price = int(input("Enter Cost Price: "))
selling_price = int(input("Enter Selling Price: "))

if cost_price > selling_price:
    print("You have in Loss")
else:
    print("You have in Profit")


# QUESTION 10

# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

principle_amount = int(input("Enter principle amount: "))
rate_of_interest = int(input("Enter rate of interest: "))
time_period = int(input("Enter time period: "))

simple_interest = (principle_amount * rate_of_interest * time_period) / 100
print(simple_interest)


# QUESTION 11

# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math

radius = float(input("Enter radius of a cylinder: "))
height = float(input("Enter height of a cylinder: "))

volume_of_cylinder = (math.pi*radius**2)*height
print("Volume is",round(volume_of_cylinder,3))

cost = volume_of_cylinder / 1000 * 40
print("Cost is",round(cost,3))

# QUESTION 12

# Write a program that will tell whether the given number is divisible by 3 & 6.

num = int(input("Enter a value: "))

if num % 3 == 0 and num % 6 == 0:
    print(num,"is divisible by 3 and 6")

else:
    print(num,"is not divisible")


# QUESTION 13
    
# Write a program that will determine weather when the value of temperature and humidity is provided by the user.

temp = int(input("Enter value: "))
humidity = int(input("Enter value: "))

if temp >= 30 and humidity >= 90:
    print("Hot and Humid")

elif temp >= 30 and humidity < 90:
    print("Hot")

elif temp < 30 and humidity >= 90:
    print("Cool and Humid")

elif temp < 30 and humidity < 90:
    print("Cool")


# QUESTION 14

# Write a program that will take three digits from the user and add the square of each digit.

num = input("Enter values: ")
num = list(num)
temp = []
final = []
add = 0
for i in num:
    a = int(i)
    temp.append(a)
for j in temp:
    j = j ** 2
    final.append(j)
    add += j

print("Sum of the squares of every element is",add)


# QUESTION 15

# Write a program that will check whether the number is armstrong number or not.

value = (input("Ennter number: "))
copy_list = list(value)
temp = []
final = []
for i in copy_list:
    a = int(i)
    temp.append(a)

for j in temp:
    j = j ** 3
    final.append(j)

count = 0

for k in final:
    count += k

if count == int(value):
    print(value,"is Armstrong number")
else:
    print(value,"is not a Armstrong number ")


# QUESTION 16

# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

print("Welcome to my page!\nWhat you want to do?\n\n1: cm to ft\n2: kl to miles\n3: usd to pkr\n4: Exit")

num = int(input("\nwhat do you want to do?: "))

if num == 1:
    ask1 = int(input("Enter value in Cm: "))
    print(round(ask1 / 30.48,3))

elif num == 2:
    ask2 = int(input("Enter value in kl: "))
    print(round(ask2 * 0.6214,3))

elif num == 3:
    ask3 = int(input("Enter value in usd: "))
    print((f"{ask3 * 250}pkr"))

elif num == 4:
    exit()
    

# QUESTION 17

# Write a program to find the sum of first n numbers, where n will be provided by the user

num = int(input("Enter a number: "))
count = 0

for i in range(1,num+1):
    count += i

print(count)


# QUESTION 18

# Write a program that can multiply 2 numbers provided by the user without using the * operator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum = 0

for i in range(0,num1):
    sum += num2
print(sum)


# QUESTION 19

# Write a program to print the first 25 odd numbers

num = int(input("Enter a value: "))
for i in range(1,num+1):
    if i % 2 != 0:
        print(i)
    

# QUESTION 20

# Print all the armstrong numbers in the range of 100 to 1000

for num in range(100, 1000):
    # Extracting digits
    digit_1 = num // 100
    digit_2 = (num % 100) // 10
    digit_3 = num % 10

    # Checking if it's an Armstrong number
    if num == (digit_1 ** 3) + (digit_2 ** 3) + (digit_3 ** 3):
        print(num)


# QUESTION 21

# Take a number from the user and find the number of digits in it. 


num = (input("Enter values: "))
num = list(num)
temp = []

count = 0
for i in num:
    count +=1 
   
print(count)


# QUESTION 22

# Count the number of vowels in a string provided by the user.

str = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for i in str:
    if i in vowels:
        count +=1 

print(count)


