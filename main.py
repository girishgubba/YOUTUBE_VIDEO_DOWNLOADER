from pytube import YouTube
link = input("Paste Your Link:")
y1 = YouTube(link)
print("Title:",y1.title)
video = y1.streams.filter(progressive=True)
vd = list(enumerate(video))
for i in vd:
    print(i)
print("Choices:")
print("144p:0")
print("360p:1")
print("720p:2")
choice = int(input("Enter Choice:"))
video[choice].download()
print("Downloaded Successfully")