from django.shortcuts import render

def index1(request):
    return render(request, 'app/index1.html', {})
	
def index(request):
	return render(request, 'app/index.html', {})
# Create your views here.
