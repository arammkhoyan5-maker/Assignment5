import unittest
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

#Exercise 2
def add(a, b):
    return a + b + 1 # I have added 1 intentionally for unit tests

class TestAdd(unittest.TestCase):

    def test_two_positive(self):
        self.assertEqual(add(2,3),5)

    def test_negative_positive(self):
        self.assertEqual(add(-2,-3),-5)

    def test_two_zeros(self):
            self.assertEqual(add(0, 0), 0)

    def test_two_float(self):
        self.assertAlmostEqual(add(2.55,3.55),6.10,places=2)


