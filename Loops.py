from decision_Making import *
#Digital root of the number
def digital_root(num):
    while(num>9):
        sum = 0
        n = num
        while(n>0):
            sum = sum + n%10
            n = n//10
        num = sum
    return num

#Prime Numbers:
def isPrime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
    return True

#Prime for given range:
def prime_number_range(a,b):
    prime_list = []
    for i in range(a,b+1):
        if isPrime(i):
            prime_list.append(i)
    return prime_list

#Sum of triangular numbers:
def triangular_num(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum = sum + j; 
    return sum

# Maximum number by deleting single digit in a 4 digit number 5872 - 872, 9865 - 985
def max_digit(n):
    l1 = []
    s = ""
    while(n>0):
        l1.append(str(n%10))
        n = n//10
    l1 = sorted(l1)
    l1 = l1[::-1]
    l1.pop()
    s = s.join(l1)
    return s

# No.of combinations for n teams to play each other, i.e. nCr
def combination(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

# Generate number triangles/pyramids, pascal triangle
def pascal_triangle(n):
    for i in range
