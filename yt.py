import subprocess
import os
import shutil
from pathlib import Path

# ANSI styles for color and bold text
styles = {
    "bold": "\033[1m",
    "reset": "\033[0m"
}

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

# Set up target folder path
downloads_dir = os.path.expanduser('~/storage/downloads/Yt_downloads')
os.makedirs(downloads_dir, exist_ok=True)

def sanitize_filename(name):
    name = name.strip().replace(" ", "_")
    return name

def download_video():
    url = input(f"{colors['cyan']}Enter YouTube video URL: {colors['reset']}").strip()
    if not url:
        print(f"{colors['red']}Error: URL is required.{colors['reset']}")
        return

    print(f"\n{colors['green']}Example quality options: 360p, 480p, 720p, 1080p{colors['reset']}")
    quality = input(f"{colors['cyan']}Enter desired resolution (default 720p): {colors['reset']}").strip() or "720p"

    filename = input(f"{colors['cyan']}Enter output filename (e.g., my_video.mp4): {colors['reset']}").strip()
    if not filename.endswith(".mp4"):
        filename += ".mp4"
    filename = sanitize_filename(filename)

    print(f"Final filename: {filename}")

    format_code = f"bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]"

    command = [
        "yt-dlp",
        "-f", format_code,
        "-o", filename,
        "--merge-output-format", "mp4",
        url
    ]

    try:
        print(f"\n{colors['yellow']}Downloading video...{colors['reset']}")
        subprocess.run(command, check=True)
        print(f"{colors['green']}Downloaded: {filename}{colors['reset']}")

        target_path = os.path.join(downloads_dir, filename)
        if os.path.exists(filename):
            shutil.move(filename, target_path)
            print(f"{colors['cyan']}Moved to: {target_path}{colors['reset']}")
        else:
            print(f"{colors['red']}Error: File '{filename}' not found. Skipping move.{colors['reset']}")

    except subprocess.CalledProcessError as e:
        print(f"{colors['red']}Download failed: {e}{colors['reset']}")
    except Exception as e:
        print(f"{colors['red']}Move failed: {e}{colors['reset']}")

def download_audio():
    url = input(f"{colors['cyan']}Enter YouTube audio URL: {colors['reset']}").strip()
    if not url:
        print(f"{colors['red']}Error: URL is required.{colors['reset']}")
        return

    print(f"{colors['green']}\nAvailable qualities: 64k, 128k, 192k, 256k, 320k{colors['reset']}")
    quality = input(f"{colors['cyan']}Enter desired quality (default 128k): {colors['reset']}").strip() or "128k"

    filename = input(f"{colors['cyan']}Enter output filename (e.g., song.mp3): {colors['reset']}").strip()
    if not filename.endswith(".mp3"):
        filename += ".mp3"
    filename = sanitize_filename(filename)

    print(f"Final filename: {filename}")

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", quality,
        "-o", filename,
        url
    ]

    try:
        print(f"\n{styles['bold']}{colors['yellow']}Downloading audio...{styles['reset']}")
        subprocess.run(command, check=True)
        print(f"{colors['green']}Downloaded: {filename}{colors['reset']}")

        target_path = os.path.join(downloads_dir, filename)
        if os.path.exists(filename):
            shutil.move(filename, target_path)
            print(f"{colors['cyan']}Moved to: {target_path}{colors['reset']}")
        else:
            print(f"{colors['red']}Error: File '{filename}' not found. Skipping move.{colors['reset']}")

    except subprocess.CalledProcessError as e:
        print(f"{colors['red']}Download error: {e}{colors['reset']}")
    except Exception as e:
        print(f"{colors['red']}Move failed: {e}{colors['reset']}")

def main():
    print(f"{styles['bold']}{colors['magenta']}\nYOUTUBE MEDIA TOOL - ASH{colors['reset']}")
    print(f"{colors['blue']}1. Download Video")
    print("2. Download Audio")
    print("0. Exit" + colors['reset'])

    choice = input(f"{colors['yellow']}Choose an option: {colors['reset']}").strip()

    if choice == '1':
        download_video()
    elif choice == '2':
        download_audio()
    elif choice == '0':
        print(f"{colors['green']}Goodbye!{colors['reset']}")
    else:
        print(f"{colors['red']}Invalid choice!{colors['reset']}")

if __name__ == "__main__":
    main()
