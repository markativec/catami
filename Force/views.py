# Create your views here.
from django.template import Context, loader

from Force.models import auvDeployment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from Force.forms import CampaignForm
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("Hello World, from the CATAMI team.  <br>We are not up and running yet, you can follow us here for now <br>https://plus.google.com/u/0/b/104765819602128308640/104765819602128308640/posts")

def auvdeployments(request):
    latest_auvdeployment_list = auvDeployment.objects.all()
    t = loader.get_template('auvindex2.html')
    c = Context({
        'latest_auvdeployment_list': latest_auvdeployment_list,
    })
    return HttpResponse(t.render(c))
   
def add_campaign(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CampaignForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save();
            return redirect('/Force/campaigns') # Redirect after POST
    else:
        form = CampaignForm() # An unbound form

    return render(request, 'Force/AddCampaign.html', {'form': form})
