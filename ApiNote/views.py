from django.shortcuts import render, redirect

# Create your views here.
def introduction(request):
    return render(request, 'Note/introduction.html')


def serialization(request):
    return render(request, 'Note/serialization.html')



def de_serialization(request):
    return render(request, 'Note/de_serialization.html')