from pytube import YouTube

def download_video_at_720p(video_url):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='720p').first()
    video_stream.download(output_path=".", filename=yt.title + ".mp4")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video_at_720p(video_url)
