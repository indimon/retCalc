from pytest_bdd import scenario, parsers, given, when, then

from main import main, getretirementage


# Scenario number 1

@scenario('/Users/JBAnderson/PycharmProjects/retirementCalc/tests/features/gerkin.feature',
          'The user was born before 1900')
def test1():
    pass


@given(parsers.cfparse('the user inputs their birth year of "{year:Number}" and birth month of "{month:Number}"',
                       extra_types=dict(Number=int)))
def birthday(year, month):
    return getretirementage(year=year, month=month)


@when('the birth year is before 1938')
def assertyear(year):
    if year < 1938:
        assert "true"
    else:
        assert "false"


@then('the retirement age will be 65 years old')
def retirementage(retage):
    assert retage == 65


# Scenario number 3

@scenario('/Users/JBAnderson/PycharmProjects/retirementCalc/tests/features/gerkin.feature',
          'The user was born in 1950')
def test3():
    pass


@given(parsers.cfparse('the user inputs their birth year of "{year:Number}" and birth month of "{month:Number}"',
                       extra_types=dict(Number=int)))
def birthday3(year, month):
    return getretirementage(year=year, month=month)


@when('the birth year is between 1942 and 1955 and the month is calculated')
def assertyear3(year, month):
    if 1942 > year < 1955:
        assert "true"
    else:
        assert "false"


@then('the retirement age will be 66 years old')
def retirementage3(retage):
    assert retage == 66