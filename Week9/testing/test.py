# *** py -3 -m pytest <function_name>.py
import pytest
def func(x):
 return x + 1
def test_answer():
	assert func(2)==3