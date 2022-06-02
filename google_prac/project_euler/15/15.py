"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
<div class="center">
<img alt="" class="dark_img" src="project/images/p015.png"/></div>
How many such routes are there through a 20×20 grid?"""
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
import random
class Grid:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.path_list = []
        self.temp_list = []
    def count_jumps(self):
        coords = (0,0)
        self.temp_list = [coords]
        for i in range(self.width+self.height+1):
            #print(f'line 34 - iteration {i+1}/{self.width+self.height}')
            if coords[0] < self.width and coords[1] < self.height:
                #print(f'line 36 - current coords are {coords}')
                temp_coords = [coords[0],coords[1]]
                temp_coords[random.randrange(0,2,1)] += 1
                coords = (temp_coords[0],temp_coords[1])
                #print(f'line 38 - after randint addition, coords are {coords}')
                self.temp_list.append(coords)
                #print(f'line 40 - current temp_list is {self.temp_list}')
            elif coords[0] == self.width and coords[1] < self.height:
                #print(f'line 42 - current coords are {coords}')
                coords = (coords[0],coords[1]+1)
                #print(f'line 44 - after height addition, coords are {coords}')
                self.temp_list.append(coords)
                #print(f'line 46 - current temp_list is {self.temp_list}')
            elif coords[0] < self.width and coords[1] == self.height:
                #print(f'line 48 - current coords are {coords}')
                coords = (coords[0]+1,coords[1])
                #print(f'line 50 - after width addition, coords are {coords}')
                self.temp_list.append(coords)
                #print(f'line 52 - current temp_list is {self.temp_list}')
            elif coords[0] == self.width and coords[1] == self.height and self.temp_list in self.path_list:
                self.temp_list = [coords]
                continue
            elif coords[0] == self.width and coords[1] == self.height and self.temp_list not in self.path_list:
                #print(f'line 57 - new path found, appending to path_list')
                self.path_list.append(self.temp_list)
                self.temp_list = [coords]
        return self.path_list

new = Grid()
new.width = 21
new.height = 21
while len(new.count_jumps()) < 500000:
    print(f'FINAL LENGTH IS:{len(new.count_jumps())}')