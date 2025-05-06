#!/bin/bash

# Clear screen and show welcome
clear
echo -e "\033[1;35m"
echo "========================================"
echo "     WELCOME TO YOUTUBE MEDIA TOOL      "
echo "              by Ash                    "
echo "========================================"
echo -e "\033[0m"

# Install dependencies
echo -e "\033[1;34mInstalling required packages...\033[0m"
pkg install -y python git ffmpeg -y > /dev/null 2>&1
pip install yt-dlp --quiet

# Success message
echo -e "\n\033[1;32mInstallation complete!\033[0m"
echo -e "\033[1;33mYou can now run the tool with:\033[0m"
echo -e "\033[1;36mpython yt_tool.py\033[0m"
