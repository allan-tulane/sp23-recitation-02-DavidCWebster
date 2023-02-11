from main import *


def test_simple_work():

  assert smple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(27, 2, 3) == 65
  assert simple_work_calc(256, 3, 4) == 781
  assert simple_work_calc(40, 4, 4) == 176


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(27, 2, 3, lambda n: n + n) == 122
  assert work_calc(256, 3, 4, lambda n: 2) == 161
  assert work_calc(40, 2, 2, lambda n: n // 2) == 124
