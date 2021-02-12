#Biggest of three
def biggest_of_three(a,b,c):
    return max(a,b,c)

# Armstrong Number
def armstrong(n):
    m = n
    digit = int(len(str(n)))
    sum = 0
    while(n>0):
        sum = sum + (n%10)**digit
        n = n//10
    if sum == m:
        return True
    else:
        return False

# Reverse the number
def rev_number(n):
    rev = 0
    while(n>0):
        rev = rev + n%10
        rev = rev*10
        n = n//10
    return rev//10

# Sum of Digit
def sum_of_digit(n):
    sum = 0
    while(n>0):
        sum = sum + n%10
        n = n//10
    return sum

#GCD/HCF of number
def gcd(a,b):
    if(a==0 and b==0):
        return 0
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return b
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

#LCM of the number
def lcm(a,b):
    large_num = max(a,b)
    small_num = min(a,b)
    i = large_num
    while(True):
        if(i%small_num==0):
            return i
        i+=large_num

#Leap year or not:

def leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        return True
    else:
        return False

#Type of triangle
def triangle_type(a,b,c):
    if((a**2 == (b**2 + c**2)) or (b**2 == (a**2 + c**2)) or (c**2 == (a**2 + b**2))):
        return "Right angle"
    elif(a==b==c):
        return "Equilateral"
    elif(a!=b!=c):
        return "Scalene"
    elif((a==b and a!=c) or (b==c and c!=a) or (a==c and a!=b)):
        return "isosceles"

#Roots of quadratic equation
def quad_root(a,b,c):
    if(a!=0):
        d = b**2 - 4*a*c
        if(d>=0):
            root1 = (-b + d**0.5)/2*a
            root2 = (-b - d**0.5)/2*a
            return int(root1),int(root2)
        else:
            return "Roots of equation are not real"

#Quadrants of the given point
def quadrants(a,b):
    if(a>0 and b>0):
        return 1
    elif(a<0 and b<0):
        return 3
    elif(a>0 and b<0):
        return 4
    elif(a<0 and b>0):
        return 2
    elif(a==0 and b==0):
        return 0

#Choice based arithmetic
def arithmetic(a,b,choice):
    if(choice=='+'):
        return a+b
    if(choice=='-'):
        return a-b
    if(choice=='/'):
        return a//b
    if(choice=='*'):
        return a*b
    else:
        return "Invalid Choice"

# Factorial of the given number
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#fibonacci series
def fibonacci(n):
    res = []
    first_num = 0
    second_num = 1
    i = 0
    while(i<n):
        if(i<=0):
            next = 1
        else:
            next = first_num + second_num
            first_num = second_num
            second_num = next
        res.append(next)
        i += 1
    return res
        
def tribonacci(n):
    res = []
    first_num = 0
    second_num = 0
    third_num = 1
    i = 0
    while(i<n):
        if(i<=1):
            next = i
        else:
            next = first_num+second_num+third_num
            first_num = second_num
            second_num = third_num
            third_num = next
        res.append(next)
        i+=1
    return res

# sum of factors
def sum_of_factors(n):
    l1 = []
    for i in range(1,n+1):
        if(n%i == 0):
            l1.append(i)
    return sum(l1)

#Vowel or consonant
def vowel_or_consonant(character):
    vowel = ['a','e','i','o','u']
    if character.isalpha():
        if(character.lower() in vowel):
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "invalid input"
