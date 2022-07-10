import time


# converter function(binary to decimal)
def convert_bin_to_decimal(code):
    octet = [128, 64, 32, 16, 8, 4, 2, 1]
    decimal_code = []

    # going through octets
    for n, x in enumerate(code.split(".")):
        one_octet = 0

        # operation i using to divide octets with dots(".")
        if n != 0:
            decimal_code.append(".")
        # going through every octet character
        for index, i in enumerate(x):
            # checking for content(if we have 1 we're adding value to result)
            if int(i):
                one_octet += octet[index]
        # adding octet to the main result( now it is just list)
        decimal_code.append(one_octet)

    # converting list to line
    result = "".join(str(x) for x in decimal_code)
    # outputting result to console
    print(f"Here it is:")
    print(result)
    time.sleep(5)

    # restart
    main()


# converter function(decimal to binary)
def convert_decimal_to_bin(code):
    octet = [128, 64, 32, 16, 8, 4, 2, 1]
    bin_code = []

    # going through octets
    for n, x in enumerate(code.split(".")):
        x = int(x)

        # operation i using to divide octets with dots(".")
        if n != 0:
            bin_code.append(".")
        # going through 8 octets values
        for i in octet:
            # actually process of converting to 1 or 0
            if x >= i:
                x -= i
                bin_code.append(1)
            else:
                bin_code.append(0)

    # full result in line
    result = "".join(str(x) for x in bin_code)

    # outputs the result to console
    print("Here it is:")
    print(result)
    time.sleep(5)

    # restart
    main()


# simple check on the users inf(if it is correct)
def check_inf(x):
    opt = {1: "bin",
           2: "decimal"
           }
    if x.isnumeric() and int(x) in opt.keys():
        return x

    # in case of error restart
    else:
        print("Enter valid information:)")
        time.sleep(3)
        print("\n")
        print("\n")
        print("\n")

        main()


# actually console interface
def get_inf():
    print("Welcome to IP converter")
    choose = input("1(bin to decimal), 2(decimal to bin)\n"
                   "Enter what you want to do: "
                   )

    check_inf(choose)

    print("\n")

    code = input("Enter your IP(make sure to enter code with '.dots' between octets): ")

    print("\n")

    return choose, code


# making choose of the converter(depends on user info)
def select_converter(choose, code):

    if int(choose) == 1:
        convert_bin_to_decimal(code)
    elif int(choose) == 2:
        convert_decimal_to_bin(code)


# stating the program
def main():
    while True:
        choose, code = get_inf()

        select_converter(choose, code)


if __name__ == "__main__":
    main()
