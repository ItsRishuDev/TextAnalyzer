from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Getting the text value
    djtext = request.POST.get('text', 'default') 
    
    #Checking checkbox checked
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Analyze the text
    if removepunc == 'on':
        analyzedText = ''
        punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzedText = analyzedText + char

        params = {'taskname':'Remove Panchuation', 'result':analyzedText}
        djtext = analyzedText         

    if uppercase == 'on':
        analyzedText = ''
        for char in djtext:
            analyzedText = analyzedText + char.upper()

        params = {'taskname':'Upper Case', 'result':analyzedText}
        djtext = analyzedText

    if lowercase == 'on':
        analyzedText = ''
        for char in djtext:
            analyzedText = analyzedText + char.lower()

        params = {'taskname':'Lower Case', 'result':analyzedText}
        djtext = analyzedText

    if extraspaceremove == 'on':
        analyzedText = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzedText = analyzedText + char
        params = {'taskname':'Extra Space Remover', 'result':analyzedText}
        djtext = analyzedText   

    if newlineremove == 'on':
        analyzedText = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzedText = analyzedText + char
        params = {'taskname':'New Line Remover', 'result':analyzedText}
        djtext = analyzedText

    if charcount == 'on':
        analyzedText = ''
        count = 0
        for char in djtext:
            count = count + 1
        
        analyzedText = f'Number of character in the text "{djtext}" is : {count}'
        params = {'taskname':'New Line Remover', 'result':analyzedText}
        djtext = analyzedText

    if charcount != 'on' and removepunc != 'on' and newlineremove != 'on' and uppercase != 'on' and lowercase != 'on' and extraspaceremove!='on':
        return HttpResponse('Please choose any operation.')

    return render(request, 'analyze.html', params) 
