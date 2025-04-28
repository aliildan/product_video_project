import os
from moviepy.editor import *
from moviepy.editor import ColorClip
from TTS.api import TTS

# === Settings ===
IMAGE_FOLDER = "images"
SCRIPT_FILE = "scripts/product_script.txt"
AUDIO_FOLDER = "audio"
OUTPUT_FOLDER = "output"
BACKGROUND_MUSIC_FILE = "music/background_music.mp3"  # optional

VOICEOVER_FILE = os.path.join(AUDIO_FOLDER, "voiceover.wav")
FINAL_VIDEO_FILE = os.path.join(OUTPUT_FOLDER, "final_product_video.mp4")
FINAL_VIDEO_WITH_MUSIC_FILE = os.path.join(OUTPUT_FOLDER, "final_product_with_music.mp4")

# === Create folders if they don't exist ===
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === Step 1: Read Script ===
with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
    script_text = f.read()

# === Step 2: Generate Voiceover ===
print("Generating voiceover...")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=True, gpu=True)
tts.tts_to_file(text=script_text, file_path=VOICEOVER_FILE)

# === Step 3: Load Audio ===
audio_clip = AudioFileClip(VOICEOVER_FILE)
audio_duration = audio_clip.duration

# === Step 4: Load Images ===
image_files = sorted(
    [os.path.join(IMAGE_FOLDER, img) for img in os.listdir(IMAGE_FOLDER) if img.endswith(('.png', '.jpg', '.jpeg'))])

if not image_files:
    raise ValueError("No images found in 'images/' folder.")

img_duration = audio_duration / len(image_files)

# === Step 5: Create Image Clips with Ken Burns Effect ===
# Parameters
intro_duration = 2  # seconds
outro_duration = 2  # seconds
video_size = (1280, 720)  # size of the video

# Create intro and outro blank clips
intro_clip = ColorClip(size=video_size, color=(0, 0, 0), duration=intro_duration)
outro_clip = ColorClip(size=video_size, color=(0, 0, 0), duration=outro_duration)

clips = []
for img_path in image_files:
    img_clip = ImageClip(img_path).set_duration(img_duration).resize(height=720)
    img_clip = img_clip.resize(lambda t: 1 + 0.02 * t)
    clips.append(img_clip)

video = concatenate_videoclips([intro_clip] + clips + [outro_clip], method="compose")


# === Step 6: Combine Video with Voiceover ===
final_video = video.set_audio(audio_clip)

# === Step 7: Export Basic Video ===
print("Exporting final video without music...")
final_video.write_videofile(FINAL_VIDEO_FILE, fps=24, codec="libx264", audio_codec="aac")


# === Step 8: Add Background Music (Optional) ===
if os.path.exists(BACKGROUND_MUSIC_FILE):
    print("Adding background music...")
    background_music = AudioFileClip(BACKGROUND_MUSIC_FILE).volumex(0.1)  # lower background music
    mixed_audio = CompositeAudioClip([audio_clip, background_music.set_duration(audio_duration)])

    final_video_with_music = video.set_audio(mixed_audio)

    print("Exporting final video with background music...")
    final_video_with_music.write_videofile(FINAL_VIDEO_WITH_MUSIC_FILE, fps=24)
else:
    print("No background music file found. Skipping music overlay.")

print("✅ All done! Check your 'output/' folder.")
