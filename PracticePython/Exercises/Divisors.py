#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

number = int(input("Please enter a number: "))
y = []
for num in list(range(1,number+1)):
    if number%num==0:
        y.append(num)

print(y)