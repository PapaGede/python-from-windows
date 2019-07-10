print("Hi Welcome to Even/Odd guessing game \n")
x=int(input("Please enter a number to check if it's an odd or even number \n"))
print("You entered: " ,x)
if x%2==0:
    print(x, " is an even number \n")
else:
    print(x, "is an odd number \n")    
if x%4==0:
    print(x," is a multiple of 4 \n")
else:
    print(x," is not a multiple of 4 \n")    

num=int(input("please enter dividend \n"))
check=int(input("please enter divisor \n")) 

if num%check==0:
    print(num, " is a factor of ",check)
else:   
    print(num, " is not a factor of ",check)