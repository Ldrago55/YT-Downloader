from django.shortcuts import render
from pytube import *
import webbrowser

# Create your views here.
def index(request):   
    return render(request, "index.html")

def search(request):
    if request.method == 'POST':
        import requests
        link = request.POST.get('link')
        clg_name = link.replace(" ", "+")
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html_content = session.get(f'https://www.google.com/search?q=+{clg_name}').text
        return html_content

        

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

        # setting path
        SAVE_PATH = "E:/"  
        # setting video resolution
        stream = video.streams.get_by_resolution(resolution)
          
        # downloads video
        try:
            stream.download(SAVE_PATH)
        except:            
            # print("ERROR!!!")
            return render(request, 'youtube.html', {"variable2": "could not download"})
      
  
        # returning HTML page
        return render(request, 'youtube.html',{"variable3": "download completed"})
    return render(request, 'youtube.html')