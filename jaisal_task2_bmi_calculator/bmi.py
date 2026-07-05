"""
bmi.py
---------
Contains all BMI calculation related functions.
"""


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI)

    Formula:
        BMI = Weight (kg) / Height² (m²)

    Returns:
        float : BMI rounded to 2 decimal places
    """

    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    """
    Returns the BMI Category.
    """

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def bmi_color(category):
    """
    Returns a color based on BMI category.
    Used for displaying the result in the GUI.
    """

    colors = {
        "Underweight": "blue",
        "Normal Weight": "green",
        "Overweight": "orange",
        "Obese": "red"
    }

    return colors.get(category, "black")