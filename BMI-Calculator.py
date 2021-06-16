Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
print("Welcome to my Programme..")
time.sleep(2)
print("In this you will be able to calculate your BMI..")
time.sleep(5)
weight = input("Enter your Weight(in Kg):-")
time.sleep(1)
height = input("Enter your Height(in cm):-")
x = float(height)/100
y = x**2
BMI = (int(weight)/y)
time.sleep(1)
print("Your BMI is ",BMI)
time.sleep(2)
print("Now this Programme will tell what is the status of your BMI after observing your BMI ")
time.sleep(5)
print("Loading..")
time.sleep(2)
if BMI < 18.5 :
    print("You are Underweight\n You need more nutrition")
elif 18.5 <= BMI < 25 :
    print("Your BMI is normal ")
elif 25 <= BMI < 30 :
    print("You are overweight")
elif BMI > 30:
    print("You have Obesity")
time.sleep(2)
print("Thank You for using my Programme..\nMade By Rohan Arora")

