import math

def isbinary(number):
    return set(str(number)).issubset({'0', '1'})
    
def checkbase(number, base):
    valid_chars = set("0123456789ABCDEF"[:base])
    return set(number.upper()).issubset(valid_chars)
    
def decimaltobase():
    a = []
    n = int(input("\nEnter a decimal number: \n"))
    base = int(input("Enter base: \n"))
    while n != 0:
        t = n % base
        if t > 9:
            a.append(chr(t + 55))
        else:
            a.append(chr(t + 48))
        n = n // base
    print("\nNumber corresponding to this base is: ", end="")
    for i in reversed(a):
        print(i, end="")
    print()

def basetodecimal():
    a = input("\nEnter Number of that Base: ").upper()
    base = int(input("Enter Base: "))
    if not (2 <= base <= 16):
        print("\nBase should be between 2 and 16.")
        return
    if not checkbase(a, base):
        print(f"{a} is not a valid number for base {base}.")
        return
    decimal = 0
    len_a = len(a) - 1
    for char in a:
        if '0' <= char <= '9':
            val = ord(char) - 48
        elif 'A' <= char <= 'F':
            val = ord(char) - 65 + 10
        decimal += val * (base ** len_a)
        len_a -= 1
    print(f"Decimal number = {decimal}")

def binarytooctal():
    num = input("\nEnter the Binary number to convert to Octal: ")
    if not isbinary(num):
        print(f"{num} is not a binary number.")
        return
    n = int(num, 2)
    octal = ''
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    print(f"Octal number = {octal}")

def binarytohexa():
    num = input("\nEnter the Binary number to convert to Hexadecimal: ")
    if not isbinary(num):
        print(f"{num} is not a binary number.")
        return
    n = int(num, 2)
    hexadecimal = ''
    while n > 0:
        rem = n % 16
        if rem < 10:
            hexadecimal = chr(48 + rem) + hexadecimal
        else:
            hexadecimal = chr(55 + rem) + hexadecimal
        n //= 16
    print(f"Hexadecimal number = {hexadecimal}")
    
def octaltobinary():
    n = int(input("\nEnter the Octal number to convert to Binary\n"))
    p = 0
    i = 0
    while n != 0:
        q = n % 10
        n = n // 10
        p += q * (8 ** i)
        i += 1
    a = []
    while p > 1:
        s = p % 2
        a.append(s)
        p //= 2
    a.append(1)
    print("The binary num is: ", end="")
    for bit in reversed(a):
        print(bit, end="")
    print()

def octaltohexa():
    n = int(input("\nEnter the Octal number to convert in Hexadecimal\n"))
    p = 0
    i = 0
    while n != 0:
        q = n % 10
        n = n // 10
        p += q * (8 ** i)
        i += 1
    a = []
    while p != 0:
        s = p % 16
        if s < 10:
            a.append(chr(48 + s))
        else:
            a.append(chr(55 + s))
        p //= 16
    print("The Hexadecimal number is: ", end="")
    for char in reversed(a):
        print(char, end="")
    print()

def hexatobinary():
    a = input("\nEnter any Hexadecimal number to convert into binary \n")
    p = 0
    len_a = len(a) - 1
    for char in a:
        if '0' <= char <= '9':
            val = ord(char) - 48
        elif 'A' <= char <= 'F':
            val = ord(char) - 65 + 10
        p += val * (16 ** len_a)
        len_a -= 1
    a1 = []
    while p > 1:
        s = p % 2
        a1.append(s)
        p //= 2
    a1.append(1)
    print("The binary number is: ", end="")
    for bit in reversed(a1):
        print(bit, end="")
    print()

def hexatooctal():
    hex_num = input("\nEnter any Hexadecimal number to convert into Octal \n")
    p = 0
    len_hex = len(hex_num) - 1
    for char in hex_num:
        if '0' <= char <= '9':
            val = ord(char) - 48
        elif 'A' <= char <= 'F':
            val = ord(char) - 65 + 10
        p += val * (16 ** len_hex)
        len_hex -= 1
    a = []
    while p > 1:
        s = p % 8
        a.append(s)
        p //= 8
    print("The Octal number is: ", end="")
    for digit in reversed(a):
        print(digit, end="")
    print()

def main():
    while True:
        print("Enter 1 to convert Decimal to Any base")
        print("Enter 2 to convert Any base to decimal")
        print("Enter 3 to convert Binary to Octal")
        print("Enter 4 to convert Binary to Hexadecimal")
        print("Enter 5 to convert Octal to Binary")
        print("Enter 6 to convert Octal to Hexadecimal")
        print("Enter 7 to convert Hexadecimal to Binary")
        print("Enter 8 to convert Hexadecimal to Octal")
        choice = int(input("\nEnter Your Choice : "))
        if choice == 1:
            decimaltobase()
        elif choice == 2:
            basetodecimal()
        elif choice == 3:
            binarytooctal()
        elif choice == 4:
            binarytohexa()
        elif choice == 5:
            octaltobinary()
        elif choice == 6:
            octaltohexa()
        elif choice == 7:
            hexatobinary()
        elif choice == 8:
            hexatooctal()
        cont = input("\nDo you want to continue? \nPress 'Y' for Yes \nPress 'N' for No\n\n")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()




