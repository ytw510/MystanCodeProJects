"""
File: largest_digit.py
Name: yiting wu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: given number
	:return: the biggest digit of n
	"""
	# 處理可能出現負數
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0)
	# ans先定義為0 (max為python內建定義使用 變數避免使用max命名)
	# return function or 用變數承接 / 不然ans不會跟著helper function而改變


def find_largest_digit_helper(n, ans):
	if n == 0:
		return ans
	else:
		if n % 10 > ans:
			ans = n % 10
			return find_largest_digit_helper(n // 10, ans)
		else:
			return find_largest_digit_helper(n // 10, ans)


if __name__ == '__main__':
	main()
