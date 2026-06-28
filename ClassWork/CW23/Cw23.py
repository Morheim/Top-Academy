# import unittest
#
# def calculate_discount(level, amount):
# 	if level == "basic":
# 		return amount * 0.95
# 	elif level == "silver":
# 		return amount * 0.90
# 	elif level == "gold":
# 		return amount * 0.85
# 	else:
# 		raise ValueError("Unknown level")
#
# class TestCalculateDiscount(unittest.TestCase):
# 	def test_basic_discount(self):
# 		self.assertEqual(calculate_discount("basic", 100),95.0)
#
# 	def test_silver_discount(self):
# 		self.assertEqual(calculate_discount("silver", 100),90.0)
#
# 	def test_gold_discount(self):
# 		self.assertEqual(calculate_discount("gold", 100),85.0)
#
# 	def test_invalid_level(self):
# 		with self.assertRaises(ValueError):
# 			calculate_discount("platinum",100)
#
# if __name__ == '__main__':
# 	unittest.main()


import pytest
def count_punct_marks(string:str)->int:
	total_count = 0
	for sym in ",.;:'":
		total_count += string.count(sym)
	return total_count

def test_cont_punct_mark_no_punct():
	assert count_punct_marks("Шла Саша по шоссе и сосала сушку") == 0


def test_cont_punct_mark_multiple():
	assert count_punct_marks("Передвегалась 'Александара' по авто магестрали и употребляла хлебоболочне изделия.") == 3


def test_cont_punct_mark_empty():
	assert count_punct_marks("") == 0