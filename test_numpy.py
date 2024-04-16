import numpy as np

def test_numpy():
    # Check if NumPy is installed
    try:
        # Create a simple array
        arr = np.array([1, 2, 3])
        # Check if array creation is successful
        assert np.array_equal(arr, np.array([1, 2, 3])), "NumPy array creation failed"
        print("NumPy is installed and working correctly.")
    except ImportError:
        print("NumPy is not installed.")
    except AssertionError as e:
        print(str(e))

if __name__ == "__main__":
    test_numpy()
