from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=UU-Avlo0Riw")

#Title of video
print("Title: ",yt.title)

#Number of views of video
print("Number of views: ",yt.views)

#Length of the video
print("Length of video: ",yt.length,"seconds")

#Description of video
print("Description: ",yt.description)

#Rating
print("Ratings: ",yt.rating)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()