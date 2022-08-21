import os,sys,subprocess
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
a = os.path.join('/home','ubuntu','youtube.txt')
#
subprocess.call(f'yt-dlp --write-info-json --embed-subs --embed-thumbnail -a {a} --recode-video mp4 -o "%(upload_date)s - %(title)s/%(upload_date)s - %(title)s.%(ext)s"',shell=True)
#
with open(a,'w') as b:
    b.write('')