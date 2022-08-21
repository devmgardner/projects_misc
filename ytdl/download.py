import os,sys,time,datetime,traceback,subprocess,json
from pytube import YouTube
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
with open(os.path.join('/home','ubuntu','youtube.txt'),'r') as fhand:
    lines = [line.strip() for line in fhand.readlines()]
logger = open(os.path.join('/media','Dock1','Media','Videos',f'Log_File_{datetime.datetime.fromtimestamp(time.time()).strftime("%m-%d-%Y_%H:%M:%S")}.txt'),'w')
#
downloaded = {}
for line in lines:
    try:
        yt = YouTube(line)
    except Exception as e:
        logger.write(f'{str(e)}\n')
        logger.write(f'{traceback.format_exc}\n')
        downloaded[line] = 'False'
    #
    if not os.path.exists(os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}')):
        subprocess.call(f"mkdir {os.path.join('media','Dock1','Media','Videos',f'{yt.channel_id}')}")
    SAVE_PATH = os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}')
    mp4files = yt.filter('mp4')
    yt.set_filename(yt.title)
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    video = {}
    video['title'] = yt.title
    video['author'] = yt.author
    video['description'] = yt.description
    video['keywords'] = yt.keywords
    video['length'] = yt.length
    video['age_restricted'] = yt.age_restricted
    video['channel_id'] = yt.channel_id
    video['channel_url'] = yt.channel_url
    video['embed_url'] = yt.embed_url
    video['initial_data'] = yt.initial_data
    video['metadata'] = yt.metadata
    video['publish_date'] = yt.publish_date
    video['rating'] = yt.rating
    video['streams'] = yt.streams
    video['thumbnail_url'] = yt.thumbnail_url
    video['video_id'] = yt.video_id
    video['views'] = yt.views
    video['watch_url'] = yt.watch_url
    video['captions'] = yt.captions
    video['caption_tracks'] = yt.caption_tracks
    try:
        d_video.download(SAVE_PATH)
        with open(os.path.join('media','Dock1','Media','Videos',f'{yt.channel_id}',f'{yt.title}.json'),'w') as fhand:
            fhand.write(json.dump(video,indent=4))
        downloaded[line] = 'True'
    except Exception as e:
        logger.write(f'{str(e)}\n')
        logger.write(f'{traceback.format_exc}\n')
        downloaded[line] = 'False'
for k,v in downloaded.items:
    with open(os.path.join('/home','ubuntu','youtube.txt'),'w') as fhand:
        if v == 'False':
            fhand.write(f'{k}\n')