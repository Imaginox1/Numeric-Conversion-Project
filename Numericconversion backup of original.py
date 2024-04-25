from keyboard import*
class NumericConversion():
    def __init__(self):
        ## Add Ctrl C loop control (not needed)
        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code") ##checks to see if they want binary or not
        if isalpha(question) == True:
            print("You seem to have entered a input that did contain only numbers, please reopen the application and enter either B for Binary input or D for decimal input")
            quit()
        else:
        ##WNUP(Will Need User Proofing)
            if upper(question) == "B":
                binary = input("Enter Binary Code")
                if ##isitBinary(binary) == True:
               decimaltoBinary()
                else:
                    print("it seems that you have entered a number that isn't Binary, remeber Binary is 15 0s that can be replaced with 1s to make a number") 
                    quit()
            else:
                print("It seems you have entered a Number or Letter that is not B or D, please exit the application and redo the process")
                quit()
            if upper(question) == "D":
                decimal = input("Enter decimal Code")
                if ##isitDecimal(decimal) == True            
                ##WNUP
                binary_to_decimal()
                else:
                    print("It seems you have forgotten to enter a number, Please reopen the application and enter a number that ranges from 0-128")
                    quit()
            else:
                print("It seems you have entered a Number or Letter that is not B or D, please exit the application and redo the process")
                quit()
    # this program will convert a decimal number to a binary one
    def decimalToBinary(self, decimal):
        # creates an empty list to store the new numbers 
        a = []
        # sets the loop to repeat untill the number is zero 
        while decimal != 0:
            # remanders the number by 2 and adds it to the list 
            a.append(decimal % 2)
            # intiger divides the number 
            decimal //= 2
        #reverses the list 
        a.reverse()
        #converts the list to string and returns it 
        return ''.join(map(str,a))
    def binary_to_decimal(self, binary):
##        binary = input("Enter a binary number: ")
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        print("The decimal value is: ", decimal)
numeric_conversion = NumericConversion()
