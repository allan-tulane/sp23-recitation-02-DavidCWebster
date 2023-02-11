"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###


def simple_work_calc(n, a, b):
  #"""Compute the value of the recurrence $W(n) = aW(n/b) + n
  #
  #	Params:
  #n......input integer
  #a......branching factor of recursion tree
  #b......input split factor

  #Returns: the value of W(n).
  #"""

  if n <= 1:
    return 1

  return a * simple_work_calc(n // b, a, b) + n


def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(27, 2, 3) == 65
  assert simple_work_calc(256, 3, 4) == 781
  assert simple_work_calc(40, 4, 4) == 176


def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  # TODO
  if n <= 1:
    return 1

  return a * work_calc(n // b, a, b, f) + f(n)


def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  if n <= 1:
    return n
  return span_calc(n // b, a, b, f) + f(n)


def test_work():
  """ done. """
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(27, 2, 3, lambda n: n + n) == 122
  assert work_calc(256, 3, 4, lambda n: 2) == 161
  assert work_calc(40, 2, 2, lambda n: n // 2) == 124


def compare_work(work_fn1,
                 work_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  result = []
  for n in input_sizes:
    # compute W(n) using current a, b, f
    result.append((n, work_fn1(n), work_fn2(n)))
  return result


def print_results(results):
  """ done """
  print(
    tabulate.tabulate(results,
                      headers=['n', 'W_1', 'W_2'],
                      floatfmt=".3f",
                      tablefmt="github"))


def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work

  # create work_fn1
  # create work_fn2

  res = compare_work(work_fn1, work_fn2)
  print(res)


def test_compare_span():
  assert span_calc(40, 2, 3, lambda n: n) == 58
  assert span_calc(40, 2, 3, lambda n: 1) == 4
  assert span_calc(40, 2, 3, lambda n: int(math.log2(n))) == 11
