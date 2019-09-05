# new created by me
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    upper = request.GET.get('upper','off')
    lower = request.GET.get('lower','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parameters = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',parameters)
    elif upper == 'on':
        analyzed = djtext.upper()
        parameters = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',parameters)
    elif lower == 'on':
        analyzed = djtext.lower()
        parameters = {'purpose':'lowercase','analyzed_text':analyzed}
        return render(request,'analyze.html',parameters)
    else:
        return HttpResponse('<h1>Error: You did not Check any option :(</h1>')

