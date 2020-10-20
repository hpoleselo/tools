# Manual unit testing
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")


# In order to make better unit tests and instead of creating single input tests for our unit test, is better to use a Test Runner, in this case, unittest
import unittest

# Instead of using assert statement, unittest uses TestCase
# And we have now to create a class that inherits from the TestCase
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    print("Using unittest")
    unittest.main()



"""
def functionToBeTested(x):
    y = x**2
    return y


class MyTest(unittest.TestCase):
    def test(self):
        # First argument is the function we're testing along with the input and the second argument is the expected result.
        self.assertEqual(functionToBeTested(3), 9)


# We can also test a class

class MyFun:
    def fun(self, n):
        return n + 1

class MyFunTest(unittest.TestCase):
    def testFun(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)

if __name__ == '__main__':
    unittest.main()
"""