"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
#import os, sys, re
#from bs4 import BeautifulSoup as bs
#import requests as rq
#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)
#filename = re.match(f'.*\/(.*)\/..*',__file__).group(1)
#url = f"https://projecteuler.net/problem={int(filename)}"
#data = rq.get(url)
#soup = bs(data.text,features="html.parser")
#content = soup.find('div',class_="problem_content")
#content = str(content)
#content = re.match(f'\<div class=\"problem_content\" role=\"problem\"\>\n(.*)\n\<\/div\>',content,re.DOTALL).group(1)
#content = re.sub(f'\<p[^\>]*\>','',content)
#content = re.sub(f'\<\/p\>','',content)
#print(content)
def is_prime(inp):
    for i in range(2,int(inp*0.5)+1):
        if inp % i == 0:
            return False
    return True
count = 1
num = 2
while count < 10001:
    if is_prime(num) == True:
        print(f'{num} is prime, count is {count}')
        count += 1
    num += 1
print(num)