#!/bin/bash

# Clear terminal
clear

# Big ASH ASCII banner with color
echo -e "\033[1;35m"
echo "               _      __   __           _                  "
echo "     /\\       | |     \\ \\ / /     /\\   | |                 "
echo "    /  \\   ___| |__    \\ V /     /  \\  | | ___  _ __   ___ "
echo "   / /\\ \\ / __| '_ \\    > <     / /\\ \\ | |/ _ \\| '_ \\ / _ \\"
echo "  / ____ \\\\__ \\ | | |  / . \\   / ____ \\| | (_) | | | |  __/"
echo " /_/    \\_\\___/_| |_| /_/ \\_\\ /_/    \\_\\_|\\___/|_| |_|\\___|"
echo -e "                                                           "
echo -e "               \033[1;36mYouTube Media Tool by ASH\033[0m"
echo ""

# Install dependencies
echo -e "\033[1;34mInstalling dependencies (Python, Git, FFmpeg, yt-dlp)...\033[0m"
pkg install -y python git ffmpeg > /dev/null 2>&1
pip install yt-dlp --quiet

# Final message
echo -e "\n\033[1;32mSetup Complete!\033[0m"
echo -e "\033[1;33mRun the tool with:\033[0m \033[1;36mpython yt.py\033[0m"
