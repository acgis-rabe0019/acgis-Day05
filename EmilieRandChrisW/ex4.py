#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     03-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
#the 4 lowest numbers that run the below code are are: 1, 2, 3, 12

if __name__ == '__main__':
    main()

def whatIsMyVar(myVar):
    if myVar % 2:
        if myVar **3 !=27:
            myVar = myVar+4
            return myVar
        else:
            myVar/=1.5
            return myVar
    else:
        if myVar <=10:
            myVar *= 2
            return myVar
        else:
            myVar -=2
            return myVar

def test_whatIsMyVar():
    print "Expect: 5 Actual: " + str(whatIsMyVar(1))
    print "Expect: 4 Actual: " + str(whatIsMyVar(2))
    print "Expect: 2.0 Actual: " + str(whatIsMyVar(3))
    print "Expect: 10 Actual: " + str(whatIsMyVar(12))

test_whatIsMyVar()
if __name__ == '__main__':
    main()
