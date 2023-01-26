"""
File: boggle.py
Name: yiting wu
----------------------------------------
TODO: boggle game - enter 4*4 characters and find every words in dictionary
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: boggle game
	"""
	# 將input變成list 且排除不是字母＆都變小寫的狀況
	lst_l = []
	for i in range(4):
		s = input(f'{i+1} row of letters:').lower().split()
		if len(s) != 4:
			print('illegal')
			return
		for ch in s:
			if not ch.isalpha():
				print('illegal')
				return
			if len(ch) != 1:
				print('illegal')
				return
		lst_l.append(s)

	# lst_l = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

	dic_lst = read_dictionary()
	start = time.time()
	find_anagrams(dic_lst, lst_l)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(dic_lst, lst_l):
	"""
    :param dic_lst: lst of words in dictionary
    :param lst_l: dictionary of entered characters and their positions to find anagrams
    :return: results of anagrams
    """
	ans_lst = []
	for x in range(4):
		for y in range(4):
			# 辨別某個位置的字母是否已經加過
			chosenpath = [(x, y)]
			find_anagrams_helper(lst_l[x][y], dic_lst, ans_lst, lst_l, chosenpath, x, y)
	print(f'There are {len(ans_lst)} words in total.')


def find_anagrams_helper(ans, dic_lst, ans_lst, lst_l, chosenpath, x, y):
	if 3 < len(ans) < 16 and ans in dic_lst and ans not in ans_lst:
		print(f'Found: \"{ans}\"')
		ans_lst.append(ans)
		find_anagrams_helper(ans, dic_lst, ans_lst, lst_l, chosenpath, x, y)
	else:
		# choose
		for i in range(-1, 2):
			for j in range(-1, 2):
				new_x = x + i
				new_y = y + j
				if 0 <= new_x < 4 and 0 <= new_y < 4 and (new_x, new_y) not in chosenpath:
					ans += lst_l[new_x][new_y]
					chosenpath.append((new_x, new_y))
					# explore
					if has_prefix(ans, dic_lst):
						find_anagrams_helper(ans, dic_lst, ans_lst, lst_l, chosenpath, new_x, new_y)
					# Un-choose 把上一步加入的退掉
					chosenpath.pop()
					ans = ans[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic_lst = []
	with open(FILE, "r") as f:
		for line in f:
			dic_lst.append(line)
	for i in range(len(dic_lst)):
		dic_lst[i] = dic_lst[i].replace('\n', '')
	return dic_lst


def has_prefix(sub_s, dic_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic_lst:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
