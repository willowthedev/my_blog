from django import forms
from django.conf import settings
from django.forms import fields, widgets
import requests

class ColorForm(forms.Form): 
    color = forms.CharField(max_length=7, required=True, widget=widgets.TextInput(attrs={'class': 'form-control'}))

    def change_color(self):
        color = self.cleaned_data.get('color')
        
        try:
            url = 'https://api.lifx.com/v1/lights/d073d526a9eb/state'


            headers = {
                "Authorization": "Bearer %s" % settings.LIFX_TOKEN,
            }

            payload = {
                "color": color,
            }

            response = requests.put(url, data=payload, headers=headers)  
        except Exception as e: 
            print(e)
