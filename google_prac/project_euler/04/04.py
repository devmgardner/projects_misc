"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
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
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
fname = os.path.join(currentdir, f'04-log.txt')
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#
from itertools import product
from operator import itemgetter
def is_palindrome(inp):
    if ''.join(reversed(list(str(inp)))) == str(inp):
        return True
    else:
        return False

pallist = []

lista = listb = [i for i in range(1000) if i > 100 and not str(i).endswith('0')]
for i1,i2 in product(lista, listb):
    if is_palindrome(i1*i2) == True:
        pallist.append([i1,i2,i1*i2])

for i in sorted(pallist, key=itemgetter(2)):
    fhand.write(f'{i}\n')