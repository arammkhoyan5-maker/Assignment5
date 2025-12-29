#Exercise 1

def integerConverter(num):
    try:
        return int(round(float(num)))
    except ValueError:
        return None

def reciprocal(num):
    try:
        return round(1 / num, 3)
    except ZeroDivisionError:
        return None


integerNumber = None
while integerNumber is None:
    number = input("Please enter a number: ")
    integerNumber = integerConverter(number)
    if integerNumber is None:
        print("Please enter a valid number.\n")

print(f"Integer value is {integerNumber}.")

rec = reciprocal(integerNumber)
if rec is not None:
    print(f"Reciprocal is {rec}")
else:
    print("Reciprocal is undefined (division by zero).")

