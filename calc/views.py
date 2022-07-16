from django.shortcuts import render
from pytube import *
import webbrowser

# Create your views here.
def index(request):   
    return render(request, "index.html")

def search(request):
    if request.method == 'POST':
        link = request.POST['link']
        webbrowser.open("https://www.google.com/search?q={}".format(link))
        return render(request,"search.html")
        

def youtube(request):
    
    # checking whether request.method is post or not
    if request.method == 'POST':
        
        # getting link from frontend
        link = request.POST['link']
        resolution = request.POST['resolution']
        try:
            video = YouTube(link)
        except:            
            # print("Connection error")
            return render(request, 'youtube.html', {"variable1": "Connection error"})
  
        # setting video resolution
        stream = video.streams.get_by_resolution(resolution)
          
        # downloads video
        try:
            stream.download()
        except:            
            # print("ERROR!!!")
            return render(request, 'youtube.html', {"variable2": "could not download"})
      
  
        # returning HTML page
        return render(request, 'youtube.html',{"variable3": "download completed"})
    return render(request, 'youtube.html')