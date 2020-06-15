from django.shortcuts import render
from .models import Confession
from .forms import ConfessionForm
# Create your views here.
def index(request):
	form = ConfessionForm(None)
	message = 'not yet databased'
	context = {
		'form':form,
		'message': message
		}
	return render(request,'test.html',context)


def databased(request):
	form = ConfessionForm(request.POST)
	if form.is_valid():
		form.save()
		message = 'Databased'
		context = {
		'form':form,
		'message': message
		}
	return render(request,'test.html',context)
