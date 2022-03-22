
from pytube import YouTube

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url=input("enter video url :")
    my_video= YouTube(url)
    videos = my_video.streams.all()
    vid = list(enumerate(videos))
    for i in vid :
        print(i)
    print()
    strm=int(input("enter : "))

    videos[strm].download()
    print("Sucessfully downloaded")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
