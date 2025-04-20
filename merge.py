from moviepy.editor import VideoFileClip, AudioFileClip

# Load video and audio
video = VideoFileClip("downloads/video.mp4")
audio = AudioFileClip("outputs/dubbed.mp3")

# Set new audio to video
final_video = video.set_audio(audio)

# Export final video
final_video.write_videofile("outputs/final_dubbed_video.mp4")

print("✅ Final dubbed video saved to outputs/final_dubbed_video.mp4")

