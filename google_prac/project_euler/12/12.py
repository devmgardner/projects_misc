"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7<sup>th</sup> triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
<blockquote class="monospace"><b> 1</b>: 1<br><b> 3</b>: 1,3<br/><b> 6</b>: 1,2,3,6<br/><b>10</b>: 1,2,5,10<br/><b>15</b>: 1,3,5,15<br/><b>21</b>: 1,3,7,21<br/><b>28</b>: 1,2,4,7,14,28</br></blockquote>
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?"""
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
def find_divisors(inp):
    divisor_list = [i for i in range(1,int((inp/2)+1),1) if inp % i == 0]
    return divisor_list

def triangle_number(inp):
    sum = 0
    for i in range(1,inp,1):
        sum += i
    return sum

n = 100000
while len(find_divisors(triangle_number(n))) < 501:
    n += 1

print(n)