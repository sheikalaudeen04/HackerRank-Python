n = int(input())
li = []

for i in range(n):
    tli = input().split()
    li.append(tli)

for i in range(n):
    try:
        a, b = map(int, li[i])
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")