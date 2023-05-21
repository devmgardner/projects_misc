import os, sys, re
from bs4 import BeautifulSoup as bs
import requests as rq
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
filename = re.match(f'.*\/(.*)\/..*',__file__).group(1)
url = f"https://projecteuler.net/problem={int(filename)}"
data = rq.get(url)
soup = bs(data.text,features="html.parser")
content = soup.find('div',class_="problem_content")
content = str(content)
content = re.match(f'\<div class=\"problem_content\" role=\"problem\"\>\n(.*)\n\<\/div\>',content,re.DOTALL).group(1)
content = re.sub(f'\<p[^\>]*\>','',content)
content = re.sub(f'\<\/p\>','',content)
print(content)