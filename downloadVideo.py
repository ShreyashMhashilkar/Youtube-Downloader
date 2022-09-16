from pytube import YouTube 
  
def download_video(link):  
# where to save 
    print(link)
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
    stream.download()

# if __name__=="__main__":
#     link = "https://youtu.be/qPtScmB8CgA"
#     download_video(link)