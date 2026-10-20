
print("===== DECIMAL TO BINARY CONVERTER =====")

while True:
    decimal = int(input("Enter a decimal number: "))

    number = abs(decimal)
    binary = ""

    if number == 0:
        binary = "0"
    else:
        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2

    if decimal < 0:
        binary = "-" + binary

    print("Binary number:", binary)

    again = input("Do you want to convert another number? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using Binary Converter!")
        break
