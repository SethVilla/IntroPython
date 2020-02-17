# can run in https://repl.it/languages/python3


# The logarithm, or log, is the inverse of the mathematical operation of exponentiation. This means that the log of a number is the number that a fixed base has to be raised to in order to yield the number. Import Numpy for method to do such

# numpy installation https://www.edureka.co/blog/install-numpy/
import numpy

# input() allows user to enter string
# int() to cast user input to an integer
x = int(input('Enter number x: '))
y = int(input('Enter number y: '))


# x ** y represents x to the power of y
# print() or print to console
# .format looks for {} in order to place its arguments
print('x**y = {}'.format(x**y))
print('log(x) = {}'.format(numpy.log2(x)))
