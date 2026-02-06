from moviepy import VideoFileClip
import os

# Input file path
video_path = input("Write the video file path: ").strip('"')  # Remove quotes if dragged
audio_path = input("Write the save audio path (e.g., output.mp3): ").strip('"')

# Ensure output has audio extension
if not audio_path.lower().endswith(('.mp3', '.wav', '.aac', '.flac', '.ogg')):
    audio_path += '.mp3'
    print(f"Added .mp3 extension: {audio_path}")

try:
    # Check if input file exists
    if not os.path.exists(video_path):
        print(f"Error: File not found: {video_path}")
        exit(1)
    
    # Load video
    print("Loading video...")
    video = VideoFileClip(video_path)
    
    # Check if video has audio
    if video.audio is None:
        print("Error: This file has no audio track!")
        video.close()
        exit(1)
    
    # Extract and write audio
    print("Extracting audio...")
    video.audio.write_audiofile(audio_path)
    print(f"✓ Audio successfully saved at: {audio_path}")
    
    # Close to free memory
    video.close()
    
except Exception as e:
    print(f"Error: {e}")