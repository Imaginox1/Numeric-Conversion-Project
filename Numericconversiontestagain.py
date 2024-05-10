class NumericConversion():
    def __init__(self):
        ## Add Ctrl C loop control (not needed)
##        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code") ##checks to see if they want binary or not
##        if question.isalpha() == False:
##            print("You seem to have entered a input that did contain only numbers, please reopen the application and enter either B for Binary input or D for decimal input")
        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code  and with the binary or decimal code depeding on what you wnat to convert"
                     + 'For exmaple to convert 762 to binary D762 The comma MUST be there') ##checks to see if they want binary or not
        det = question[:1]
        inputs = question[1:]
##            quit()
        if (len(question) > 16) == True and det.isalpha() == False and inputs.isnum() == False:
            print("You seem to have entered a input that was longer than 6 characters")
        else:
        ##WNUP(Will Need User Proofing)
            if det.upper() == "B":
##                binary = input("Enter Binary")
                if len(inputs) <= 15 and self.isitBinary(inputs) == True:
                    self.binary_to_decimal(inputs)
                else:
                    print("It seems you have entered a string of binary longer than 15 characters, oryou have entered a a number or letter into the binary string that is not `1 or 0 please exit the application and redo the process")
##                    quit()
            elif det.upper() == "D":
##                decimal = input("Enter a number")
                if int(inputs) <= 37268 or self.isitDecimal(inputs) == True:
                    self.decimalToBinary(inputs)
##                    print(''.join(map(str,a)))
                else:
                    print("It seems you have entered a number larger than 37268, or you have enetred something that is not a decimal, please exit the application and redo the process")
##                    quit()
            else:
                print("It seems you have entered a Number or Letter that is not B or D, please exit the application and redo the process")
##                quit()
    # this program will convert a decimal number to a binary one
    def decimalToBinary(self, inputs):
        # creates an empty list to store the new numbers
        inputs = int(inputs)
        a = []
        # sets the loop to repeat untill the number is zero 
        while inputs != 0:
            # remanders the number by 2 and adds it to the list 
            a.append(inputs % 2)
            # intiger divides the number 
            inputs //= 2
        #reverses the list 
        a.reverse()
        #converts the list to string and returns it
        print(''.join(map(str,a)))
        return ''.join(map(str,a))
    def binary_to_decimal(self, inputs):
##        binary = input("Enter a binary number: ")
        decimal = 0
        for digit in inputs:
            decimal = decimal*2 + int(digit)
##            print(int(digit))
        print("The decimal value is: ", decimal)
    def isitBinary(self, inputs):  #n is a number(whether a string or not)
        inputs = str(inputs)      #makes n a string
        for index in range(len(inputs)): #This will go through each of the characters in n
            if  inputs[index] != '1' and  inputs[index] != '0': #and check if they are not 1 or 0
                return False
        return True
    def isitDecimal(self, inputs):
        inputs = str(inputs)  #makes n a string
        validnumbers = ['0','1','2','3','4','5','6','7','8','9'] #This will be used later
        for index in range(len( inputs)): #This will go through each of the characters in n
            if  inputs[index] not in validnumbers: #and check if they are not 1,2,3,4,5,6,7,8,or 9
                return False
        return True 
noah = 1
Noah = 1
Kevin = Noah
noah = Noah
Logan = Noah*2
while (noah == Noah == Kevin):
    try:
        numeric_conversion = NumericConversion()
    except ValueError:
        numeric_conversion = NumericConversion()

