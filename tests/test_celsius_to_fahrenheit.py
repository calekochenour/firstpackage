from pytest import approx

from firstpackage.temperature import celsius_to_fahrenheit


def test_celsius_to_fahrenheit():
    """
    Test the celsius_to_fahrenheit function.
    """
    # Test with freezing point of water
    assert approx(celsius_to_fahrenheit(0), abs=0.01) == 32.0

    # Test with boiling point of water
    assert approx(celsius_to_fahrenheit(100), abs=0.01) == 212.0

    # Test with a negative temperature
    assert approx(celsius_to_fahrenheit(-40), abs=0.01) == -40.0
