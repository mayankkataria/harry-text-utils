from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name': 'Mayank', 'place': 'Udaipur'}
    return render(request, 'index.html')

def analysed(request):

    punctuations = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
    punccheck=request.POST.get('punccheck', 'off')
    capfirstcheck=request.POST.get('capfirstcheck', 'off')
    newlinerem=request.POST.get('newlinerem', 'off')
    extraspacerem=request.POST.get('extraspacerem', 'off')
    simple_text=request.POST.get('text', 'default')
    analysed_text = simple_text
    purpose='default'

    if punccheck == 'on':
                analysed_text = "".join([char for char in simple_text if char not in punctuations])

    if capfirstcheck == 'on':
        analysed_text=analysed_text.title()

    if newlinerem == 'on':
        analysed_text = "".join(char for char in analysed_text if char is not "\n" and char is not "\r")
        purpose = 'newlinerem'

    if extraspacerem == 'on':
        analysed_text = "".join(char for index, char in enumerate(analysed_text) if char is not " " or analysed_text[index+1] != " ")


    params={'purpose': purpose, 'analysed_text': analysed_text}
    return render(request, 'analysed.html', params)