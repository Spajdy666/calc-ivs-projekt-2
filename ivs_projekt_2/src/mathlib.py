import math
    
class MathLibrary:
    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b

    def divide(a,b):
        #add division of 0 exception
        if b==0:
            raise ValueError("Can not divide with zero.")
        return a/b

    def multiply(a,b):
        return a*b

    def fact(a):
        #fix negative values and decimal
        if a%1!=0:
            raise ValueError("Factorial must be natural number")
        if a<0:
            raise ValueError("Factorial value must be greater than 0.")
        if a==0:
            return 1
        fact=1
        for i in range(1,a+1):
            fact*=i
        
        return fact
            
    def root(a,b):
        if b%1!=0:
            raise ValueError("Exponent must be natural number")
        if b<=0:
            raise ValueError("Exponent must be greater than 0.")
        if a<0 and b%2==0:
            raise ValueError("%dth root must have a positive value",b)
        if a<0:
            a=abs(a)
        return a**(1/b)

    def power(a,b):
        if b%1!=0:
            raise ValueError("Exponent must be natural number")
        if b<0:
            raise ValueError("Exponent must be greater than 0.")
        return a**b
    
    def ln(a):
        if a<0:
            raise ValueError("Number must be higher than 0")
            return
        return math.log(a)