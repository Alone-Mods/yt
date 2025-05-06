import subprocess

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

def sanitize_filename(name):
    name = name.strip().replace(" ", "_")
    return name if name.endswith(".mp3") else f"{name}.mp3"

def download_video():
    url = input(f"{colors['cyan']}Enter YouTube video URL: {colors['reset']}").strip()
    if not url:
        print(f"{colors['red']}Error: URL is required.{colors['reset']}")
        return

    print(f"\n{colors['green']}Available quality options (example): 360p, 480p, 720p, 1080p{colors['reset']}")
    quality = input(f"{colors['cyan']}Enter desired video resolution (default 720p): {colors['reset']}").strip() or "720p"

    filename = input(f"{colors['cyan']}Enter output filename (e.g., my_video.mp4): {colors['reset']}").strip()
    if not filename.endswith(".mp4"):
        filename += ".mp4"

    format_code = f"bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]"

    command = [
        "yt-dlp",
        "-f", format_code,
        "-o", filename,
        url
    ]

    try:
        print(f"\n{colors['yellow']}Downloading video in {quality} resolution...{colors['reset']}")
        subprocess.run(command, check=True)
        print(f"\n{colors['green']}Success! Video saved as: {filename}{colors['reset']}")
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

    output_file = sanitize_filename(filename)

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