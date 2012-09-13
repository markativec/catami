__author__ = 'mat'

from django.forms import ModelForm
from models import campaign

#class CampaignForm(forms.Form):
#    description = forms.Textarea()
#    associatedResearchers = forms.Textarea()
#    associatedPublications = forms.Textarea()
#    associatedResearchGrant = forms.TextInput()
#    dateStart = forms.SplitDateTimeWidget()
#    dateEnd = forms.SplitDateTimeWidget()

class CampaignForm(ModelForm):
    class Meta:
        model = campaign