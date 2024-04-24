# this program will convert a decimal number to a binary one


def decimalToBinary(decimal):'
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


decimalToBinary()






        
