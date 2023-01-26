"""
File: webcrawler.py
Name: yiting wu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Write your code below this line ----- #

        tag = soup.find('tbody')
        number_male = []
        number_female = []
        count = 0
        d = []
        number = []
        digit_male = []
        digit_female = []
        for tr in tag.find_all('tr'):
            for td in tr.find_all('td'):
                d.append(td.text)
        for ch in d:
            if ch.find(',') != -1:
                number.append(ch)
        # 分出男女兩個list
        for i in range(len(number)):
            if i % 2 == 0:
                number_male.append(number[i])
                count += 1
            else:
                number_female.append(number[i])
                count += 1
        # 把,取代才能轉成數字list後加總
        for num_male in number_male:
            num_male = num_male.replace(',', '')
            digit_male.append(int(num_male))
        for num_female in number_female:
            num_female = num_female.replace(',', '')
            digit_female.append(int(num_female))
        print('Male number: ' + str(sum(digit_male)))
        print('Female number: ' + str(sum(digit_female)))


if __name__ == '__main__':
    main()
