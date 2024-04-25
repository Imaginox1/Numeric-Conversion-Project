def binary_to_decimal(self, binary):
    binary = input("Enter a binary number: ")
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
        print(int(digit))
    print("The decimal value is: ", decimal)
