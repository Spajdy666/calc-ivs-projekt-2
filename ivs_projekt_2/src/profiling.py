#TODO
from mathlib import MathLibrary
import sys

def getNumbersFromStdin():
    numlist = []
    sum=0
    count=0
    for line in sys.stdin:
        #sys.stdout.write(line)
        numbers=line.split()
        for num in numbers:
            #print(j)
            sum=MathLibrary.add(float(sum), float(num))
            numlist.append(num)
            count+=1
        
    return sum,count,numlist

def averageValue(sum,count):
    return MathLibrary.divide(float(sum), int(count))

def distancesSum(avrg,numlist):
    sum=0
    for num in numlist:
        #print(num)
        diff=MathLibrary.subtract(float(num), float(avrg))
        pow=MathLibrary.power(float(diff), 2)
        sum=MathLibrary.add(float(sum), float(pow))
        #print(sum)
    
    return sum

def getStdDeviation():
    sum,count,numlist=getNumbersFromStdin()
    avrg=averageValue(sum,count)
    sum=distancesSum(avrg, numlist)
    avrg=averageValue(sum, count)
    deviation=MathLibrary.root(avrg, 2)
    return deviation

if __name__ == '__main__':
    print(getStdDeviation())