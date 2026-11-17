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



def test_nested_if_conditions():
    """Test nested if conditions for discount eligibility."""

    # Scenario 1: Adult student qualifies for a discount
    age = 20
    is_student = True
    is_senior = False

    discount = False

    if age >= 18:
        if is_student:
            discount = True
        elif is_senior:
            discount = True

    assert discount is True

    # Scenario 2: Senior customer qualifies for a discount
    age = 65
    is_student = False
    is_senior = True

    discount = False

    if age >= 18:
        if is_student or is_senior:
            discount = True

    assert discount is True

    # Scenario 3: Regular adult does not qualify for a discount
    age = 30
    is_student = False
    is_senior = False

    discount = False

    if age >= 18:
        if is_student or is_senior:
            discount = True

    assert discount is False

    # Scenario 4: Minor student does not qualify for a discount
    age = 16
    is_student = True
    is_senior = False

    discount = False

    if age >= 18:
        if is_student or is_senior:
            discount = True

    assert discount is False
