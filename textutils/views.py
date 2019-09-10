# new created by me
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    upper = request.POST.get('upper','off')
    lower = request.POST.get('lower','off')
    nlremover = request.POST.get('nlremover','off')
    charcounter = request.POST.get('charcounter','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parameters = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed
    if upper == 'on':
        analyzed = djtext.upper()
        parameters = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed
    if lower == 'on':
        analyzed = djtext.lower()
        parameters = {'purpose':'lowercase','analyzed_text':analyzed}
        djtext = analyzed
    if nlremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                analyzed = analyzed + ' '
        parameters = {'purpose':'NewLine Remover','analyzed_text':analyzed}
        djtext = analyzed
    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
            if char == ' ':
                pass
            else:
                analyzed=analyzed+1
        parameters = {'purpose':'Char Counter','analyzed_text':analyzed}
    
    if removepunc != 'on' and nlremover != 'on' and charcounter != 'on' and upper != 'on' and lower != 'on':
        return render(request, 'sorry.html')

    return render(request,'analyze.html',parameters)
def about(request):
    return render(request,'about.html')

