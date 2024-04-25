from keyboard import*
##Remove the user proofing function checks that have not been added yet
class NumericConversion():
    def __init__(self):
        ## Add Ctrl C loop control (not needed)
        question = input("Enter D if you want to enter a decimal and Enter B if you want to enter a Binary code") ##checks to see if they want binary or not
        if question.isalpha() == False:
            print("You seem to have entered a input that did contain only numbers, please reopen the application and enter either B for Binary input or D for decimal input")
##            quit()
        else:
        ##WNUP(Will Need User Proofing)
            if question.upper() == "B":
                binary = input("Enter Binary")
                if len(binary) <= 15 :
                    self.binary_to_decimal(binary)
                else:
                    print("It seems you have entered a string of binary longer than 15 characters, please exit the application and redo the process")
##                    quit()
            elif question.upper() == "D":
                decimal = input("Enter a number")
                if int(decimal) <= 37268:
                    self.decimalToBinary(decimal)
                else:
                    print("It seems you have entered a number larger than 37268, please exit the application and redo the process")
##                    quit()
            else:
                print("It seems you have entered a Number or Letter that is not B or D, please exit the application and redo the process")
##                quit()
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
            print(int(digit))
        print("The decimal value is: ", decimal)
noah = 1
Noah = 1
noah = Noah
while (noah == Noah):
    numeric_conversion = NumericConversion()
