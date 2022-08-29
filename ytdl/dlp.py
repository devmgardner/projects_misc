import os,sys,subprocess,datetime,time,re
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
a = [line.strip() for line in open(os.path.join('/home','ubuntu','youtube.txt')).readlines()]
#
now = datetime.datetime.fromtimestamp(time.time()).strftime("%m-%d-%Y_%H:%M:%S")
#
for b in a:
    if not 'channel' in b or '/c/' in b or 'user' in b:
        subprocess.call(f'yt-dlp --write-info-json --embed-subs --embed-thumbnail --recode-video mp4 -o "/media/Dock1/Media/Videos/Dailies/{now}/%(upload_date)s - %(title)s/%(upload_date)s - %(title)s.%(ext)s" {b}',shell=True)
    elif 'channel' in b or '/c/' in b or 'user' in b:
        try:
            channel = re.search('channel\/(.*)',b).group(1)
        except:
            channel = re.search('\/c\/(.*)',b).group(1)
        except:
            channel = re.search('\/user\/(.*)',b).group(1)
        subprocess.call(f'yt-dlp --write-info-json --embed-subs --embed-thumbnail --recode-video mp4 --download-archive {channel}.txt {b} -o "/media/Dock1/Media/Videos/Channels/{channel}/%(upload_date)s - %(title)s/%(upload_date)s - %(title)s.%(ext)s"', shell=True)
#
with open(os.path.join('/home','ubuntu','youtube.txt'),'w') as c:
    c.write('')