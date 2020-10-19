import unittest

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