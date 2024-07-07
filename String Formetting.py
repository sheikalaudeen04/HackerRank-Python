def print_formatted(number):
    width = len(bin(n))-2
    for i in range(1,n+1):
        Decimal = f"{i:>{width}d}"
        Octal = f"{oct(i)[2:]:>{width}}"
        Hexadecimal = f"{hex(i)[2:].upper():>{width}}"
        Binary = f"{bin(i)[2:]:>{width}}"
        print(Decimal+' '+Octal+' '+Hexadecimal+' '+Binary)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)