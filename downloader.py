import os
import subprocess
import sys
import shutil  # For checking yt-dlp installation

# --------------------------- CHECK IF yt-dlp IS INSTALLED ---------------------------
# Ensures 'yt-dlp' is available; if not, exits with a helpful message.
if not shutil.which("yt-dlp"):
    print("Error: yt-dlp is not installed. Please install it using 'pip install yt-dlp'.")
    sys.exit(1)

# --------------------------- FUNCTION TO DOWNLOAD FULL PLAYLIST ---------------------------
def download_playlist(url, folder_path, resolution):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # yt-dlp command for downloading playlist
    command = [
        'yt-dlp',
        '-f', f'bv*[height={resolution}]+ba/b',  # Download video + audio in desired resolution
        '--merge-output-format', 'mp4',           # Merge into MP4 format
        '--yes-playlist',                         # Download entire playlist
        '--download-archive', os.path.join(folder_path, 'downloaded_videos.txt'),  # Track downloaded files
        '--no-post-overwrites',  # Skip re-downloading already downloaded files
        url,
        '-o', os.path.join(folder_path, '%(title)s.%(ext)s')  # File naming pattern
    ]

    # Command execution and error handling
    try:
        subprocess.run(command, check=True)
        print("\nPlaylist downloaded successfully!")
    except subprocess.CalledProcessError:
        print("\nError: Failed to download playlist.")
    except Exception as e:
        print(f"\nError: {e}")

# --------------------------- FUNCTION TO DOWNLOAD A SINGLE VIDEO ---------------------------
def download_single_video(url, folder_path, resolution):
    # List all videos in the playlist
    list_command = [
        'yt-dlp',
        '--flat-playlist',   # Only fetch video titles without downloading
        '--print', '%(title)s',
        url
    ]

    try:
        result = subprocess.run(list_command, capture_output=True, text=True, check=True)
        video_titles = result.stdout.strip().split("\n")

        if not video_titles:
            print("Error: No videos found in the playlist.")
            return

        # Display available videos with numbering
        print("\nAvailable Videos:")
        for idx, title in enumerate(video_titles, 1):
            print(f"{idx}. {title}")

        # Select video from the list
        choice = input("\nEnter the number of the video you want to download: ").strip()
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(video_titles):
            print("Error: Invalid selection.")
            return

        selected_video = int(choice)

        # yt-dlp command to download the selected video
        command = [
            'yt-dlp',
            '-f', f'bv*[height={resolution}]+ba/b',
            '--merge-output-format', 'mp4',
            '--playlist-items', str(selected_video),  # Download only the selected video
            '--download-archive', os.path.join(folder_path, 'downloaded_videos.txt'),
            '--no-post-overwrites',  # Skip already downloaded videos
            url,
            '-o', os.path.join(folder_path, '%(title)s.%(ext)s')
        ]

        # Command execution and error handling
        subprocess.run(command, check=True)
        print(f"\n'{video_titles[selected_video - 1]}' downloaded successfully!")
        
    except subprocess.CalledProcessError:
        print("\nError: Failed to retrieve playlist or download video.")
    except Exception as e:
        print(f"\nError: {e}")

# --------------------------- MAIN FUNCTION ---------------------------
def main():
    print("YouTube Playlist Downloader")

    # Step 1: Folder selection
    folder_path = input("Enter folder path to save videos (leave empty for current folder): ").strip()
    if not folder_path:
        folder_path = os.getcwd()  # Default to current folder

    # Step 2: Playlist URL input
    playlist_url = input("Paste the YouTube playlist URL here: ").strip()
    if not playlist_url:
        print("Error: Playlist URL is required.")
        sys.exit(1)

    # Step 3: Resolution input
    resolution = input("Enter desired resolution (e.g., 480, 720, 1080, 1440): ").strip()
    if not resolution.isdigit():
        print("Error: Resolution must be a valid number.")
        sys.exit(1)

    # Step 4: Download options
    print("\nOptions:\n1. Download Full Playlist\n2. Download a Single Video")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        download_playlist(playlist_url, folder_path, resolution)
    elif choice == '2':
        download_single_video(playlist_url, folder_path, resolution)
    else:
        print("Error: Invalid choice.")

# --------------------------- PROGRAM ENTRY POINT ---------------------------
if __name__ == "__main__":
    main()
