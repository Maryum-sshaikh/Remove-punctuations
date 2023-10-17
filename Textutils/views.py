from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,'index.html')

def analyzed(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','default')
    print(removepunc)
    print(djtext)
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyzed.html', params)

    else:
        return HttpResponse('Error')