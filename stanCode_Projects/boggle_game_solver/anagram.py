"""
File: anagram.py
Name: yitig wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: 依輸入的單字 各字母排列組合 在dictionary中尋找有意義的單字
    """
    print("Welcome to stanCode \"Anagram Generator \" (or -1 to quit)")
    while True:
        s = str(input('Find anagrams for: '))
        start = time.time()
        if s == EXIT:
            pass
        else:
            dic_lst = read_dictionary()
            find_anagrams(s, dic_lst)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dic_lst = []
    with open(FILE, "r") as f:
        for line in f:
            dic_lst.append(line)
    for i in range(len(dic_lst)):
        dic_lst[i] = dic_lst[i].replace('\n', '')
    return dic_lst


def find_anagrams(s, dic_lst):
    """
    :param s: the entered word to find anagrams
    :param dic_lst: lst of words in dictionary
    :return: results of anagrams
    """
    ans_lst = []
    find_anagrams_helper(s, '', dic_lst, ans_lst)
    # print(str(count) + 'anagrams: '+ ans_lst )
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def find_anagrams_helper(s, ans, dic_lst, ans_lst):
    # 必須判斷每次的結果是否為已出現過的組合加以排除 (s出現重複字母的狀況下會發生)
    if len(ans) == len(s) and ans in dic_lst and ans not in ans_lst:
        print('Found: ' + ans)
        print('Searching...')
        ans_lst.append(ans)
    else:
        for ch in s:
            # choose
            ans += ch
            # explore
            # 當字母有重複時 需要判斷為出現的第幾個字母 小於或等於s中的數量 就要繼續加入
            if ans.count(ch) <= s.count(ch) and has_prefix(ans, dic_lst):
                find_anagrams_helper(s, ans, dic_lst, ans_lst)
                # Un-choose 把上一步加入的退掉
            ans = ans[:-1]


def has_prefix(sub_s, dic_lst):
    """
    :param sub_s: part of s from the beginning
    :return: boolean
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
