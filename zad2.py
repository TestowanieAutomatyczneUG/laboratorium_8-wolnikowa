# import unittest
# from parameterized import *
class FizzBuzz:
    def game(self, num):
        if (type(num) is int):
            if (num % 5==0 and num%3==0):
                return "FizzBuzz"
            elif ((num % 5) == 0):
                return "Buzz"
            elif((num%3)==0):
                return "Fizz"
            else:
                return num
        else:
            raise Exception("Wrong value type")
# class testFizzBuzz(unittest.TestCase):
#     def setUp(self):
#         self.temp =FizzBuzz()
#     @parameterized.expand([
#         (5,"Buzz"),
#         (3,"Fizz"),
#         (15, "FizzBuzz"),
#         (-15, "FizzBuzz"),
#         (13, 13),
#         (-16, -16)
#     ])
#     def test_parameterized(self,number, expectedOutput):
#         self.assertEqual(self.temp.game(number), expectedOutput)
#
# @parameterized_class(('num', 'expectedOutput'), [
#     (5, "Buzz"),
#     (3, "Fizz"),
#     (15, "FizzBuzz"),
#     (-15, "FizzBuzz"),
#     (13, 13),
#     (-16, -16)
# ])
#
# class testFizzBuzzClass(unittest.TestCase):
#     def setUp(self):
#         self.tmp = FizzBuzz()
#
#     def test_parameterized_class(self):
#         self.assertEqual(self.tmp.game(self.num), self.expectedOutput)

# @parameterized_class(('exception'), [
#     ("trzy"),
#     ("3"),
#     ([1,2,3]),
#     ({}),
#     (False),
#     (None)
# ])
#
# class testFizBuzzClasException(unittest.TestCase):
#     def setUp(self):
#         self.tmp = FizzBuzz()
#
#     def test_parameterized_exceptions(self):
#         self.assertRaises(Exception, self.tmp.game, self.exception)

# if __name__ == '__main__':
#     unittest.main()



from parameterized import parameterized, parameterized_class
import unittest

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
            (5, "Buzz"),
            (3, "Fizz"),
            (15, "FizzBuzz"),
            (-15, "FizzBuzz"),
            (13, 13),
            (-16, -16)
    ])

    def test_parameterized(self, num, expectedOutput):
        self.assertEqual(self.tmp.game(num), expectedOutput)

    @parameterized.expand([
        ("3",),
        ([1,2,3],),
        ({},),
        (99.9999,),
        (False,),
        (None,)
    ])

    def test_parameterized_exceptions(self, exception):
        self.assertRaises(Exception, self.tmp.game, exception)

@parameterized_class(('num', 'expectedOutput'), [
    (5, "Buzz"),
    (3, "Fizz"),
    (15, "FizzBuzz"),
    (-15, "FizzBuzz"),
    (13, 13),
    (-16, -16)
])

class TestFizzBuzzClass(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_parameterized_class(self):
        self.assertEqual(self.tmp.game(self.num), self.expectedOutput)

@parameterized_class(('exception'), [
    ("3",),
    ([1, 2, 3],),
    ({},),
    (99.9999,),
    (False,),
    (None,)
])

class TestFizzBuzzClassException(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_parameterized_class_exceptions(self):
        self.assertRaises(Exception, self.tmp.game, self.exception)

if __name__ == '__main__':
    unittest.main()