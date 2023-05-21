"""In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08<br>
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00<br/>
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65<br/>
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91<br/>
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80<br/>
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50<br/>
32 98 81 28 64 23 67 10 <span class="red"><b>26</b></span> 38 40 67 59 54 70 66 18 38 64 70<br/>
67 26 20 68 02 62 12 20 95 <span class="red"><b>63</b></span> 94 39 63 08 40 91 66 49 94 21<br/>
24 55 58 05 66 73 99 26 97 17 <span class="red"><b>78</b></span> 78 96 83 14 88 34 89 63 72<br/>
21 36 23 09 75 00 76 44 20 45 35 <span class="red"><b>14</b></span> 00 61 33 97 34 31 33 95<br/>
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92<br/>
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57<br/>
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58<br/>
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40<br/>
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66<br/>
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69<br/>
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36<br/>
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16<br/>
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54<br/>
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48<br/></br>
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""
import os, sys, pandas as pd
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
with open(os.path.join(currentdir,'11.txt'),'r') as fhand:
    lines = fhand.readlines()
line_list = [line.strip().split(',') for line in lines]
print(line_list)

def find_product(inp):
    count = 1
    for i in inp:
        count *= int(i)
    return count
#set up slices list to hold all possible 4-number combinations
slices = []
#find all 4-number horizontal sets
for line in line_list:
    ind = (0,4)
    while ind[1] < len(line)-1:
        slices.append([int(i) for i in line[ind[0]:ind[1]]])
        ind = (ind[0]+1,ind[1]+1)
#find all 4-number vertical sets
for i in range(20):
    ind = (0,4)
    while ind[1] < 20:
        temp_list = []
        for x in range(ind[0],ind[1],1):
            temp_list.append(line_list[x][i])
        slices.append(temp_list)
        ind = (ind[0]+1,ind[1]+1)
#find all 4-number diagonal sets top left to bottom right
for x in range(20):
    ind = [0,1,2,3]
    while ind[3] < 20:
        try:
            slices.append([line_list[x+i][i] for i in ind])
            slices.append([line_list[i][x+i] for i in ind])
        except IndexError:
            pass
        ind = [i+1 for i in ind]
#find all 4-number diagonal sets top right to bottom left
for x in range(20):
    ind = [16,17,18,19]
    while ind[0] >= 0:
        slices.append([line_list[x-i][i] for i in ind])
        slices.append([line_list[i][x-i] for i in ind])
        ind = [i-1 for i in ind]
result = (0,[])
for i in slices:
    if find_product(i) > result[0]:
        result = (find_product(i),i)

print(result)