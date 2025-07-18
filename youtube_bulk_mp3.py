import yt_dlp
from pathlib import Path

# Resolve ffmpeg binary path
ffmpeg_path = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Packages" / \
              "Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe" / \
              "ffmpeg-7.1.1-essentials_build" / "bin"
ffmpeg_path = str(ffmpeg_path)

# Ensure export folder exists
export_dir = Path(__file__).parent / "exports"
export_dir.mkdir(exist_ok=True)

# Optional: path to your exported YouTube cookies
cookie_file = 'youtube_cookies.txt'

# List of (filename_prefix, YouTube URL)
urls = [
    ("01", "https://www.youtube.com/watch?v=hx6mh9BkL2M"),
    ("02", "https://youtu.be/n4uUIY6MDU0?t=22"),
    # Add more...
]

# Loop and download each video as MP3
for number, url in urls:
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': str(export_dir / f'{number} - %(title)s.%(ext)s'),
        'noplaylist': True,
        'cookiefile': cookie_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Failed to download {url}: {e}")

##