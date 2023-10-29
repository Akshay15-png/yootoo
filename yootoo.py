from pytube import YouTube, Playlist
from pydub import AudioSegment
import os


import module_video
import module_playlist
import module_menu

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    
# end def


while (True):
    module_menu.logo()

    if __name__ == "__main__":
        module_menu.main_menu()
        user_input=0
        try :
            user_input=int(input("Enter :"))
        except Exception as e:
            print("Please Enter Valid Input,",e)

        
        destination_folder = "YOUR_DOWNLOADS"

        if (user_input==1):
            
            module_menu.video_menu()
            
            
            try :
                user_input=int(input("Enter :"))

                if(user_input==1):
                    res='144p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==2):
                    res='240p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==3):
                    res='360p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==4):
                    res='480p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==5):
                    res='720p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==6):
                    res='1080p'
                    module_playlist.download_playlist(res,destination_folder)
                elif(user_input==7):
                    clear_screen()
                    module_menu.main_menu()
                else:
                    clear_screen()
                    print("Please enter valid input")

            except Exception as e:
                print("Please Enter Valid Input,",e)
        elif (user_input==2):
            module_menu.video_menu()
            
            
            try :
                user_input=int(input("Enter :"))

                if(user_input==1):
                    res='144p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==2):
                    res='240p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==3):
                    res='360p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==4):
                    res='480p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==5):
                    res='720p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==6):
                    res='1080p'
                    module_video.download_video(res,destination_folder)
                elif(user_input==7):
                    clear_screen()
                    module_menu.main_menu()
                else:
                    clear_screen()
                    print("Please enter valid input")
            
            except Exception as e:
                print("Please Enter Valid Input,",e)

        else:
            print("Good Bye 💀 !")
            exit()
# end while
