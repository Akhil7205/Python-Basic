

# Q)check the no is +ve or -ne or 0

# num=int(input('enter no to check: '))

# if num>0:
#     print('no is +ve no')
# elif num<0:
#     print('no is -ve no')
# else:
#     print('no is zero')


# # Q)check no is odd or even 
# num=int(input('enter no to check: '))

# if num%2==0:
#     print('no is even: ')
# else:
#     print('its odd')

# Q)check the largest no out of two and three

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


# Q ask the user for input and print that is eligible for vosting or not 

# vote=int(input('enter the age: '))
# if vote>18 and vote<110:
#     print("you are eligible for voting")
# else:
#     print('your are not eligible to vote')


# Q)Write a program that checks if a given number is divisible by both 5 and 7

# no=int(input("enter no to check 5 and 7:"))
# if(no%5==0 and no%7==0):
#     print('no is divisible from 5 and 7 ')
# else:
#     print('no is not divisible from 5 and 7')

# Q)Take three sides of a triangle as input and check if a valid triangle can be formed (sum of any two sides should be greater than the third).
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

# if side1+side2>side3 and side1+side3>side2 and side3+side2>side1 
#     print('vaild triangle')
# else:
#     print('envalid triangle')

# Q)Write a program that checks if a given year is a leap year.
# (A year is a leap year if it is divisible by 4 and not divisible by 100, unless also divisible by 400).

# leap=int(input('enter year:'))
# if(leap%4==0 and leap%100!=0 or leap%400==0):
#     print('its a leap year:')
# else:
#     print('its not a leap year')

# Q)ATM Withdrawal Logic:

# Take a withdrawal amount and balance as input.
# Print "Transaction Successful" if the withdrawal amount is a multiple of 100 and less than or equal to the balance.
# Otherwise, print "Transaction Failed".

withdrawal=int(input('enter bal amount:'))
bal=50000

if(withdrawal%100==0):
    print('cant be multiple of 100')
elif(bal > withdrawal ):
    print('Transation successful')
else:
    print('bal is not sufficent')

# Q)Password Strength Checker:

# Take a password as input and classify it as:
# "Weak" (length < 6)
# "Medium" (6 to 10 characters)
# "Strong" (more than 10 characters)

password=(input('enter no: '))
len=len(password)
if(len>=6 and len<=10):
    print('medium password')
elif(len>10):
    print('strong password')
else:
    print('week password')