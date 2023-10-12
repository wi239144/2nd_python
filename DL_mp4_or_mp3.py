
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
    #標題當作文件名稱
    titlenmae = yt.title + ".mp3"
    #output:
    aud.download(filename=titlenmae)
    print('download as mp3...')
elif choose == 0 :
    #下載最高畫質影片
    vid = yt.streams.filter().get_highest_resolution()
    #標題當作文件名稱
    titlenmae = yt.title + ".mp4"
    #output:
    vid.download(filename=titlenmae)
    print('download as mp4...')
else:
    print("Error")

print('ok!')

