# YouTube Media Tool by Ash

A simple Termux-compatible Python tool to download YouTube **videos** and **audio (MP3)** using `yt-dlp`.

## Features

- Download videos in selected resolutions (360p, 480p, 720p, etc.)
- Download audio in high-quality MP3 (64k – 320k)
- Clean, colored CLI interface
- Works offline once dependencies are installed

## Requirements

- Python (3.x)
- Git
- yt-dlp
- ffmpeg

## Installation (in Termux)

```bash
pkg update && pkg upgrade
pkg install python git ffmpeg
pip install yt-dlp
git clone https://github.com/Alone-Mods/yt
cd yt
chmod +x setup.sh
bash setup.sh
