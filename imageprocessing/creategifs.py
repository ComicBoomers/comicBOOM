from moviepy.editor import *

def stackIt(path):
  clip = VideoFileClip(path) # path is relative to where the file is being run
  length = clip.duration
  step = length / 4
  clip0 = clip.subclip(0,1)
  clip1 = clip.subclip(step,1+step)
  clip2 = clip.subclip(2*step,1+2*step)
  clip3 = clip.subclip(3*step,1+3*step)
  final_clip = clips_array([[clip0, clip1],[clip2, clip3]])
  return final_clip.resize(width=480)

def gifIt(clip, outputPath):
  clip.write_gif(outputPath, 12) # path is relative to where to file is being run

# example
# different = stackIt('src/ComicBoom_Testing.mov')
# gifIt(different, '../repotest.gif')
