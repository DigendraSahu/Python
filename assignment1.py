import webcolors
#Implement Banking Account class
class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def deposit(self,a):
        self.balance += a
        return self.balance
    
    def withdrwa(self,b):
        if self.balance<=0:
            raise Exception
        self.balance -= b
        return self.balance


#Implement Mobile billing Customer class
class Mobile:
    def __init__(self, call_duration, sms_usage, service, carry_amt, addon):
        self.call_duration = call_duration            
        self.sms_usage = sms_usage              
        self.service = service      
        self.carry_amt = carry_amt  
        self.addon = addon          
        self.bill = 0               

        if self.service == 'POSTPAID':
            self.call_charges = 0.20
            self.sms_charges = 0.50
        else:
            self.call_charges = 0.75
            self.sms_charges = 1.0

    def bill_amount(self):
        self.bill += self.call_duration * self.call_charges + self.sms_usage * self.sms_charges + self.carry_amt
        if self.addon:
            self.bill = self.bill +  10
        return self.bill

#Implement IP Address as a class
class ipaddress:
    def __init__(self, int_address):
         self.address = int_address

    def address_str(self):
        s = ""
        k = 3
        while k >=0:
            s += str((self.address // pow(256, k))%256) + "."
            k -= 1

        return s[:-1]

#Implement Color as a class
class color:
    def __init__(self, hex_value):
        self.red = hex_value[0]
        self.green = hex_value[1]
        self.blue = hex_value[2]
        self.hex_value = hex_value
    
    def form_color(self):
        try:
            return webcolors.rgb_to_name(self.hex_value)
        except ValueError:
            print("Invalide color code")

#Implement Point as a class
class Point:
    def __init__(self, x, y):
        self.x = x                
        self.y = y                

    def quad(self):               
        if self.x > 0:
            if self.y > 0:
                return 1
            else:
                return 2
        else:
            if self.y > 0:
                return 3
            else:
                return 4
            
    def __str__(self):
        return f"({self.x}, {self.y})"

    def dist_origin(self):        
        return round(pow((self.x**2 + self.y**2), 0.5), 3)

#Implement Circle/Triangle/Rectangle as a class
class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return 2*3.141*self.radius
    
    def area(self):
        return 3.141 * (self.radius ** 2)

class triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
        self.s = (self.a + self.b + self.c)/2

    def area(self):
        return pow(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c), 0.5)
    
    def circumference(self):
        return self.a + self.b + self.c

class rectangle():
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def circumference(self):
        return 2 * (self.a + self.b)

#Implement Box as class
class box:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def volume(self):
        return self.length * self.breadth * self.height
    
    def display(self):
        print(f"Length = {self.length}, Breadth = {self.breadth}, Height = {self.height}")