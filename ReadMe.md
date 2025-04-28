
## Product Video Generator

This is a simple learning project that shows how to create basic product videos with Python.

It combines a short product script, a few images, and generates a video with automatic voiceover and optional background music.

The goal of this project is to practice working with:

- Text-to-Speech (TTS) technology
- Image and video editing with Python
- Audio mixing and video exporting

It is **not** a full production tool — it is designed for **educational purposes**.

> Note: This project requires Python 3.11 to run properly.
---
## Future Improvements

This project can be expanded by integrating AI agents to automate content creation.

📸 Automatically generate product images using AI image generators.

🔊 Automatically generate marketing scripts based on product descriptions.

📊 Build a fully automated product video creation pipeline with minimal human input.

These improvements would make the tool even more powerful for rapid content generation.

---
## Features

- 📸 Add multiple product images
- 🎤 Generate a realistic voiceover from your text
- 🎬 Create a video with intro and outro blank screens
- 🎵 (Optional) Add background music
- ⚡ Lightweight and easy to customize

---

## Folder Structure

```
product_video_project/
├── images/        # Product images (.jpg or .png)
├── scripts/       # Product text script (.txt file)
├── audio/         # Generated voiceover (.wav file)
├── music/         # Optional background music (.mp3)
├── output/        # Final product videos (.mp4)
├── create_video.py # Main script
└── requirements.txt # Python dependencies
```

---

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv testenv
source testenv/bin/activate
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

---

## How to Use

1. Add your product images into the `images/` folder.
2. Write a simple script inside `scripts/product_script.txt`.
3. (Optional) Add background music to the `music/` folder.
4. Run the main script:

```bash
python3 create_video.py
```

5. Find the final video inside the `output/` folder.

---

## Notes

- Images should be in `.jpg` or `.png` format.
- Recommended image size is **1280x720** pixels.
- The video will automatically add 2 seconds intro and outro.
- No external API is needed — everything works locally.

---

## Troubleshooting

If you experience issues during setup or running the script, check the following:

- **Check your Python version:**

```bash
python --version
```
Make sure it shows **Python 3.11.x**.

- **Make sure you are using the virtual environment:**

```bash
which python
which pip
```
They should point to the `/your_project_path/testenv/bin/` folder.

- **If you installed packages globally instead of inside the virtual environment:**
  
You might need to reinstall inside the virtual environment:

```bash
pip install -r requirements.txt
```

- **If a package seems installed but you still get `ModuleNotFoundError`:**

Recreate the environment:

```bash
rm -rf testenv
python3 -m venv testenv
source testenv/bin/activate
pip install -r requirements.txt
```

This will reset the environment cleanly.

---
## License

This project is free for personal learning and experimentation.

---
