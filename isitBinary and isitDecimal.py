#4/23/2024
#Russell Kinnear

#defining the isitBinary function
def isitBinary(n):  #n is a number(whether a string or not)
    n = str(n)      #makes n a string
    for index in range(len(n)): #This will go through each of the characters in n
        if n[index] != '1' and n[index] != '0': #and check if they are not 1 or 0
            return False
    return True

#defining the isitDecimal funtion
def isitDecimal(n):
    n = str(n)  #makes n a string
    validnumbers = ['0','1','2','3','4','5','6','7','8','9'] #This will be used later
    for index in range(len(n)): #This will go through each of the characters in n
        if n[index] not in validnumbers: #and check if they are not 1,2,3,4,5,6,7,8,or 9
            return False
    return True 
    

