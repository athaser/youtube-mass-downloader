# 🎧 YouTube Mass Downloader

A Python script that **batch downloads audio from multiple YouTube videos** and converts them to high-quality MP3s using `yt-dlp` and `ffmpeg`. Authenticated downloads (e.g. age-restricted or CAPTCHA-blocked videos) are supported via cookie export.

---

## 📁 Output

All downloaded MP3 files are saved in the `exports/` folder, with filenames prefixed by their assigned number.

---

## ✅ Features

- Batch download multiple YouTube links
- Converts to `.mp3` format with `ffmpeg`
- Supports timestamps (e.g. `?t=22`)
- Handles restricted videos using your browser cookies
- Cross-platform (Windows-focused pathing)

---

## 📦 Requirements

- Python 3.9+ (Python 3.13 recommended)
- `ffmpeg` installed locally
- Required Python package:

---

## Install it:

```bash
pip install -r requirements.txt
