from django.http import Http404, HttpResponse
from django.shortcuts import render

texts = ["Text 1", "Text 2", "Text 3"]

# Create your views here.
def index(request):
    return render(request, "section/index.html")

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("Invalid section")