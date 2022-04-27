class MathLibrary:

    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b

    def divide(a,b):
        #add division of 0 exception
        return a/b

    def multiply(a,b):
        return a*b

    def fact(a):
        #fix negative values and decimal
        if a == 1:
            return a
        elif a==0:
            return 1
        else:
            return a*MathLibrary.fact(a-1)

    def root(a,b):
        #add negative values exception
        return a**(1/b)

    def power(a,b):
        return a**b

#print(MathLibrary.power(4,3))