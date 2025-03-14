# Lambda Function:-
# lambda funtion is also called anomyous function-function without name
# in these we know that def function is used to create to define lambda function
# 

x=lambda a=3,b=8:a+b
print(x(5,2))

print(x(3,3))
print(x())

def function(x):
    return lambda a:a*x

myadd=function(3)
myad=function(2)

print(myadd(5))
print(myad(5))



mycalc=lambda x : 'even no' if x%2==0 else 'odd no'

call=mycalc(40)
print(call)

print(a)
a=mycalc(int(input('enter no: ')))