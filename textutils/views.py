# new created by me
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parameters = {'analyzed_text':analyzed}
        return render(request,'analyze.html',parameters)
    else:
        return HttpResponse('Error You did not Checked any option :(')

