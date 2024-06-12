# views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    strings = ["button1", "button2", "button3"]
    return render(request, 'index.html', {'strings': strings})

def handle_button_click(request):
    if request.method == 'POST':
        clicked_string = request.POST.get('clicked_string', '')
        return render(request, 'response.html', {'clicked_string': clicked_string})
    return HttpResponse('Invalid request', status=400)
