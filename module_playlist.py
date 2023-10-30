from pytube import YouTube, Playlist
from pydub import AudioSegment
import module_video

# Function to download a playlist in different resolutions and formats
def download_playlist(res,destination_folder):
    playlist_url = input("Enter Playlist Url: ")
    try:
        playlist = Playlist(playlist_url)
        
        i=1
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            stream = yt.streams.filter(res=res, file_extension='mp4').first()
            stream.download(output_path=destination_folder)
            print("\n-------------------------------------------------------------------------")
            print(f"{i}. Downloaded: {yt.title}")
            i+=1
        
        print("Location: ",destination_folder)
        print("Playlist download completed 😀.")

    except Exception as e:
        print(f"An error occurred: {e}")
