from django.shortcuts import render

def main(request):
    return render(request, 'pepero/pepero.html')