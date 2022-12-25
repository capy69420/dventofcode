
def snafu_to_decimal(snafu):
    # Split the SNAFU number into its individual digits
    digits = list(snafu)
    
    # Assign each digit a place value based on powers of 5
    place_values = [5**i for i in range(len(digits)-1, -1, -1)]
    
    # Multiply each digit by its place value and sum the results
    decimal_equivalent = sum(place_values[i] * int(digits[i]) if digits[i].isdigit() else place_values[i] * -1 if digits[i] == '-' else place_values[i] * -2 for i in range(len(digits)))
    
    return decimal_equivalent

def decimal_to_snafu(decimal):
    # Initialize the SNAFU number as an empty string
    snafu = ''
    # Residual for remainder 3 and 4 conversion
    res = 0
    # Divide the decimal number by 5
    # Repeat the process with the quotient
    # Continue until the quotient is 0
    while decimal > 0:
        # Divide the decimal number by 5 and find the remainder, quotient
        # decimal = quotient * 5 + remainder
        quotient, remainder = divmod(decimal, 5)
        # add the residue from the last digit to the remainder
        remainder += res
        res = 0
        # Convert the remainder to its SNAFU digit and add it to the SNAFU number
        if remainder == 0:
            snafu = '0' + snafu
        elif remainder == 1:
            snafu = '1' + snafu
        elif remainder == 2:
            snafu = '2' + snafu
        elif remainder == 3:
            res = 1
            snafu = '=' + snafu
        elif remainder == 4:
            res = 1
            snafu = '-' + snafu

        # Update the decimal number with the quotient
        decimal = quotient
    
    # If the SNAFU number is empty, return '0'
    if snafu == '':
        return '0'
    
    return snafu

decimals = []
with open('input25.txt', 'r') as f:
    for line in f:
        # convert from SNAFU to dec add them to the list
        snafu = line.strip()
        dec = snafu_to_decimal(snafu)
        decimals.append(dec)
    # get the decimal sum
    sum = 0
    for d in decimals:
        sum += d
    print('Decimal sum:',sum)
    print('SNAFU:',decimal_to_snafu(sum))
    