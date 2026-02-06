from moviepy import VideoFileClip


# Input MP4 file path
video_path = input("Write The Video Path")
# Output MP3 file path
audio_path = input("Write The Save Audio Path")

# Load video
video = VideoFileClip(video_path)

# Extract and write audio
video.audio.write_audiofile(audio_path)
print(f"Audio Succefully Saved At {audio_path}")
# Close to free memory
video.close()