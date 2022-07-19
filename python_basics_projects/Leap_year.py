#python program to check if year is leap year or not
#get input from the user

year = int(input("Enter the year to check: "))

#Divided by 100 means century year(year that ends with 00)
##Divided by 400 means century year(year that ends with 00)
if(year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year". format(year))

elif(year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year". format(year))
    
#if not divided by 100 (century year) and not divided by 4 (non century year)  
    
else:
    print("{0} is not a leap year". format(year))    