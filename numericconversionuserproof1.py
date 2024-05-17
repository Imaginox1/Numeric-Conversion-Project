class NumericConversion():
    def __init__(self):
        ## Add Ctrl C loop control (not needed)
##        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code") ##checks to see if they want binary or not
##        if question.isalpha() == False:
##            print("You seem to have entered a input that did contain only numbers, please reopen the application and enter either B for Binary input or D for decimal input")
##        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code and with the binary or decimal code depeding on what you want to convert"
##                     + 'For exmaple to convert 762 to binary D762') ##checks to see if they want binary or not   
##        question = input("This is a binary to decimal, and a decimal to binary converter.\n" +
##                         "If you want to convert a decimal number to a binary number, add a D to the beginning of your input.\n" +
##                         "For example D762. If you want to convert a binary number to a decimal number, add a B to the beginning of your input, For example B10011.\n" +
##                         "What number would you like to convert:") 
        question = input("Enter D if you want to convert from decimal to binary. Enter B if you would like to convert from binary to decimal.\n" +
                         "For example D762. If you want to convert a binary number to a decimal number, add a B to the beginning of your input, For example B10011.\n" +
                         "What number would you like to convert:")
        det = question[:1]
        inputs = question[1:]
##            quit()
        if (len(question) > 16) == False and det.isalpha() == True and inputs.isdigit() == True:
            if det.upper() == "B":
##                binary = input("Enter Binary")
                if len(inputs) <= 15 and self.isitBinary(inputs) == True:
                    self.binary_to_decimal(inputs)
                else:
                    print("\nIt seems you have entered a binary number longer than 15 characters, or you have entered a binary number that does not only contain 1's and 0's.\nPlease try again.")
##                    quit()
            elif det.upper() == "D":
##                decimal = input("Enter a number")
                if int(inputs) <= 37268 or self.isitDecimal(inputs) == True:
                    self.decimalToBinary(inputs)
##                    print(''.join(map(str,a)))
                else:
                    print("It seems you have entered a number larger than 37268, or you have entered something that is not a decimal.\nPlease try again.")
##                    quit()
            else:
                print("It seems you have entered a number or letter that is not B or D, please exit the application and redo the process.\nPlease try again.")
##                quit()
        else:
        ##WNUP(Will Need User Proofing)
            print("\nInputs that are longer than 6 characters, don't start with D or B, do not include numbers, or have numbers located in the wrong area are not allowed.\nPlease try again.")
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
        outputs = ''.join(map(str,a))
        print("The binary value is:", outputs)
        return ''.join(map(str,a))
    def binary_to_decimal(self, inputs):
##        binary = input("Enter a binary number: ")
        decimal = 0
        for digit in inputs:
            decimal = decimal*2 + int(digit)
##            print(int(digit))
        print("The decimal value is:", decimal)
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
noah = Noah
print("Rules: \n 1.If you are putting in a decinmal to be converted to Binary, the Decimal input cannot be longer than 5 characters and no greater than 37268\n" +
      "2.If you are putting in a Binary input to be converted to Decimal, The Binary input cannot be longer than 15 characters\n" +
      "3.Only D and B are allowd before the numbers")
while (noah == Noah):
    try:
        numeric_conversion = NumericConversion()
    except ValueError:
        numeric_conversion = NumericConversion()

