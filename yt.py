
import subprocess
import os
import shutil
import glob

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

def sanitize_filename(name, ext=".mp3"):
    name = name.strip().replace(" ", "_")
    return name if name.endswith(ext) else f"{name}{ext}"

def move_to_downloads(file_name):
    # Detect if running in Termux
    is_termux = 'com.termux' in os.environ.get('PREFIX', '')
    if is_termux:
        downloads_dir = os.path.expanduser("~/storage/downloads")
        if not os.path.exists(downloads_dir):
            print(f"{colors['yellow']}Requesting storage permission...{colors['reset']}")
            os.system("termux-setup-storage")
    else:
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    try:
        shutil.move(file_name, os.path.join(downloads_dir, file_name))
        print(f"{colors['green']}Moved to Downloads: {downloads_dir}/{file_name}{colors['reset']}")
    except Exception as e:
        print(f"{colors['red']}Error moving file: {e}{colors['reset']}")

def download_video():
    url = input(f"{colors['cyan']}Enter YouTube video URL: {colors['reset']}").strip()
    if not url:
        print(f"{colors['red']}Error: URL is required.{colors['reset']}")
        return

    print(f"\n{colors['green']}Available quality options: 360p, 480p, 720p, 1080p{colors['reset']}")
    quality = input(f"{colors['cyan']}Enter desired resolution (default 720p): {colors['reset']}").strip() or "720p"

    format_code = f"bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]"
    output_template = "%(title)s.%(ext)s"

    command = [
        "yt-dlp",
        "-f", format_code,
        "-o", output_template,
        url
    ]

    try:
        print(f"\n{colors['yellow']}Downloading video in {quality} resolution...{colors['reset']}")
        subprocess.run(command, check=True)

        downloaded_files = sorted(
            glob.glob("*.webm") + glob.glob("*.mp4") + glob.glob("*.mkv"),
            key=os.path.getmtime,
            reverse=True
        )
        if downloaded_files:
            output_file = downloaded_files[0]
            print(f"{colors['green']}Success! Video saved as: {output_file}{colors['reset']}")
            move = input(f"{colors['cyan']}Move this video to Downloads folder? (y/n): {colors['reset']}").strip().lower()
            if move == "y":
                move_to_downloads(output_file)
        else:
            print(f"{colors['red']}Error: Could not detect downloaded file.{colors['reset']}")

    except subprocess.CalledProcessError as e:
        print(f"\n{colors['red']}Download error: {e}{colors['reset']}")

def download_audio():
    url = input(f"{colors['cyan']}Enter YouTube video link: {colors['reset']}").strip()
    if not url:
        print(f"{colors['red']}Error: You must provide a link.{colors['reset']}")
        return

    print(f"{colors['green']}\nAvailable audio qualities: 64k, 128k, 192k, 256k, 320k{colors['reset']}")
    quality = input(f"{colors['cyan']}Enter desired audio quality (default 128k): {colors['reset']}").strip().lower() or "128k"

    filename = input(f"{colors['cyan']}Enter output file name (e.g., song.mp3): {colors['reset']}").strip()
    if not filename:
        print(f"{colors['red']}Error: You must provide a file name.{colors['reset']}")
        return

    output_file = sanitize_filename(filename, ".mp3")

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", quality,
        "-o", output_file,
        url
    ]

    try:
        print(f"{styles['bold']}{colors['yellow']}\nDownloading and converting to MP3...{styles['reset']}")
        subprocess.run(command, check=True)
        print(f"{styles['bold']}{colors['green']}\nSuccess! Audio saved as: {output_file}{styles['reset']}")

        move = input(f"{colors['cyan']}Move this audio to Downloads folder? (y/n): {colors['reset']}").strip().lower()
        if move == "y":
            move_to_downloads(output_file)

    except subprocess.CalledProcessError as e:
        print(f"{styles['bold']}{colors['red']}Error occurred during download: {e}{styles['reset']}")

def main():
    print(f"{styles['bold']}{colors['magenta']}YOUTUBE MEDIA TOOL BY ASH{colors['reset']}")
    print(f"{colors['blue']}1. Download Video")
    print("2. Download Audio")
    print("0. Exit" + colors['reset'])

    choice = input(f"{colors['yellow']}Select an option: {colors['reset']}").strip()

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
