from django.shortcuts import render
from .models import ImageUpload
# Create your views here.
def index(request):

    # title: str 
    #image: str
    #uploaded_at: str
        
    """snap1 = ImageUpload()
    snap1.title = 'Smirth Jon'
    snap1.image = 't1.jpg'

    snap2 = ImageUpload()
    snap2.title = 'Jean Doe'
    snap2.image = 't2.jpg'

    snap3 = ImageUpload()
    snap3.title = 'Alex Dan'
    snap3.image = 't3.jpg'

    snaps = [snap1, snap2, snap3]"""

    snaps = ImageUpload.objects.all()
    return render(request, "index.html", {'snaps': snaps})

def why(request):
    return render(request, "why.html")

#def trainer(request):
#    return render(request, "trainer.html")

def trainer(request):

    # title: str 
    #image: str
    #uploaded_at: str
        
    snap1 = ImageUpload()
    snap1.title = 'Smirth Jon'
    snap1.image = 't1.jpg'

    snap2 = ImageUpload()
    snap2.title = 'Jean Doe'
    snap2.image = 't2.jpg'

    snap3 = ImageUpload()
    snap3.title = 'Alex Dan'
    snap3.image = 't3.jpg'

    snaps = [snap1, snap2, snap3]
    #pic = ImageUpload.objects.all()
    return render(request, "trainer.html", {'snaps': snaps})

def contact(request):
    return render(request, "contact.html")
