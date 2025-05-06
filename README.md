<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&pause=1000&color=FF0000&center=true&vCenter=true&width=435&lines=Welcome+to+YouTube+Media+Tool+by+Ash;Download+Videos+and+MP3s+Effortlessly;Built+for+Termux!" alt="Typing SVG" />
</p>

# YouTube Media Tool by Ash

A simple, Termux-friendly Python tool to download YouTube **videos** and **audio (MP3)** using `yt-dlp`.

## Features

- Download videos in selected resolutions (360p, 480p, 720p, 1080p)
- Download audio in high-quality MP3 (64k – 320k)
- Automatically moves downloads to `~/storage/downloads/Yt_downloads/`
- Clean, colorful command-line interface


## Requirements

- Download Termux From Here :-
<p align="left">
  <a href="https://f-droid.org/en/packages/com.termux/">
    <img src="https://github.com/Alone-Mods/filesmahnn/blob/main/termux.jpg" alt="Download Termux" width="250" style="vertical-align: middle;"/>
  </a>
</p>

- Python (3.x)
- Git
- yt-dlp
- ffmpeg

## Installation (Termux)

```bash
pkg update && pkg upgrade

#Grant the storage permission:
termux-setup-storage

pkg install python git ffmpeg

pip install yt-dlp

# Clone the repository
git clone https://github.com/Alone-Mods/yt

# Navigate to the folder
cd yt

# Make setup script executable and run it
chmod +x setup.sh
bash setup.sh

# Run the tool
python yt.py
