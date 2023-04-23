"""A Pythagorean triplet is a set of three natural numbers, <var>a</var> &lt; <var>b</var> &lt; <var>c</var>, for which,
<div class="center"> <var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup></div>
For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.
There exists exactly one Pythagorean triplet for which <var>a</var> + <var>b</var> + <var>c</var> = 1000.<br>Find the product <var>abc</var>.</br>"""
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
import itertools
def is_pythag(inp):
    inp1, inp2, inp3 = inp[0], inp[1], inp[2]
    if inp1**2 + inp2**2 == inp3**2:
        return True
    else:
        return False
#3+4+5=12
#highest number in triplet is 5
#5/12=.4167
#1000*.4167=416.7
for i in itertools.product(range(1,1001,1), range(1,1001,1), range(1,1001,1)):
    if sum(i) == 1000:
        if is_pythag(i) == True:
            if i[0] < i[1] and i[1] < i[2]:
                print(f'{i[0]} x {i[1]} x {i[2]} = {i[0]*i[1]*i[2]}')