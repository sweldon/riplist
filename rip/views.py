from django.shortcuts import render
import youtube_dl
import os
import traceback

savedir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static/upload')

def index(request):

    return render(request, 'rip/rip.html')

def make_savepath(title, savedir=savedir):
    return os.path.join(savedir, "%s.mp3" % (title))

def rip(request):


    # create YouTube downloader
    options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3
        'outtmpl': '%(id)s',        # name the file the ID of the video
        'noplaylist' : True,}       # only download single song, not playlist
    song = youtube_dl.YoutubeDL(options)

    with song:

        link = "https://www.youtube.com/watch?v=21YJcWdiNfI&list=RD21YJcWdiNfI"
        info = song.extract_info(link, download=False)

        savepath = make_savepath(info["title"])
        try:
            os.stat(savepath)
            print "%s already downloaded, continuing..." % savepath
            pass

        except OSError:

            try:
                result = song.extract_info(link, download=True)
                os.rename(result['id'], savepath)
                print "Downloaded and converted %s successfully!" % savepath

            except Exception as e:
                print "Can't download audio! %s\n" % traceback.format_exc()

    return render(request, 'rip/rip.html')