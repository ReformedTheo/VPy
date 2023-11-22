# VPy - One Pace Python Video Player

## Overview
VPy is a custom-built desktop video player designed for fans of One Pace. Developed in Python using the Tkinter GUI toolkit and VLC Python bindings, it simplifies the experience of watching One Pace episodes from the comfort of your bed. Its user-friendly interface allows for easy playback controls.

## Prerequisites
- Python 3.x
- VLC Media Player
- Python packages: `python-vlc`, `Pillow`

## Installation
1. **VLC Media Player**: Download and install from [the official VLC website](https://www.videolan.org/vlc/).
2. **Python Libraries**: Install necessary libraries:
   ```bash
   pip install python-vlc Pillow

## How to Use VPy

1. **Starting the Application**: 
   - Run the VPy script to open the video player interface.

2. **Load a Video**: 
   - Click "Open File" to choose a One Pace episode from your files(may not work. If it doesn't, hardcode the path inside the main.py file).

3. **Control Playback**: 
   - Use the "Play" and "Pause" buttons to manage video playback.

4. **Skip Intro**: 
   - The application automatically skips to 2 minutes and 40 seconds into each episode.

5. **Next Episode**: 
   - Click "Next" to automatically load and play the next episode in the folder.

6. **Exiting VPy**: 
   - Use the "Quit" button to safely close the application.

## Features

- **Simplified Video Controls**: 
  - Easy-to-use play, pause, and navigation through One Pace episodes.

- **Auto Skip Intro**: 
  - Automatically jumps to 2 minutes and 40 seconds into each episode, skipping the intro.

- **Next Episode Transition**: 
  - Effortlessly move to the next episode in the directory with a single click.

- **Customized for One Pace**: 
  - Specifically designed for a comfortable One Pace viewing experience, particularly from bed.