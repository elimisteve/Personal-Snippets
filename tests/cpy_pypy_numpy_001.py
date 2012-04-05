#
#       Dead simple CPython vs. PyPy vs. NumPy benchmark
#   Taken from: http://www.python-course.eu/numpy.php
#
#   Did this for the purpose of including PyPy into the test.
import time

def CPy_PyPy_version():
    '''
    Run this for CPython vs PyPy
    My results:
     CPython = 0.420805931091 secs
     PyPy    = 0.143736839294 secs
    ''' 
    t = time.time()
    x = range(1000000)
    y = range(1000000)
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
    print time.time() - t
 
def numpy_version():
    '''
    Run this with NumPy
    My results:
    NumPy = 0.0284070968628
    '''
    import numpy
     
    t = time.time()
    x = numpy.arange(1000000)
    y = numpy.arange(1000000)
    z = x + y
    print time.time() - t

