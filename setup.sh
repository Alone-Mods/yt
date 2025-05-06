#!/bin/bash

# Clear the terminal
clear

# Big banner
echo -e "\033[1;35m"
echo "██╗   ██╗████████╗     ███╗   ███╗███████╗██████╗ ██╗ █████╗     ████████╗ ██████╗  ██████╗ ██╗     "
echo "██║   ██║╚══██╔══╝     ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     "
echo "██║   ██║   ██║        ██╔████╔██║█████╗  ██████╔╝██║███████║       ██║   ██║   ██║██║   ██║██║     "
echo "██║   ██║   ██║        ██║╚██╔╝██║██╔══╝  ██╔═══╝ ██║██╔══██║       ██║   ██║   ██║██║   ██║██║     "
echo "╚██████╔╝   ██║        ██║ ╚═╝ ██║███████╗██║     ██║██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗"
echo " ╚═════╝    ╚═╝        ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"
echo "                                     YouTube Media Tool by Ash                                   "
echo -e "\033[0m"

# Install packages
echo -e "\033[1;34mInstalling dependencies (Python, Git, FFmpeg, yt-dlp)...\033[0m"
pkg install -y python git ffmpeg > /dev/null 2>&1
pip install yt-dlp --quiet

# Done message
echo -e "\n\033[1;32mSetup Complete!\033[0m"
echo -e "\033[1;33mRun the tool with:\033[0m \033[1;36mpython yt.py\033[0m"
