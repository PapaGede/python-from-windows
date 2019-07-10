# import math
# radi=int(input("Please enter your radius \n"))
# print("You entered: " ,radi)
# surfaceArea= 4*math.pi*math.pow(radi,2)
# print("The surface area of the sphere is: ",surfaceArea)
# print("\n")
# volume= (4/3)*math.pi*math.pow(radi,3)
# print("The Volume of the sphere is: ",volume)

# import datetime
# print(datetime.datetime.now())

# sentence= "The Big Brown Fox Jumps Over The Lazy Dog"
# print(sentence.split())

# a="You are"
# b=" not okay"
# print(a+b)

# string=['The boy is',' not okay']
# print(''.join(string))


# x=int(input("Please enter the first number \n"))
# y=int(input("Please enter the second number \n"))
# word=input("Enter what the operation you want to perform on these two numbers \n")

# if word=="add":
#     result= x + y
#     print(result,"\n")    
# elif word=="subtract":
#     result= x - y
#     print(result,"\n")
# elif word=="multiply":
#     result= x * y
#     print(result,"\n")        
# elif word=="divide":
#     result= x / y
#     print(result,"\n")

def calculate(x,y,word):
    if word=="add":
        result= x + y
        # print(result,"\n")
    elif word=="subtract":
        result= x - y
        # print(result,"\n")
    elif word=="multiply":
        result= x * y
        # print(result,"\n")        
    elif word=="divide":
        result= x / y
        # print(result,"\n")
    else:
        print("Error")        
    return result

x=int(input("Please enter the first number \n"))
y=int(input("Please enter the second number \n"))
word=input("Enter what the operation you want to perform on these two numbers \n")
print(calculate(x,y,word))
