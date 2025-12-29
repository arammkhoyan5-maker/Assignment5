# Exercise 3
# super_confusing_code.py

def valueCollector(grades):
    """
    Collects 5 new grades from the user and appends them to the given list.

    :param grades: list of floats
    :return: list of floats including the newly added grades
    """
    for n in range(5):
        grade = float(input("Import the grade: "))
        grades.append(grade)
    return grades


def averageCalculator(grades):
    """
    Calculates the average of a list of numbers.

    :param grades: list of floats
    :return: float, the average of the numbers in the list
    """
    t = 0
    for j in range(len(grades)):
        t += grades[j]
    return t / len(grades)


def run(grades):
    """
    Collects grades, calculates the average, and prints the result.

    :param grades: list of floats
    :return: None
    """
    grade_list = valueCollector(grades)
    average = averageCalculator(grade_list)
    print(f"The average is: {average}")


grades = []
run(grades)