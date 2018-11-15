from moviepy.editor import *

def stackIt(path):
  clip = VideoFileClip(path)
  length = clip.duration
  step = length / 4
  clip0 = clip.subclip(0,1)
  clip1 = clip.subclip(step,1+step)
  clip2 = clip.subclip(step+step,1+step+step)
  clip3 = clip.subclip(step+step+step,1+step+step+step)
  final_clip = clips_array([[clip0, clip1],[clip2, clip3]])
  return final_clip.resize(width=480)

  # .write_gif("steppedstack.gif",12)

def gifIt(clip, outputPath):
  clip.write_gif(outputPath, 12)

# final = stackIt("trailer_1080p.mov")
# gifIt(final, "functional.gif")

# different = stackIt("IMG_1064.mov")
# gifIt(different, "test.gif")
