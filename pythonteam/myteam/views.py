from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserProfileInfo
# Create your views here.


def login(request):
    return render('login.html')


def sing_up(request):
    username = request.data.get("user")
    image = request.FILES['image']
    user = UserProfileInfo.objects.create(user=username, image=image)
    return HttpResponseRedirect('login', user)

def CreateNote(CreateAPIView):
    serializer_class = NoteSerializer


def demo(request):
	return render(request, 'demo.html')
    
