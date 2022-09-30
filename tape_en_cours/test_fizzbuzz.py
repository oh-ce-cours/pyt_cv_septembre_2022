from fizzbuzz import est_divisible_par, regle_fizzbuzz


def test_division():
    assert est_divisible_par(3, 2) == False
    assert est_divisible_par(10, 5) == True


def test_regle_fizz_buzz():
    assert regle_fizzbuzz(1) == "1"
    assert regle_fizzbuzz(3) == "fizz"
    assert regle_fizzbuzz(5) == "fizz"
    assert regle_fizzbuzz(15) == "fizzbuzz"
