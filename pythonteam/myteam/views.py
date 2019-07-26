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
    

class NoteDetails(APIView):
    def get(self, request, pk):
        note = Notes.objects.get(pk=pk)
        serializer = NoteSerializer(note)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        note = Notes.objects.get(pk=pk)
        serializer = NoteSerializer(instance=note, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        note = Notes.objects.get(pk=pk)
        note.delete()
        return Response({"deleted": "yes"}, status=status.HTTP_200_OK)
