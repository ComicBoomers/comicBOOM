from moviepy.editor import *

clip = VideoFileClip('/Users/samfran/Desktop/comicBoom/my-app/src/ComicBoom_Testing.mov').subclip(1, 3)

clip.write_gif('tester.gif')

