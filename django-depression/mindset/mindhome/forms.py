from django import forms
from .models import Confession

class ConfessionForm(forms.ModelForm):
	class Meta:
		model = Confession
		fields = [
		'text'
		]
		widgets = {
					'text':forms.TextInput(attrs={'placeholder':'Enter your Full feels here'})
		}
		labels = {
					'text':''
		}