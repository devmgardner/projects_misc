import os,sys,subprocess,datetime,time
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
a = [line.strip() for line in open(os.path.join('/home','ubuntu','youtube.txt')).readlines()]
#
for b in a:
    subprocess.call(f'yt-dlp --write-info-json --embed-subs --embed-thumbnail --recode-video mp4 -o "/media/Dock1/Media/Videos/Dailies/{datetime.datetime.fromtimestamp(time.time()).strftime("%m-%d-%Y_%H:%M:%S")}/%(upload_date)s - %(title)s/%(upload_date)s - %(title)s.%(ext)s" {b}',shell=True)
#
with open(os.path.join('/home','ubuntu','youtube.txt'),'w') as c:
    c.write('')