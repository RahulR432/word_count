from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html', {"phone": "9985585556"})

def count(request):
    text = request.GET['fullText']
    words = text.split()

    wordDict = {}
    
    for word in words:
        if word in wordDict:
            #increment
            wordDict[word]+=1
        else:
            #add to dict
            wordDict[word]=1

    sortedwords = sorted(wordDict.items(), key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'text': text, 'words':words, 'wordcount':len(words),'wordDict':sortedwords})

