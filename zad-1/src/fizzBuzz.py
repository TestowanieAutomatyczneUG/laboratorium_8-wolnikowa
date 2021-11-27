import math
import re


def fizzBuzz(num):
    if type(num) is int:
       if (num % 5==0 and num%3==0):
            return "FizzBuzz"
       elif ((num % 5) == 0):
            return "Buzz"
       elif((num%3)==0):
            return "Fizz"
       else:
           return num
   else:
        raise TypeError("Error in FizzBuzz")