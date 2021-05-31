# I have created this file - prajeet_kalchuri
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")



def analyze(request):
    #getting the text
    djtext = request.POST.get('text','default')

    #checking the checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')


    #checking which checkbox is ON
    #if removepunc is on remove the puncuations
    if removepunc == "on":
        #analyzed = djtext
        punctuations  = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Puncuations','analyzed_text':analyzed}

        #overiding the djtext
        djtext = analyzed
        #removing all the return statements and returning a final return at the last - doing this for usig all the buttons simulantaneously
        #return render(request,'analyze.html',params)

    #and if fullcaps in on , change all the text into upper case
    if (fullcaps =="on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #and if we click newlineremover
    if(newlineremover == "on"):
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #and for removing extra space
    elif(extraspaceremover == "on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #counting the characters
    if (charactercounter == "on"):
        analyzed = len(djtext)
        #print("Count of the Characters in the given text is : " + str(count))
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #if none of the operations are selected
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on"):
       return HttpResponse("Error: Please choose any operation ")

    #returning here finally
    return render(request, 'analyze.html', params)

