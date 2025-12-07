#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.)

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2,int(number**0.5)+1):
        if number % divisor==0:
            return False
    return True
def get_divisors(number):
    divisors = []

    for divisor in range(1,number+1):
        if number%divisor==0:
            divisors.append(divisor)
    return divisors


n = int(input("Enter a number: "))
if is_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")

print("Divisors: ", get_divisors(n))