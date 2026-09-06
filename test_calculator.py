from calculator import square 

def main():
    testsquare(5)
    
    
def testsquare(x):
    assert square(x) == x * x, f"Expected {x * x}, but got {square(x)}" #This command uses an assertion to check if the square() function returns the expected result for the input value x. It compares the output of square(x) with the expected value x * x. If the assertion fails, it raises an AssertionError with a message indicating the expected and actual values. This is a common practice in testing to ensure that functions behave as expected.

if __name__ == "__main__":
    main()
    