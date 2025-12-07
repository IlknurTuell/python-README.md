# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

num = int(input("How many Fibonacci numbers do you want: "))
for i in range(2,num):
    fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])

print(fibonacci_list)
print(len(fibonacci_list))