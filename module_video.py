from pytube import YouTube, Playlist
from pydub import AudioSegment

# Function to download a single video in different resolutions and formats
def download_video(res,destination_folder):
    video_url = input("Enter Video Url: ")
    try:
        yt = YouTube(video_url)

        # List available video streams
        stream = yt.streams.filter(res=res, file_extension='mp4').first()

        if stream:
            print("\n")
            stream.download(output_path=destination_folder)
            print(f"Downloaded: {stream}")
            print(f"Location: destination_folder")
        else:
            print(f"No matching stream available for the specified resolution and format.")

        print("Your Video downloaded Successfully 😀.")

    except Exception as e:
        print(f"An error occurred: {e}")


def download_video_for_playlist(video_url,res,destination_folder):
    
    try:
        yt = YouTube(video_url)

        # List available video streams
        stream = yt.streams.filter(res=res, file_extension='mp4').first()
        
        if stream:
            print("\n")
            stream.download(output_path=destination_folder)
            print("\n-------------------------------------------------------------------------")
            print(f"Downloaded: {yt.title}")
            print("Location: ",destination_folder)
        else:
            print(f"No matching stream available for the specified resolution and format.")

        print("Your Video downloaded Successfully 😀.")

    except Exception as e:
        print(f"An error occurred: {e}")
# end def
