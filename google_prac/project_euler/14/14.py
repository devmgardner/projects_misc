"""The following iterative sequence is defined for the set of positive integers:
<var>n</var> → <var>n</var>/2 (<var>n</var> is even)<br><var>n</var> → 3<var>n</var> + 1 (<var>n</var> is odd)</br>
Using the rule above and starting with 13, we generate the following sequence:
<div class="center">13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1</div>
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
<b>NOTE:</b> Once the chain starts the terms are allowed to go above one million."""
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
from tqdm import tqdm
def is_even(inp):
    if inp % 2 == 0:
        return True
def is_odd(inp):
    if inp % 2 == 1:
        return True
def seq(inp):
    chain = [inp]
    while not inp == 1:
        if is_even(inp):
            inp = int(inp/2)
            chain.append(inp)
        elif is_odd(inp):
            inp = int((inp*3)+1)
            chain.append(inp)
    return chain
count = (0,0,0)
for i in tqdm(range(2,1000001,1)):
    if len(seq(i)) > count[2]:
        count = (i,seq(i),len(seq(i)))
print(f'i is {count[0]}\nlength of sequence is {count[2]}\nsequence is {count[1]}')