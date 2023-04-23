import ffmpeg, os, sys
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
with open(os.path.join(currentdir,'tree.txt'),'r') as fhand:
    lines = [line.strip() for line in fhand.readlines()]
    lines = [line.split('---') for line in lines]
#
SAVE_PATH = os.path.join('/media','Dock1','Media','Videos')
#
for line in lines:
    audio_stream = ffmpeg.input(os.path.join(SAVE_PATH,line[0],line[1]))
    video_stream = ffmpeg.input(os.path.join(SAVE_PATH,line[0],line[2]))
    ffmpeg.output(audio_stream, video_stream, os.path.join(SAVE_PATH,line[3])).run()