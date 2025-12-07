#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Extras:
# If the number is a multiple of 4, print out a different message.

number = int(input("Please enter a number: "))
if number%4==0:
    print(number,"is a multiple of 4.")
if number%2 ==0:
    print(f"The number is an even number.")
else:
    print(f"The number is an odd number.")










