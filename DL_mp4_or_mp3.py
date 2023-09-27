
from pytube import YouTube

# 0 = download as mp4, 1 = download as mp3
choose = 1
url = "https://www.youtube.com/watch?v=XXXXXXXXXXX"

#age restrictions or private film
yt = YouTube(
    url,
    use_oauth=True,
    allow_oauth_cache=True
    )

if choose == 1 :
    #download mp3
    aud = yt.streams.filter(only_audio=True).first()
    aud.download(filename='downloadaudio.mp3')
    print('download as mp3...')
elif choose == 0 :
    #下載最高畫質影片
    vid = yt.streams.filter().get_highest_resolution()
    vid.download(filename='downloadvideo.mp4')
    print('download as mp4...')
else:
    print("Error")

print('ok!')

