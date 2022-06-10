"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""
import os, sys
#from bs4 import BeautifulSoup as bs
#import requests as rq
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
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
from tqdm import tqdm
def is_prime(inp):
    for i in range(2,int(inp*0.5)+1):
        if inp % i == 0:
            return False
    return True
sum = 0
for i in tqdm(range(2,2000001,1)):
    if is_prime(i) == True:
        sum += i
        with open(os.path.join(currentdir,'10.txt'),'a') as fhand:
            fhand.write(f'Current number is {i}, {i} is prime, adding {i} to sum. Current sum is {sum}.\n')
print(sum)