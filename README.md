# YouTube Playlist Downloader

A Python-based automation tool for downloading entire YouTube playlists with enhanced features for better user experience. This project leverages `yt-dlp` to simplify the download process with added customization options.

## Features
- Download entire YouTube playlists in one go
- Supports custom folder selection for saving videos
- Allows users to specify desired resolution (e.g., 480p, 720p, 1080p, etc.)
- Automatically merges separate video and audio files into a single MP4 file
- Ensures correct file naming based on video titles for better organization

## Requirements
- Python 3.8+
- `yt-dlp` package

To install `yt-dlp`, run:
```bash
pip install yt-dlp
```

## Setup Instructions
1. Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Run the Program
```bash
python main.py
```

## Usage Instructions
1. Enter Folder Path: Specify the folder where the videos should be saved (leave empty to use the current directory).
2. Paste Playlist URL: Provide the URL of the YouTube playlist you want to download.
3. Select Resolution: Enter the desired resolution (e.g., 480, 720, 1080, etc.).
4. The tool will automatically download and merge video-audio files into MP4 format.

## Example Usage
```
Enter folder path to save videos (leave empty for current folder): D:\MyDownloads\Tutorials
Paste the YouTube playlist URL here: https://www.youtube.com/playlist?list=PLabc123
Enter desired resolution (e.g., 480, 720, 1080, 1440): 1080
```
Playlist downloaded successfully!

## Future Enhancements (Planned)
- Pause and resume download
- Implement video range selection (e.g., download videos 5-10 only).
- Download the video of your choice.
- Provide a progress bar for enhanced visibility

## Author
[Abhishek Maurya]
Feel free to connect and contribute!

