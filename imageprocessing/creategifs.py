from moviepy.editor import *
# video.fx is loaded as vfx

def stackIt(path):
  clip = VideoFileClip(path).margin(10) # path is relative to where the file is being run
  length = clip.duration
  step = length / 3
  clip0 = clip.subclip(0,1)
  clip1 = clip.subclip(step,1+step)
  clip2 = clip.subclip(length - step - 1,length - step)
  clip3 = clip.subclip(length-1, length)
  booms_clip = clips_array([[clip0, clip1],[clip2, clip3]]).resize(width=480)
  # create a list of the horizontal comic frames
  frame = ["./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png", "./public/comicframesh.png"]
  # summon an image clip for the image of duration of .1 second for each frame
  frames = [ImageClip(m).set_duration(.1) for m in frame]
  # turn the list of comic frames into a video of length 1 s
  frames_clip = concatenate_videoclips(frames, method="compose")
  # overlay the comic frames on
  final_clip = CompositeVideoClip([booms_clip,frames_clip])
  return final_clip

def gifIt(clip, outputPath):
  clip.write_gif(outputPath, 12) # path is relative to where to file is being run

# example
different = stackIt('../test.mov')
gifIt(different, '../test.gif')

# def paintIt(clip):
# painted = paintIt(different)
# pngIt(painted, '../painttest.png')
#   freezeframe = clip.to_ImageClip(0)
#   return (clip.fx(vfx.painting, 2.0, 0.5).to_ImageClip(0))

# def pngIt(clip, outputPath):
  # clip.save_frame(outputPath)
