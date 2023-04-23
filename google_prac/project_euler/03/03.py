"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""
import os, sys, re
from tqdm import tqdm
#from bs4 import BeautifulSoup as bs
#import requests as rq
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
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
num = 600851475143
factor_list = []
for i in tqdm(reversed(range(int(num/2)))):
    if num % (i+1) == 0:
        with open(os.path.join(currentdir,"factors.txt"),'r+') as fhand:
            fhand.write(f'{num} is divisible by {i+1}')
        print(f'{num} is divisible by {i+1}')
print(factor_list)