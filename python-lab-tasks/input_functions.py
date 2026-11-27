#all input functions are defined here
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")

a= int(input("Enter a number: "))
print("You entered:", a)
print("the class of a given input is:", type(a))

b= float(input("Enter a decimal number: "))
print("You entered:", b)
print("the class of a given input is:", type(b))

c= input("Enter a string: ")
print("printing the string you entered:", c)
print("the class of a given input is:", type(c))

d= float(input("what is your height in meters: "))
print("your height is", d, "meters.")
print("the class of a given input is:", type(d))   
 

#using f strings to print the output
e= input("Enter your name: ")
f= input("Enter your age: ")
print(f"Hello, {e}! You are {f} years old.")
print(f"{e} is {d} meters tall.")

