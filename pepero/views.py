from django.shortcuts import render


# Create your views here.
def pepero_make_start_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero.html')
    return render(request, 'peperos/pepero.html')


def pepero_make_choco_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero_make1.html')
    return render(request, 'peperos/pepero_make1.html')

def pepero_make_sauce_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero_make2.html')
    elif request.methd == 'POST':
        pass
        
def pepero_make_deco_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero_make3.html')
    elif request.methd == 'POST':
        pass
    
def pepero_make_letter_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero_letter.html')
    elif request.methd == 'POST':
        pass
    
