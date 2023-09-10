from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == "POST":
        source = request.POST["source"]
        destination = request.POST["destination"]
        
        match source:
            case "spotify":
                pass
            case "apple-music":
                pass
            case "tidal":
                pass
            case "google-play":
                pass
            case "deezer":
                pass
            case _:
                print("Unknown source!")

                
        return render(request, 'musictransferapp/index.html')

    return render(request, 'musictransferapp/index.html')