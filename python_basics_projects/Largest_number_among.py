#python codes to find the largest number amaong the three input numbers

#Get three input numbers from the user
num1 = float(input("Enter the first number1: "))
num2 = float(input("Enter the first number2: "))
num3 = float(input("Enter the first number3: "))

# Checking for the largest number
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif(num2 >= num1) and (num2 >= num3):
    largest = num2
else:
     largest = num3
print("The largest number is ", largest)    
        