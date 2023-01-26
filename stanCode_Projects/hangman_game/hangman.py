"""
File: hangman.py
Name: yiting wu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1.ans ="-"依答案的字母數print
    2.將輸入的字母變大寫
    如果不是單一字母print "illegal format"
    3.確認每次猜的是否為答案中的字母
    for loop:
    Check輸入的字母是否可在答案中找到
    並依編號取代"-"
    4.計算猜題次數剩幾次（初始值=7）
    猜錯剩餘次數才會減少、猜對的話次數不變
    5.print猜題結果
    全部猜對（已不含-）答對或
    最後一次猜完（次數=0）公佈答案
    """
    # hint : show how many characters of the answer
    ans = ""
    turns = 7
    word = random_word()
    for i in range(len(word)):
        ans += "-"
    print('The word looks like: ' + ans)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    while True:
        old_guess = input("Your guess: ")
        if turns < 1:
            break
        elif not old_guess.isalpha():
            print('Illegal format.')
        elif len(old_guess) > 1:
            print('Illegal format.')
        elif turns >= 1:
            old_guess = old_guess.upper()
            # 經由check_answer得到每次猜完的結果
            ans = check_answer(word, ans, old_guess)
            # 經由check_turns得到每次猜完剩下的次數
            turns = int(check_turns(word, old_guess, turns))
            # 根據每次猜完顯示對應的結果
            if word.find(old_guess) != -1:
                if ans.find("-") == -1:
                    print('You are correct!\nYou win!!\nThe word was' + str(ans))
                    break
                else:
                    print('You are correct!\nThe word looks like: ' + str(ans))
                    print('You have ' + str(turns) + ' wrong guesses left.')
            else:
                if turns != 0:
                    print("There is no " + old_guess.upper() + "'s in the word.\nThe word looks like: " + ans)
                    print('You have ' + str(turns) + ' wrong guesses left.')
                else:
                    print('You are completely hung :( \nThe word was: ' + word)
                    break


def check_answer(word, ans, old_guess):
    if word.find(old_guess) != -1:
        new_guess = ""
        for j in range(len(word)):
            ch = word[j]
            if ch == old_guess:
                new_guess += old_guess
            else:
                new_guess += ans[j]
        ans = new_guess
    return ans


def check_turns(word, old_guess, turns):
    if word.find(old_guess) == -1:
        turns -= 1
    return turns


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
