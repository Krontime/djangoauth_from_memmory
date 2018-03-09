from django.shortcuts import render

def get_home_index(request):
    return render(request, 'home/index.html')
    