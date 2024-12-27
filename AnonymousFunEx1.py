#program for cal addition of two numbers by using anonymous
#anonymousfunex1.py
def sumop(a,b):
    return a+b
addop=lambda k,v : k+v # anonymous function defition



#main program
res=sumop(10,20) # normal function call
print("type of sumop=",type(sumop))
print("sum by using normal func=",res)
print("----------------------------------")
print("enter two values for addition")
a,b=float(input()),float(input())
res1=addop(a,b) # anonymous function call
print ("type of addop=",type(addop))
print ("sum by using anonymous function=",res1)

