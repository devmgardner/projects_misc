import os,sys,time,datetime,traceback,subprocess,json,ffmpeg
from pytube import YouTube
# set up currentdir
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# read input file and set up logger
with open(os.path.join('/home','ubuntu','youtube.txt'),'r') as fhand:
    lines = [line.strip() for line in fhand.readlines()]
logger = open(os.path.join('/media','Dock1','Media','Videos',f'Log_File_{datetime.datetime.fromtimestamp(time.time()).strftime("%m-%d-%Y_%H:%M:%S")}.txt'),'w')
if len(lines[0]) == 0:
    logger.write(f'no files to download, quitting\n')
    quit()
# set up blank dict for finding out what has been downloaded successfully and what hasn't
downloaded = {}
# main loop
for line in lines:
    try:
        # get youtube link and instantiate a YouTube object
        yt = YouTube(line)
    except Exception as e:
        logger.write(f'{str(e)}\n')
        logger.write(f'{traceback.format_exc}\n')
        downloaded[line] = 'False'
    # if the directory for this channel_id doesn't exist, create it
    if not os.path.exists(os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}')):
        subprocess.call(f"mkdir {os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}')}",shell=True)
    # set up output path
    SAVE_PATH = os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}')
    # main video loop, gets all streams by video only with mp4 extension
    mp4files = yt.streams.filter(file_extension='mp4',only_video=True)
    # get the itag and resolution of the stream
    resolutions = [(stream.itag,stream.resolution[:-1]) for stream in mp4files]
    # sort by resolution
    resolutions.sort(key=lambda y: y[1],reverse=True)
    # iterate through all resolutions/itags
    for res in resolutions:
        # if the resolution is the maximum resolution in the list,
        if int(res[1]) == max([int(res[1]) for res in resolutions]):
            # get the stream by its itag
            vstream = yt.streams.get_by_itag(res[0])
    # main audio loop, gets all streams by audio only with mp4 extension
    mp3files = yt.streams.filter(file_extension='mp4',only_audio=True)
    # get the itag and bitrate of the stream
    bitrates = [(stream.itag,stream.abr[:-4]) for stream in mp3files]
    # sort by bitrate
    resolutions.sort(key=lambda y: y[1],reverse=True)
    # iterate through all bitrates/itags
    for res in resolutions:
        # if the bitrate is the maximum bitrate in the list,
        if int(res[1]) == max([int(res[1]) for res in resolutions]):
            # get the stream by its itag
            astream = yt.streams.get_by_itag(res[0])
    # set up a dictionary for the video for metadata and collect all of it
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
    video['thumbnail_url'] = yt.thumbnail_url
    video['video_id'] = yt.video_id
    video['views'] = yt.views
    video['watch_url'] = yt.watch_url
    video['captions'] = yt.captions
    video['caption_tracks'] = yt.caption_tracks
    if not os.path.exists(os.path.join(SAVE_PATH,f'{yt.title}.mp4')):
        try:
            # try to download the video and audio of the stream
            vstream.download(output_path=SAVE_PATH,filename=f'{yt.title}_video.mp4')
            astream.download(output_path=SAVE_PATH,filename=f'{yt.title}_audio.mp4')
            # try to combine them using ffmpeg
            video_stream = ffmpeg.input(os.path.join(SAVE_PATH,f'{yt.title}_video.mp4'))
            audio_stream = ffmpeg.input(os.path.join(SAVE_PATH,f'{yt.title}_audio.mp4'))
            ffmpeg.output(audio_stream, video_stream, os.path.join(SAVE_PATH,f'{yt.title}.mp4')).run()
            # write the metadata to a JSON file
            with open(os.path.join('/media','Dock1','Media','Videos',f'{yt.channel_id}',f'{yt.title}.json'),'w') as fhand:
                fhand.write(json.dump(video,indent=4))
            downloaded[line] = 'True'
            logger.write(f'wrote {yt.title}.mp4\n')
        except Exception as e:
            logger.write(f'{str(e)}\n')
            logger.write(f'{traceback.format_exc()}\n')
            downloaded[line] = 'False'
    else:
        logger.write(f'{yt.title}.mp4 already exists, skipping\n')
# iterate through downloaded dict, anything that wasn't downloaded gets re-written to the original .txt file
for k,v in downloaded.items():
    with open(os.path.join('/home','ubuntu','youtube.txt'),'w') as fhand:
        if v == 'False':
            fhand.write(f'{k}\n')