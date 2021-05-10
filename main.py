"""Task 1"""

lis = [12, 13, 14, 15]


def oops() -> int:
    return lis[5]


def exept():
    try:
        print(oops())
    except IndexError:
        return "Ooops"


print(exept())

"""Task2"""


def calc():
    while True:
        try:
            a = int(input("Enter a:"))
            b = int(input("Enter b:"))
            c = a ** 2 / b
            return c
        except ValueError:
            print("Введите числа")
        except Exception as e:
            print("Делить на ноль нельзя")
            print(e)
print(calc())