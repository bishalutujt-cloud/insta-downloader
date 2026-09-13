import os
import yt_dlp

def download_instagram_video(video_url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'quiet': False,
    }

    try:
        print("Downloading video...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Instagram Video/Reel URL paste karein: ")
    download_instagram_video(url)
  
