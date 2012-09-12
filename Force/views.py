# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from Force.models import auvDeployment

def index(request):
    return HttpResponse("Hello World, from the CATAMI team.  <br>We are not up and running yet, you can follow us here for now <br>https://plus.google.com/u/0/b/104765819602128308640/104765819602128308640/posts")
def auvdeployments(request):
    latest_auvdeployment_list = auvDeployment.objects.all()
    t = loader.get_template('auvindex2.html')
    c = Context({
        'latest_auvdeployment_list': latest_auvdeployment_list,
    })
    return HttpResponse(t.render(c))