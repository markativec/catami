# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, from the CATAMI team.  We are not up and running yet, you can follow us here for now https://plus.google.com/u/0/b/104765819602128308640/104765819602128308640/posts")
