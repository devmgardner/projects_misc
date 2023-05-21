"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
#import os, sys, re
#from bs4 import BeautifulSoup as bs
#import requests as rq
#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)
#filename = re.match(f'.*\\\(.*)\..*',__file__).group(1)
#url = f"https://projecteuler.net/problem={int(filename)}"
#data = rq.get(url)
#soup = bs(data.text,features="html.parser")
#content = soup.find('div',class_="problem_content")
#content = str(content)
#content = re.match(f'\<div class=\"problem_content\" role=\"problem\"\>\n(.*)\n\<\/div\>',content,re.DOTALL).group(1)
#content = re.sub(f'\<p[^\>]*\>','',content)
#content = re.sub(f'\<\/p\>','',content)
#print(content)

def find_num(inp):
    rangelist = []
    for i in range(20):
        rangelist.append(i+1)
    for item in rangelist:
        if inp % item == 0:
            continue
        elif inp % item != 0:
            return False
        elif inp % item == 0 and item == 20:
            return True
count = 296985108420
while find_num(count) != True:
    count -= 20
    print(f'Still not found, count is now {count}.')
print(count)