from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def removePunc(text):
    punctuations = '''!@#$%^&<>《》☆☆¡¿◇♡♤●○•°÷×;€£₹₩*():"",.?/][}{\|=+-_~`'''
    analyzedText = ""
    for char in text:
        if char not in punctuations:
            analyzedText = analyzedText+char
    return analyzedText


def toLower(text):
    analyzedText = text
    analyzedText = analyzedText.lower()
    return analyzedText


def toUpper(text):
    analyzedText = text
    analyzedText = analyzedText.upper()
    return analyzedText


def Analyze(request):
    Text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    uppercase = request.POST.get('uppercase', 'off')

    if (removepunc == 'off' and lowercase == "off" and uppercase == "off") or ( removepunc == 'on' and lowercase == "on" and uppercase == "on"):
            return HttpResponse("Error")

    elif (removepunc == 'on' and uppercase == 'on'):
        result = removePunc(Text)
        result = toUpper(result)
        params = {'purpose': 'Punctuations & UpperCase', 'analyzetext': result}
        return render(request, 'analyze.html', params)

    elif (removepunc == 'on' and lowercase == 'on'):
        result = removePunc(Text)
        result = toLower(result)
        params = {'purpose': 'Punctuations & LowerCase', 'analyzetext': result}
        return render(request, 'analyze.html', params)


    elif removepunc == 'on':
        result = removePunc(Text)
        params = {'purpose': 'Remove Punctuations', 'analyzetext': result}
        return render(request, 'analyze.html', params)
    elif lowercase == "on":
        result = toLower(Text)
        params = {'purpose': 'To LowerCase', 'analyzetext': result}
        return render(request, 'analyze.html', params)
    elif uppercase == "on":
        result = toLower(Text)
        params = {'purpose': 'To UpperCase', 'analyzetext': result}
        return render(request, 'analyze.html', params)
    else:
        pass
