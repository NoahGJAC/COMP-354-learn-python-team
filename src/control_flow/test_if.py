"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'



def test_multiple_elif_conditions():
    """Demonstrate multiple elif conditions"""

    grade = 85
    result = ''

    if grade >= 90:
        result = 'Excellent'
    elif grade >= 80:
        result = 'Very Good'
    elif grade >= 70:
        result = 'Good'
    elif grade >= 60:
        result = 'Pass'
    else:
        result = 'Fail'

    assert result == 'Very Good'


def test_nested_if_conditions():
    """Test nested if conditions for discount eligibility."""

    age = 20
    is_student = True
    is_senior = False

    discount = False

    if age >= 18:
        if is_student or is_senior:
            discount = True

    assert discount is True

    # Test discount eligibility for senior customers
    age = 65
    is_student = False
    is_senior = True

    discount = False

    if age >= 18:
        if is_student or is_senior:
            discount = True

    assert discount is True
