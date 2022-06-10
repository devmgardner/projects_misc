"""<p>If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.</p>
<p>If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? </p>
<br /><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.</p>"""
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
nums = {}
nums[1] = 'one'
nums[2] = 'two'
nums[3] = 'three'
nums[4] = 'four'
nums[5] = 'five'
nums[6] = 'six'
nums[7] = 'seven'
nums[8] = 'eight'
nums[9] = 'nine'
nums[10] = 'ten'
nums[11] = 'eleven'
nums[12] = 'twelve'
nums[13] = 'thirteen'
nums[14] = 'fourteen'
nums[15] = 'fifteen'
nums[16] = 'sixteen'
nums[17] = 'seventeen'
nums[18] = 'eighteen'
nums[19] = 'nineteen'
nums[20] = 'twenty'
nums[30] = 'thirty'
nums[40] = 'forty'
nums[50] = 'fifty'
nums[60] = 'sixty'
nums[70] = 'seventy'
nums[80] = 'eighty'
nums[90] = 'ninety'
num_list = []

for i in range(999):
    i += 1
    print(f'current number is {i}')
    if i in nums.keys():
        num_list.append(nums[i])
    elif not i in nums.keys():
        if i >= 100:
            num_list.append(nums[int(i/100)])
            remainder = i%100
            if remainder != 0:
                num_list.append('hundred')
                num_list.append('and')
                if remainder in nums.keys():
                    num_list.append(nums[remainder])
                elif remainder > 20 and not remainder in nums.keys():
                    num_list.append(nums[int(remainder/10)*10])
                    remainder = i%10
                    num_list.append(nums[remainder])
            elif remainder == 0:
                num_list.append('hundred')
        elif i > 20 and i < 100:
            num_list.append(nums[int(i/10)*10])
            remainder = i%10
            if remainder != 0:
                num_list.append(nums[remainder])
num_list.append('one')
num_list.append('thousand')
no_spaces = ''.join(num_list)
print(len(no_spaces))