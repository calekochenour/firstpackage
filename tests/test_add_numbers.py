from firstpackage.add_numbers import add_num


def test_add_numbers():
    result = add_num(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

    result2 = add_num(-1, 4)
    assert result2 == 3, f"Expected 3, but got {result2}"

    result3 = add_num(0, 0)
    assert result3 == 0, f"Expected 0, but got {result3}"