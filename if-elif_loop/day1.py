

# Q1)check the no is +ve or -ne or 0

# num=int(input('enter no to check: '))

# if num>0:
#     print('no is +ve no')
# elif num<0:
#     print('no is -ve no')
# else:
#     print('no is zero')


# # Q2)check no is odd or even 
# num=int(input('enter no to check: '))

# if num%2==0:
#     print('no is even: ')
# else:
#     print('its odd')

# Q3)check the largest no out of two and three

# num1=int(input('enter no to check: '))
# num2=int(input('enter no to check: '))
# num3=int(input('enter no to check: '))

# if(num1>num2 and num1>num3):
#     print('num1 is greater no')
# elif(num2>num1 and num2>num3):
#     print('num2 is greater no ')
# elif(num3>num1 and num3>num2):
#     print('num3 is greater no ')
# elif(num1==num2 or num2==num3 or num3==num1):
#     print('two no are greater and of same value')
# else:
#     print('try again')


# Q4 4ask the user for input and print that is eligible for vosting or not 

# vote=int(input('enter the age: '))
# if vote>18 and vote<110:
#     print("you are eligible for voting")
# else:
#     print('your are not eligible to vote')


# Q5)Write a program that checks if a given number is divisible by both 5 and 7

# no=int(input("enter no to check 5 and 7:"))
# if(no%5==0 and no%7==0):
#     print('no is divisible from 5 and 7 ')
# else:
#     print('no is not divisible from 5 and 7')

# Q6)Take three sides of a triangle as input and check if a valid triangle can be formed (sum of any two sides should be greater than the third).
# side1=int(input('enter side1:'))
# side2=int(input('enter side2:'))
# side3=int(input('enter side3:'))

# if side1+side2>side3:
#     print('its a valid triangle')
# elif side2+side3>side1:
#     print('its a valid triangle')
# elif side1+side3>side2:
#     print('its a valid triangle')
# else:
#     print('its not a valid triangle')

# better version****************

# if side1+side2>side3 and side1+side3>side2 and side3+side2>side1 :
#     print('vaild triangle')
# else:
#     print('envalid triangle')

# Q7)Write a program that checks if a given year is a leap year.
# (A year is a leap year if it is divisible by 4 and not divisible by 100, unless also divisible by 400).

# leap=int(input('enter year:'))
# if(leap%4==0 and leap%100!=0 or leap%400==0):
#     print('its a leap year:')
# else:
#     print('its not a leap year')

# Q8)ATM Withdrawal Logic:

# Take a withdrawal amount and balance as input.
# Print "Transaction Successful" if the withdrawal amount is a multiple of 100 and less than or equal to the balance.
# Otherwise, print "Transaction Failed".

# withdrawal=int(input('enter bal amount:'))
# bal=50000

# # if(withdrawal%100!=0):
# #     print('cant be multiple of 100')
# if(bal >=withdrawal and withdrawal%100==0 ):
#     print('Transation successful')
# else:
#     print('bal is not sufficent')

# Q9)Password Strength Checker:

# Take a password as input and classify it as:
# "Weak" (length < 6)
# "Medium" (6 to 10 characters)
# "Strong" (more than 10 characters)

# password=(input('enter no: '))
# len=len(password)
# if(len>=6 and len<=10):
#     print('medium password')
# elif(len>10):
#     print('strong password')
# else:
#     print('week password')


# nested ifelese
# find which is greater n1,n2,n3
# n1=int(input('enter no n1:'))
# n2=int(input('enter no n2:'))
# n3=int(input('enter no n3:'))

# if(n1>n2):
#     if(n1>n3):
#         print('n1 is greater no')
#     else:
#         print('n3 is grater no')
# else:
#     if(n2>n3):
#         print('n2 is greater no')
#     else:
#         print('n3 is greater no')



# num=int(input('enter no:'))

# if(num%5==0 or num %3==0):
#     if(num%15==0):
#         print('no is divisble with 15')
#     else:
#         print('no is not div by 15 but dvi by 5 or 3')
# else:
#     print("no is not div 3, 5  and 15")


# match 

# n1=int(input('enter no n1:'))
# n2=int(input('enter no n2:'))
# operator=(input('operation to perform:'))

# match operator:
#         case "+":
#                 print('sum is',n1+n2)
#         case "-":
#                 print('sub is',n1-n2)
#         case "//":
#                 print('floor div is',n1//n2)
#         case "**":
#                 print('power is',n1**n2)


# ternary operator 



no=int(input('enter no:'))

num= f'{no} is even' if no%2==0 else f' {no} is ood'
print(num)