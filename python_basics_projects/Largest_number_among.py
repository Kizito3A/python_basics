#python codes to find the largest number amaong the three input numbers

#Get three input numbers from the user
num1 = float(input("Enter the first number1: "))
num2 = float(input("Enter the first number2: "))
num3 = float(input("Enter the first number3: "))

# Checking for the largest number
if (num1 > num2) and (num1 > num3):
    print("Num1 is the largest")
elif(num2 > num1) and (num2 > num3):
    print("Num2 is the largest")
else:
    print("Num3 is the largest")    
        