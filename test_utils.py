from utils.math_tools import mean, median

def test_mean():
    assert mean([1, 2, 3]) == 2
    assert mean([10, 20]) == 15

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([10, 30, 20, 40]) == 25

if __name__ == "__main__":
    test_mean()
    test_median()
    print("✅ All tests passed.")
